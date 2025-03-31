from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

response = client.chat.completions.create(
    model="gpt-4-1106-preview",
    messages=[
        {
            "role": "system",
            "content": "Você é um assistente treinado para responder perguntas com base em livros."
        },
        {
            "role": "user",
            "content": "Quais são os títulos dos livros disponíveis?"
        }
    ],
    tools=[
        {"type": "file_search"}
    ],
    tool_choice={"type": "file_search"},
    file_search={
        "vector_store_ids": ["vs_67eac6ed32648191baa934730017735c"]
    }
)

print(response.choices[0].message.content.strip())
