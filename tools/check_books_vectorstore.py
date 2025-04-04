import os
from dotenv import load_dotenv
from openai import OpenAI

# Carrega .env e inicializa client
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
ASSISTANT_ID = os.getenv("ASSISTANT_ID", "asst_zgKsZ5XOt8y8XVVsxIaCdNWH")

# Pega o assistente
assistant = client.beta.assistants.retrieve(ASSISTANT_ID)

# Pega vectorstore vinculado ao assistente
vectorstore_ids = assistant.tool_resources.file_search.vector_store_ids

if not vectorstore_ids:
    print("❌ Nenhum vector store encontrado no assistente.")
    exit(1)

vectorstore_id = vectorstore_ids[0]

# Lista arquivos do vectorstore
files = client.beta.vector_stores.files.list(vector_store_id=vectorstore_id)

print(f"\n📌 Assistant: {assistant.name}")
print(f"🧠 Vector Store ID: {vectorstore_id}")
print(f"📚 Arquivos conectados ({len(files.data)}):\n")

for i, file in enumerate(files.data, 1):
    status = file.status
    print(f"{i}. {file.filename} (ID: {file.id}) - Status: {status}")

print("\n✅ Verificação concluída.")
