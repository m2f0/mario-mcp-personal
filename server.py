import os
from flask import Flask, jsonify, request
import json
from flask_cors import CORS
from flask import render_template
import psutil
import platform
import time
import requests
from datetime import datetime

app = Flask(__name__)
CORS(app)

START_TIME = time.time()

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

@app.route("/")
def status_page():
    return render_template("status.html")

@app.route('/resources/linkedin', methods=['GET'])
def get_linkedin():
    return jsonify(linkedin)

@app.route('/resources/github', methods=['GET'])
def get_github():
    return jsonify(github)

@app.route('/resources/blogposts', methods=['GET'])
def get_blogposts():
    return jsonify(blog)

@app.route('/resources/blogposts_simple', methods=['GET'])
def list_blogposts_simple():
    simple_posts = [
        {
            "title": post["title"],
            "url": post["url"]
        }
        for post in blog["posts"][:5]
    ]
    return jsonify({"posts": simple_posts})

# --- NOVO ENDPOINT DE STATUS ---
def check_service_status(url):
    try:
        response = requests.get(url, timeout=5)
        return "online" if response.status_code == 200 else "offline"
    except:
        return "offline"

@app.route('/status', methods=['GET'])
def get_status():
    uptime_seconds = int(time.time() - START_TIME)
    uptime_str = time.strftime("%H:%M:%S", time.gmtime(uptime_seconds))

    def check_service_status(url):
        try:
            response = requests.get(url, timeout=5)
            return "online" if response.status_code == 200 else "offline"
        except:
            return "offline"

    base_url = "https://mcp.mariomayerle.com"

    status_info = {
        "mcp_backend": "online",
        "frontend_ui": check_service_status(base_url),
        "linkedin_scraper": check_service_status(f"{base_url}/resources/linkedin"),
        "blog_feed": check_service_status("https://hubiabrasil.com.br"),
        "api_resources": check_service_status(f"{base_url}/resources"),
        "api_github": check_service_status(f"{base_url}/resources/github"),
        "api_blogposts": check_service_status(f"{base_url}/resources/blogposts"),
        "api_project_details_example": check_service_status(f"{base_url}/tools/get_project_details?repo_name=mcp"),
        "cpu_usage": f"{psutil.cpu_percent()}%",
        "ram_usage": f"{psutil.virtual_memory().percent}%",
        "uptime": uptime_str,
        "host_os": platform.system(),
        "last_update": datetime.utcnow().isoformat() + "Z"
    }

    return jsonify(status_info)

    return jsonify(status_info)
# --- FIM DO BLOCO DE STATUS ---

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
