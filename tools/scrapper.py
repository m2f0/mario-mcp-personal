import pdfplumber
import json
import re

# Caminho do PDF exportado
document_path = "../resources/linkedin_profile.pdf"

# Variável para armazenar texto extraído
extracted_text = ""

# Extração do texto
def extract_text_from_pdf(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text

# Extração
print("\nExtraindo dados do PDF...\n")
extracted_text = extract_text_from_pdf(document_path)

# Debug: salva todo o texto extraído para referência
with open("../resources/full_linkedin_text.txt", "w", encoding="utf-8") as f:
    f.write(extracted_text)

# Divide em linhas
lines = extracted_text.split("\n")

# Inicializa JSON
linkedin_profile = {
    "profile": {
        "name": "",
        "title": "",
        "location": "",
        "experience": [],
        "certifications": [],
        "publications": [],
        "education": [],
        "skills": [],
        "languages": []
    }
}

# Flags auxiliares
current_section = None

# Palavras-chave para identificar seções
section_keywords = {
    "experience": ["Experiência", "Experience"],
    "certifications": ["Certifications", "Certificações"],
    "publications": ["Publications", "Publicações"],
    "education": ["Education", "Formação Acadêmica", "Educação"],
    "skills": ["Skills", "Competências"],
    "languages": ["Languages", "Idiomas"]
}

# Loop principal para capturar seções
for idx, line in enumerate(lines):
    clean_line = line.strip()

    # Nome e título
    if idx == 0:
        linkedin_profile["profile"]["name"] = clean_line
    elif idx == 1:
        linkedin_profile["profile"]["title"] = clean_line

    # Localização
    if any(keyword in clean_line for keyword in ["Brasil", "Sao Paulo", "São Paulo"]) and linkedin_profile["profile"]["location"] == "":
        linkedin_profile["profile"]["location"] = clean_line

    # Detecta início de seções
    for section, keywords in section_keywords.items():
        if any(keyword.lower() in clean_line.lower() for keyword in keywords):
            current_section = section
            break
    else:
        # Seção não identificada
        if clean_line in ["", "Page"]:
            continue
        
        if current_section:
            # Evitar capturar headers ou rodapés
            if clean_line.startswith("Page"):
                continue
            linkedin_profile["profile"][current_section].append(clean_line)

# Salva no JSON final
with open("../resources/linkedin.json", "w", encoding="utf-8") as f:
    json.dump(linkedin_profile, f, indent=4)

print("\n✅ Dados extraídos e salvos em 'resources/linkedin.json' com sucesso!")
