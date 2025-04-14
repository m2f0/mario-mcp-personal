import os
import sys
from flask import Flask, jsonify, request
import json
from flask_cors import CORS
from flask import render_template
import psutil
import platform
import time
import requests
from datetime import datetime
from flasgger import Swagger
from engines.book_qa import query_books
from flask import Flask, send_from_directory, jsonify
from tools.mario_images_tool import mario_images_tool
from flask import request, redirect, render_template_string
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

app = Flask(__name__)
CORS(app)

swagger_config = {
    "headers": [],
    "specs": [
        {
            "endpoint": 'apispec_1',
            "route": '/swagger.json',
            "rule_filter": lambda rule: True,
            "model_filter": lambda tag: True,
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/docs/"
}

swagger_template = {
    "swagger": "2.0",
    "info": {
        "title": "Mario Mayerle MCP API",
        "description": "Documentação interativa da API do MCP",
        "version": "1.0.0"
    },
    "basePath": "/",
    "schemes": ["https", "http"]
}

swagger = Swagger(app, config=swagger_config, template=swagger_template)

START_TIME = time.time()

base_path = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(base_path, "resources", "linkedin.json")) as f:
    linkedin = json.load(f)
with open(os.path.join(base_path, "resources", "github.json")) as f:
    github = json.load(f)
with open(os.path.join(base_path, "resources", "blogposts.json")) as f:
    blog = json.load(f)

@app.route("/resources/livros", methods=["POST"])
def livros_query():
    data = request.get_json()
    pergunta = data.get("query", "").strip()

    if not pergunta:
        return jsonify({"erro": "Você deve fornecer uma pergunta no campo 'query'."}), 400

    resposta = query_books(pergunta)
    return jsonify({"resposta": resposta})


@app.route("/agent", methods=["POST"])
def ask_agent():
    """
    Endpoint que pergunta ao agente GPT baseado nos dados do MCP.
    ---
    tags:
      - Agente GPT
    parameters:
      - name: question
        in: body
        required: true
        schema:
          type: object
          properties:
            question:
              type: string
              example: "Quais são os principais projetos do Mario?"
    responses:
      200:
        description: Resposta gerada pelo agente GPT
    """
    data = request.get_json()
    question = data.get("question", "")

    if not question:
        return jsonify({"error": "Campo 'question' é obrigatório"}), 400

    # Monta o contexto com base nos dados locais
    context = {
        "linkedin": linkedin,
        "github": github,
        "blogposts": blog
    }

    prompt = f"""
Você é um agente que responde perguntas com base nos dados públicos do Mario Mayerle. Aqui estão os dados disponíveis:

LinkedIn:
{json.dumps(context['linkedin'], indent=2)}

GitHub:
{json.dumps(context['github'], indent=2)}

Blogposts:
{json.dumps(context['blogposts'], indent=2)}

Pergunta do usuário: {question}
Responda de forma clara e objetiva.
    """

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Você é um assistente pessoal especializado em dados públicos do Mario Mayerle."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )

        answer = response.choices[0].message.content.strip()
        return jsonify({"answer": answer})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    

@app.route('/resources', methods=['GET'])
def list_resources():
    """
    Lista todos os dados de LinkedIn, GitHub e blog em um único JSON.
    ---
    tags:
      - Recursos
    responses:
      200:
        description: JSON com todos os recursos carregados
    """
    return jsonify({
        "linkedin": linkedin,
        "github": github,
        "blogposts": blog
    })

@app.route("/")
def status_page():
    """
    Página de status com visualização HTML.
    ---
    tags:
      - Interface
    responses:
      200:
        description: Página HTML com status da aplicação
    """
    return render_template("status.html")

@app.route('/resources/linkedin', methods=['GET'])
def get_linkedin():
    """
    Retorna os dados completos do LinkedIn.
    ---
    tags:
      - Recursos
    responses:
      200:
        description: Dados do LinkedIn
    """
    return jsonify(linkedin)

@app.route('/resources/github', methods=['GET'])
def get_github():
    """
    Retorna os dados dos repositórios GitHub.
    ---
    tags:
      - Recursos
    responses:
      200:
        description: Dados dos repositórios GitHub
    """
    return jsonify(github)

@app.route('/resources/blogposts', methods=['GET'])
def get_blogposts():
    """
    Retorna os posts completos do blog.
    ---
    tags:
      - Recursos
    responses:
      200:
        description: Lista completa dos posts do blog
    """
    with open(os.path.join(base_path, "resources", "blogposts.json"), encoding="utf-8") as f:
        blog = json.load(f)
    return jsonify(blog)



@app.route('/resources/blogposts_simple', methods=['GET'])
def list_blogposts_simple():
    """
    Retorna os 5 posts mais recentes do blog com título e URL.
    ---
    tags:
      - Recursos
    responses:
      200:
        description: Lista simplificada de posts recentes
    """
    with open(os.path.join(base_path, "resources", "blogposts.json"), encoding="utf-8") as f:
        blog = json.load(f)

    simple_posts = [
        {
            "title": post["title"],
            "url": post["url"]
        }
        for post in blog["posts"][:5]
    ]
    return jsonify({"posts": simple_posts})


@app.route('/tools/get_project_details', methods=['GET'])
def get_project_details():
    """
    Retorna detalhes de um repositório pelo nome.
    ---
    tags:
      - GitHub
    parameters:
      - name: repo_name
        in: query
        type: string
        required: true
        description: Nome do repositório para busca
    responses:
      200:
        description: Detalhes do repositório encontrado
      404:
        description: Projeto não encontrado
    """
    repo_name = request.args.get('repo_name')
    for repo in github["repositories"]:
        if repo["name"].lower() == repo_name.lower():
            return jsonify(repo)
    return jsonify({"error": "Projeto não encontrado"}), 404

@app.route("/resources/livros_indexados", methods=["GET"])
def get_indexed_books():
    """
    Lista os livros de Mario Mayerle diretamente do vectorstore.
    ---
    tags:
      - Recursos
    responses:
      200:
        description: Lista de livros presentes no vectorstore
    """
    import os
    import requests

    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    ASSISTANT_ID = os.getenv("ASSISTANT_ID")

    if not OPENAI_API_KEY or not ASSISTANT_ID:
        return jsonify({"erro": "Variáveis de ambiente OPENAI_API_KEY ou ASSISTANT_ID não estão configuradas."}), 500

    HEADERS = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "OpenAI-Beta": "assistants=v2"
    }

    # Obter o assistente
    res = requests.get(f"https://api.openai.com/v1/assistants/{ASSISTANT_ID}", headers=HEADERS)
    if res.status_code != 200:
        return jsonify({"erro": "Erro ao buscar assistente", "detalhes": res.text}), 500

    assistant = res.json()
    vs_ids = assistant.get("tool_resources", {}).get("file_search", {}).get("vector_store_ids", [])

    if not vs_ids:
        return jsonify({"erro": "Nenhum vector store vinculado ao assistente."}), 404

    vectorstore_id = vs_ids[0]

    # Listar arquivos do vectorstore
    res = requests.get(f"https://api.openai.com/v1/vector_stores/{vectorstore_id}/files", headers=HEADERS)
    if res.status_code != 200:
        return jsonify({"erro": "Erro ao buscar arquivos", "detalhes": res.text}), 500

    files = res.json().get("data", [])

    livros = []
    for f in files:
        file_id = f["id"]
        file_info = requests.get(f"https://api.openai.com/v1/files/{file_id}", headers=HEADERS).json()
        livros.append({
            "id": file_id,
            "nome": file_info.get("filename", "desconhecido"),
            "status": f.get("status", "desconhecido")
        })

    return jsonify({"livros": livros})



