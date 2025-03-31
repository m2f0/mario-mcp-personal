# ./engine/book_qa.py

import os
import time
from dotenv import load_dotenv
from openai import OpenAI

# Carregar chave da OpenAI
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

ASSISTANT_ID = "asst_zgKsZ5XOt8y8XVVsxIaCdNWH"

def query_books(question: str) -> str:
    try:
        # Criar um novo thread
        thread = client.beta.threads.create()

        # Adicionar a mensagem do usuário ao thread
        client.beta.threads.messages.create(
            thread_id=thread.id,
            role="user",
            content=question
        )

        # Iniciar o processamento com o assistant
        run = client.beta.threads.runs.create(
            thread_id=thread.id,
            assistant_id=ASSISTANT_ID
        )

        # Aguardar até o processamento ser concluído
        while True:
            run_status = client.beta.threads.runs.retrieve(
                thread_id=thread.id,
                run_id=run.id
            )
            if run_status.status == "completed":
                break
            elif run_status.status in ["failed", "cancelled", "expired"]:
                return f"Erro: execução interrompida ({run_status.status})"
            time.sleep(1)

        # Buscar a resposta final
        messages = client.beta.threads.messages.list(thread_id=thread.id)
        resposta = messages.data[0].content[0].text.value
        return resposta.strip()

    except Exception as e:
        return f"Erro ao consultar livros via assistant: {str(e)}"
