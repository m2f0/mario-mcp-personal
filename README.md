# 🌐 Mario Personal MCP API

Bem-vindo ao **Mario Personal MCP (Model Context Protocol)**!
Aqui você encontrará um servidor padronizado, exposto publicamente, contendo meus dados profissionais abertos — ideal para integração com aplicações, automações e LLMs que desejem consumir essas informações de forma estruturada.

Agora disponível em:

```
https://mcp.mariomayerle.com
```

---

## 🚀 O que esta API oferece?

- **📄 Perfil Profissional Público**  
  Informações completas como nome, cargo, localização, experiências, certificações, publicações, idiomas e formação acadêmica (via LinkedIn).
  
- **📂 Repositórios Públicos**  
  Lista atualizada dos meus projetos no GitHub.

- **📝 Publicações e Artigos**  
  Posts e materiais relevantes do meu blog.

---

## 📁 Como consumir esta API?

A API expõe **endpoints RESTful simples, em formato JSON**, projetados para consumo direto por:

- **LLMs (Claude, GPT, Llama, etc.)** que desejem buscar informações atualizadas.
- **Aplicações web, bots e integrações.**
- **Pessoas interessadas no perfil público.**

### 🔗 URL Base de Consumo

```
https://mcp.mariomayerle.com
```

---

## 🌐 Endpoints Disponíveis

### ➔ `GET /resources`

**Retorna todos os dados públicos.**

```bash
GET https://mcp.mariomayerle.com/resources
```

---

### ➔ `GET /resources/linkedin`

**Retorna somente dados do LinkedIn.**

```bash
GET https://mcp.mariomayerle.com/resources/linkedin
```

---

### ➔ `GET /resources/github`

**Retorna somente dados do GitHub.**

```bash
GET https://mcp.mariomayerle.com/resources/github
```

---

### ➔ `GET /resources/blogposts`

**Retorna somente publicações do blog.**

```bash
GET https://mcp.mariomayerle.com/resources/blogposts
```

---

### ➔ `GET /tools/get_project_details?repo_name={nome}`

**Consulta detalhada de um repositório específico.**

```bash
GET https://mcp.mariomayerle.com/tools/get_project_details?repo_name=mario-mcp-personal
```

---

## 🤖 Integração com LLMs

Para integração com LLMs como ChatGPT ou Claude:

### Exemplo de instrução:

> "Use o endpoint `https://mcp.mariomayerle.com/resources/linkedin` e retorne todas as certificações listadas no perfil do Mario."

### Exemplo Plugin (ChatGPT Manifest)

```json
{
  "schema_version": "v1",
  "name_for_human": "Mario MCP API",
  "name_for_model": "mario_mcp",
  "description_for_human": "Consulta dados públicos do Mario Mayerle (LinkedIn, GitHub, Blogposts).",
  "description_for_model": "Permite acessar informações públicas do perfil de Mario Mayerle, incluindo LinkedIn, repositórios GitHub e publicações.",
  "auth": {
    "type": "none"
  },
  "api": {
    "type": "openapi",
    "url": "https://mcp.mariomayerle.com/.well-known/openapi.yaml"
  },
  "logo_url": "https://mcp.mariomayerle.com/logo.png",
  "contact_email": "contato@mariomayerle.com",
  "legal_info_url": "https://mcp.mariomayerle.com/legal"
}
```

---

## 📊 Exemplos de Consumo

### Python:

```python
import requests

response = requests.get("https://mcp.mariomayerle.com/resources/linkedin")
data = response.json()
print(data["profile"]["certifications"])
```

### JavaScript:

```javascript
fetch('https://mcp.mariomayerle.com/resources/linkedin')
  .then(response => response.json())
  .then(data => console.log(data.profile.certifications));
```

---

## 🔐 Autorização

Esta API é **pública e não requer autenticação**.

---

## 📢 Limites

Requisições ilimitadas por enquanto, desde que usadas com boas práticas.

---

## 📅 Roadmap Futuro

