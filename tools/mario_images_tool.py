import os
import json

STATIC_DIR = os.path.join(os.path.dirname(__file__), "..", "static", "imagens")
METADATA_FILE = os.path.join(os.path.dirname(__file__), "..", "data", "imagens_metadata.json")

def carregar_metadata():
    with open(METADATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def mario_images_tool_run(_):
    imagens = carregar_metadata()
    for img in imagens:
        img["url"] = f"https://mcp.mariomayerle.com/imagens/{img['filename']}"
    return {"imagens": imagens}

# Tool MCP para registro no SDK
from mcp import Tool

mario_images_tool = Tool(
    name="mario_images",
    description="Retorna imagens do Mario Mayerle com descrição e link público",
    input_schema=None,
    output_schema={"imagens": "Lista com descrição e URL"},
    run=mario_images_tool_run
)