# --- NOVO ENDPOINT DE STATUS ---

def check_service_status(url):
    try:
        response = requests.get(url, timeout=5)
        return "online" if response.status_code == 200 else "offline"
    except:
        return "offline"

@app.route('/status', methods=['GET'])
def get_status():
    """
    Retorna o status do sistema, consumo de recursos e disponibilidade dos serviços.
    ---
    tags:
      - Status
    responses:
      200:
        description: JSON com métricas de status do MCP
    """
    uptime_seconds = int(time.time() - START_TIME)
    uptime_str = time.strftime("%H:%M:%S", time.gmtime(uptime_seconds))

    base_url = "https://mcp.mariomayerle.com"

    status_info = {
        "mcp_backend": "online",
        "frontend_ui": check_service_status(base_url),
        "linkedin_scraper": check_service_status(f"{base_url}/resources/linkedin"),
        "blog_feed": check_service_status("https://hubiabrasil.com.br"),
        "api_resources": check_service_status(f"{base_url}/resources"),
        "api_github": check_service_status(f"{base_url}/resources/github"),
        "api_blogposts": check_service_status(f"{base_url}/resources/blogposts"),
        "api_project_details_example": check_service_status(f"{base_url}/tools/get_project_details?repo_name=mcp"),
        "cpu_usage": f"{psutil.cpu_percent()}%",
        "ram_usage": f"{psutil.virtual_memory().percent}%",
        "uptime": uptime_str,
        "host_os": platform.system(),
        "last_update": datetime.utcnow().isoformat() + "Z"
    }

    return jsonify(status_info)
# --- FIM DO BLOCO DE STATUS ---

@app.route("/imagens/<path:filename>")
def servir_imagem(filename):
    return send_from_directory("static/imagens", filename)

@app.route("/resources/imagens")
def listar_imagens():
    return jsonify(mario_images_tool.run(None))

UPLOAD_HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Upload de Imagem - Mario MCP</title>
</head>
<body>
    <h2>Enviar nova imagem</h2>
    <form action="/upload_imagem" method="post" enctype="multipart/form-data">
        <label>Imagem:</label><br>
        <input type="file" name="imagem" accept="image/*" required><br><br>
        <label>Descrição:</label><br>
        <input type="text" name="descricao" style="width: 400px;" required><br><br>
        <button type="submit">Enviar</button>
    </form>
</body>
</html>
"""

@app.route("/upload_imagem", methods=["GET", "POST"])
def upload_imagem():
    if request.method == "POST":
        imagem = request.files.get("imagem")
        descricao = request.form.get("descricao", "").strip()

        if not imagem or not descricao:
            return "Imagem e descrição são obrigatórias", 400

        # Salvar imagem
        save_path = os.path.join(STATIC_DIR, imagem.filename)
        imagem.save(save_path)

        # Atualizar imagens_metadata.json
        with open(METADATA_FILE, "r", encoding="utf-8") as f:
            dados = json.load(f)

        dados.append({
            "filename": imagem.filename,
            "descricao": descricao
        })

        with open(METADATA_FILE, "w", encoding="utf-8") as f:
            json.dump(dados, f, ensure_ascii=False, indent=2)

        return f"""<p>✅ Imagem <b>{imagem.filename}</b> enviada com sucesso!</p>
        <p><a href="/upload_imagem">Voltar</a></p>"""

    return render_template_string(UPLOAD_HTML)



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)