# test_vectorstore.py

from openai import OpenAI
import os
from dotenv import load_dotenv

# Carregar variáveis do .env
load_dotenv()

# Inicializar cliente com nova API
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# ID do vectorstore atualizado
VECTORSTORE_ID = "vs_67eac6ed32648191baa934730017735c"

# Criar a chamada com ferramenta file_search
response = client.chat.completions.create(
    model="gpt-4-1106-preview",
    messages=[
        {
            "role": "system",
            "content": "Você é um assistente treinado para responder perguntas com base nos livros do Mario Mayerle."
        },
        {
            "role": "user",
            "content": "Quais são os títulos dos livros?"
        }
    ],
    tools=[
        { "type": "file_search" }
    ],
    tool_choice={ "type": "file_search" },
    file_search={ "vector_store_ids": [VECTORSTORE_ID] },
    max_tokens=1024
)

# Mostrar resposta
print(response.choices[0].message.content.strip())
