import requests
import json

# Exemplo para atualizar GitHub
def update_github():
    username = "seu-usuario"
    response = requests.get(f"https://api.github.com/users/{username}/repos")
    repos = [{"name": repo["name"], "url": repo["html_url"]} for repo in response.json()]
    with open("resources/github.json", "w") as f:
        json.dump({"repositories": repos}, f, indent=4)

update_github()
