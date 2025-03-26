import os
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

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
