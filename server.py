from mcp_sdk.server import MCPServer
import json

class PersonalMCP(MCPServer):
    def __init__(self):
        super().__init__(name="MarioPersonalMCP")
        # Carregar recursos
        with open("resources/linkedin.json") as f:
            self.linkedin = json.load(f)
        with open("resources/github.json") as f:
            self.github = json.load(f)
        with open("resources/blogposts.json") as f:
            self.blog = json.load(f)

    # Expondo recursos
    def get_resources(self):
        return {
            "linkedin": self.linkedin,
            "github": self.github,
            "blogposts": self.blog
        }

    # Ferramenta: buscar projeto específico
    def get_project_details(self, repo_name):
        for repo in self.github["repositories"]:
            if repo["name"] == repo_name:
                return repo
        return {"error": "Projeto não encontrado"}

if __name__ == "__main__":
    server = PersonalMCP()
    server.run(host="0.0.0.0", port=8000)
