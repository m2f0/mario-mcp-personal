import os
from flask import Flask, jsonify, request
import json

app = Flask(__name__)

base_path = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(base_path, "resources", "linkedin.json")) as f:
    linkedin = json.load(f)
with open(os.path.join(base_path, "resources", "github.json")) as f:
    github = json.load(f)
with open(os.path.join(base_path, "resources", "blogposts.json")) as f:
    blog = json.load(f)

@app.route('/resources', methods=['GET'])
def list_resources():
    return jsonify({
        "linkedin": linkedin,
        "github": github,
        "blogposts": blog
    })

@app.route('/resources/linkedin', methods=['GET'])
def get_linkedin():
    return jsonify(linkedin)

@app.route('/resources/github', methods=['GET'])
def get_github():
    return jsonify(github)

@app.route('/resources/blogposts', methods=['GET'])
def get_blogposts():
    return jsonify(blog)

@app.route('/tools/get_project_details', methods=['GET'])
def get_project_details():
    repo_name = request.args.get('repo_name')
    for repo in github["repositories"]:
        if repo["name"].lower() == repo_name.lower():
            return jsonify(repo)
    return jsonify({"error": "Projeto não encontrado"}), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