- Integração com APIs de Medium, Twitter e LinkedIn.
- Novas ferramentas para busca personalizada.
- Integração nativa com LLMs.

---

## 📄 Política de Privacidade e Uso

Leia os termos completos de privacidade e responsabilidade de uso aqui:

[Política de Privacidade e Uso](https://mcp.mariomayerle.com/legal)

---

# 🌐 Mario Personal MCP API (English)

Welcome to **Mario Personal MCP (Model Context Protocol)**!
This is a public server exposing my open professional data — ideal for integration with applications, automations, and LLMs seeking structured access.

Now available at:

```
https://mcp.mariomayerle.com
```

---

## 🚀 What does this API provide?

- **📄 Public Professional Profile**  
  Complete info such as name, job title, location, experience, certifications, publications, languages and education (via LinkedIn).
  
- **📂 Public GitHub Repositories**  
  Updated list of public projects.

- **📝 Blogposts and Articles**  
  Relevant content from my blog.

---

## 📁 How to Consume

The API exposes **simple RESTful endpoints in JSON format**, designed for:

- **LLMs (Claude, GPT, Llama, etc.)** seeking updated info.
- **Web apps, bots, integrations.**
- **Anyone interested in public data.**

### 🔗 Base URL for Consumption

```
https://mcp.mariomayerle.com
```

---

## 🌐 Available Endpoints

### ➔ `GET /resources`

Returns all public data.

```bash
GET https://mcp.mariomayerle.com/resources
```

---

### ➔ `GET /resources/linkedin`

Returns only LinkedIn profile data.

```bash
GET https://mcp.mariomayerle.com/resources/linkedin
```

---

### ➔ `GET /resources/github`

Returns only GitHub repositories.

```bash
GET https://mcp.mariomayerle.com/resources/github
```

---

### ➔ `GET /resources/blogposts`

Returns only blog publications.

```bash
GET https://mcp.mariomayerle.com/resources/blogposts
```

---

### ➔ `GET /tools/get_project_details?repo_name={name}`

Query details of a specific repository.

```bash
GET https://mcp.mariomayerle.com/tools/get_project_details?repo_name=mario-mcp-personal
```

---

## 🤖 LLM Integration

Example instruction:

> "Use `https://mcp.mariomayerle.com/resources/linkedin` endpoint and return all certifications listed in Mario's profile."

### Example Plugin (ChatGPT Manifest)

```json
{
  "schema_version": "v1",
  "name_for_human": "Mario MCP API",
  "name_for_model": "mario_mcp",
  "description_for_human": "Fetch Mario Mayerle's public profile data (LinkedIn, GitHub, Blog).",
  "description_for_model": "Allows access to Mario Mayerle's public professional profile, including LinkedIn, GitHub repositories and blog publications.",
  "auth": {
    "type": "none"
  },
  "api": {
    "type": "openapi",
    "url": "https://mcp.mariomayerle.com/.well-known/openapi.yaml"
  },
  "logo_url": "https://mcp.mariomayerle.com/logo.png",
  "contact_email": "contato@mariomayerle.com",
  "legal_info_url": "https://mcp.mariomayerle.com/legal"
}
```

---

## 📊 Consumption Examples

### Python:

```python
import requests

response = requests.get("https://mcp.mariomayerle.com/resources/linkedin")
data = response.json()
print(data["profile"]["certifications"])
```

### JavaScript:

```javascript
fetch('https://mcp.mariomayerle.com/resources/linkedin')
  .then(response => response.json())
  .then(data => console.log(data.profile.certifications));
```

---

## 🔐 Authorization

This API is **public and requires no authentication**.

---

## 📢 Limits

Unlimited requests for now, assuming responsible use.

---

## 📅 Future Roadmap

- Integration with Medium, Twitter, LinkedIn APIs.
- Custom search tools.
- Native LLM integrations.

---

## 📄 Privacy Policy and Usage Terms

Read the full privacy and usage terms here:

[Privacy Policy and Terms](https://mcp.mariom
