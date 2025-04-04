import os
from dotenv import load_dotenv
import openai

# Carregar variáveis do .env
load_dotenv()

# Pegar variáveis do ambiente
openai.api_key = os.getenv("OPENAI_API_KEY")
ASSISTANT_ID = os.getenv("ASSISTANT_ID", "asst_zgKsZ5XOt8y8XVVsxIaCdNWH")

if not openai.api_key:
    print("❌ OPENAI_API_KEY não encontrada no .env")
    exit(1)

# Obter dados do assistente
assistant = openai.beta.assistants.retrieve(ASSISTANT_ID)

vectorstore_ids = assistant.tool_resources["file_search"]["vector_store_ids"]

if not vectorstore_ids:
    print("❌ Nenhum vector store associado ao assistente.")
    exit(1)

vectorstore_id = vectorstore_ids[0]

# Listar arquivos no vectorstore
files = openai.beta.vector_stores.files.list(vector_store_id=vectorstore_id)

print(f"\n📌 Assistant: {assistant.name}")
print(f"🧠 Vector Store ID: {vectorstore_id}")
print(f"📚 Arquivos encontrados ({len(files.data)}):\n")

for i, file in enumerate(files.data, 1):
    print(f"{i}. {file.filename} (ID: {file.id})")

print("\n✅ Verificação concluída.")
