import os
import requests
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
ASSISTANT_ID = os.getenv("ASSISTANT_ID")

if not OPENAI_API_KEY:
    print("❌ OPENAI_API_KEY não encontrada.")
    exit(1)

HEADERS = {
    "Authorization": f"Bearer {OPENAI_API_KEY}",
    "OpenAI-Beta": "assistants=v2"
}

# 1. Obter o assistente
res = requests.get(
    f"https://api.openai.com/v1/assistants/{ASSISTANT_ID}",
    headers=HEADERS
)

if res.status_code != 200:
    print("❌ Erro ao buscar assistente:", res.text)
    exit(1)

assistant = res.json()
vs_ids = assistant["tool_resources"]["file_search"]["vector_store_ids"]

if not vs_ids:
    print("❌ Nenhum vector store vinculado.")
    exit(1)

vectorstore_id = vs_ids[0]

# 2. Listar arquivos do vectorstore
res = requests.get(
    f"https://api.openai.com/v1/vector_stores/{vectorstore_id}/files",
    headers=HEADERS
)

if res.status_code != 200:
    print("❌ Erro ao buscar arquivos:", res.text)
    exit(1)

files = res.json().get("data", [])

print(f"\n📌 Assistant: {assistant['name']}")
print(f"🧠 Vector Store ID: {vectorstore_id}")
print(f"📚 Arquivos encontrados ({len(files)}):\n")

for i, f in enumerate(files, 1):
    print(f"{i}. {f['filename']} (ID: {f['id']}) - Status: {f.get('status', 'desconhecido')}")

print("\n✅ Verificação concluída.")
