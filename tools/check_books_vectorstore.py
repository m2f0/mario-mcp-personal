import os
import openai
from dotenv import load_dotenv

# Carregar variáveis do .env
load_dotenv()

# Obter chave da OpenAI do .env
openai.api_key = os.getenv("OPENAI_API_KEY")
ASSISTANT_ID = os.getenv("ASSISTANT_ID", "asst_zgKsZ5XOt8y8XVVsxIaCdNWH")

if not openai.api_key:
    print("❌ OPENAI_API_KEY não encontrada no .env")
    exit(1)

# Obter o assistente
assistant = openai.beta.assistants.retrieve(ASSISTANT_ID)

print(f"\n📌 Assistant Name: {assistant.name}")
print(f"🧠 Vector Store ID: {assistant.tool_resources.file_search.vector_store_ids}\n")

# Obter arquivos do vectorstore
vectorstore_id = assistant.tool_resources.file_search.vector_store_ids[0]
vs = openai.beta.vector_stores.retrieve(vectorstore_id)
files = openai.beta.vector_stores.files.list(vector_store_id=vectorstore_id)

print(f"📚 Arquivos conectados ao vectorstore ({len(files.data)}):\n")
for i, f in enumerate(files.data, 1):
    print(f"{i}. {f.filename} (ID: {f.id})")

print("\n✅ Verificação concluída.")
