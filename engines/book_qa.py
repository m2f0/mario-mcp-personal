# ./engine/book_qa.py

import os
from openai import OpenAI
from dotenv import load_dotenv

# Carrega a chave da OpenAI
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

VECTORSTORE_ID = "vs_67eac6ed32648191baa934730017735c"

def query_books(question, model="gpt-4-1106-preview", temperature=0.3):
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {
                    "role": "system",
                    "content": "Você é um assistente treinado para responder perguntas com base no conteúdo de livros autorais fornecidos em PDF."
                },
                {
                    "role": "user",
                    "content": question
                }
            ],
            temperature=temperature,
            tools=[
                {
                    "type": "file_search"
                }
            ],
            tool_choice="file_search",
            file_search={"vector_store_ids": [VECTORSTORE_ID]},
        )

        return response.choices[0].message.content.strip()

    except Exception as e:
        return f"Erro ao consultar livros: {str(e)}"
