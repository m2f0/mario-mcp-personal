import os
import json
from mcp import Tool

# Caminhos
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
STATIC_DIR = os.path.join(BASE_DIR, "static", "imagens")
METADATA_FILE = os.path.join(BASE_DIR, "data", "imagens_metadata.json")

# Função da tool
def mario_images_tool_run(_: dict) -> dict:
    with open(METADATA_FILE, "r", encoding="utf-8") as f:
        imagens_metadata = json.load(f)

    for imagem in imagens_metadata:
        imagem["url"] = f"https://mcp.mariomayerle.com/imagens/{imagem['filename']}"

    return {"imagens": imagens_metadata}

# Schema direto (dict)
input_schema = {
    "type": "object",
    "properties": {}
}

output_schema = {
    "type": "object",
    "properties": {
        "imagens": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "filename": {"type": "string"},
                    "descricao": {"type": "string"},
                    "url": {"type": "string"}
                },
                "required": ["filename", "descricao", "url"]
            }
        }
    },
    "required": ["imagens"]
}

# Registro final da Tool
mario_images_tool = Tool(
    name="mario_images",
    description="Retorna imagens públicas de Mario Mayerle com descrição e URL",
    inputSchema=input_schema,
    outputSchema=output_schema,
    run=mario_images_tool_run
)
