import os
import json
from pydantic import BaseModel
from mcp import Tool

# Diretórios
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
STATIC_DIR = os.path.join(BASE_DIR, "static", "imagens")
METADATA_FILE = os.path.join(BASE_DIR, "data", "imagens_metadata.json")

# Schemas
class MarioImagesInput(BaseModel):
    pass

class MarioImageItem(BaseModel):
    filename: str
    descricao: str
    url: str

class MarioImagesOutput(BaseModel):
    imagens: list[MarioImageItem]

# Função da Tool
def mario_images_tool_run(_: MarioImagesInput) -> MarioImagesOutput:
    with open(METADATA_FILE, "r", encoding="utf-8") as f:
        imagens_metadata = json.load(f)

    for imagem in imagens_metadata:
        imagem["url"] = f"https://mcp.mariomayerle.com/imagens/{imagem['filename']}"

    imagens = [MarioImageItem(**imagem) for imagem in imagens_metadata]
    return MarioImagesOutput(imagens=imagens)

# Tool registrada com camelCase explícito
mario_images_tool = Tool(**{
    "name": "mario_images",
    "description": "Retorna imagens públicas de Mario Mayerle com descrição e URL",
    "inputSchema": MarioImagesInput,
    "outputSchema": MarioImagesOutput,
    "run": mario_images_tool_run
})
