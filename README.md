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
  Informações como nome, cargo e localização (via LinkedIn).
  
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

**Exemplo:**

```bash
GET https://mcp.mariomayerle.com/resources
```

**Resposta:**

```json
{
  "linkedin": {
    "profile": {
      "name": "Mario",
      "title": "Especialista em IA",
      "location": "Brasil"
    }
  },
  "github": {
    "repositories": [
      {
        "name": "mario-mcp-personal",
        "url": "https://github.com/seu-usuario/mario-mcp-personal"
      }
    ]
  },
  "blogposts": {
    "posts": [
      {
        "title": "Introdução ao MCP",
        "url": "https://seublog.com/mcp-intro"
      }
    ]
  }
}
```

---

### ➔ `GET /tools/get_project_details?repo_name={nome}`

**Consulta detalhada de um repositório específico.**

**Parâmetro:**
- `repo_name` → Nome do repositório (exato).

**Exemplo:**

```bash
GET https://mcp.mariomayerle.com/tools/get_project_details?repo_name=mario-mcp-personal
```

**Resposta:**

```json
{
  "name": "mario-mcp-personal",
  "url": "https://github.com/seu-usuario/mario-mcp-personal"
}
```

---

## 🤖 Integração com LLMs

1. Realize consultas HTTP GET simples para:

```
https://mcp.mariomayerle.com
```

2. Receba respostas JSON estruturadas.
3. Ideal para integração com plugins (ChatGPT Plugins, Claude Tools, etc.).

**Exemplo para um LLM:**

> "Acesse `https://mcp.mariomayerle.com/resources` e retorne os repositórios do Mario."

---

## 📊 Exemplos de Consumo

### Python:

```python
import requests

response = requests.get("https://mcp.mariomayerle.com/resources")
data = response.json()
print(data["github"]["repositories"])
```

### JavaScript:

```javascript
fetch('https://mcp.mariomayerle.com/resources')
  .then(response => response.json())
  .then(data => console.log(data.github.repositories));
```

---

## 🔐 Autorizacão

Esta API é **pública e não requer autenticação**.

---

## 📢 Limites

Requisições ilimitadas por enquanto, desde que usadas com boas práticas.

---

## 📅 Roadmap Futuro

- Integração com APIs de Medium, Twitter e LinkedIn.
- Novas ferramentas para busca personalizada.
- Integração com LLMs nativamente.

---

## 🌐 Mario Personal MCP API (English)

Welcome to **Mario Personal MCP (Model Context Protocol)**!
This is a public server exposing my open professional data — ideal for integration with applications, automations, and LLMs seeking structured access.

Now available at:

```
https://mcp.mariomayerle.com
```

---

## 🚀 What does this API provide?

- **📄 Public Professional Profile**
  Information like name, job title, and location (via LinkedIn).
  
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

**Returns all public data.**

**Example:**

```bash
GET https://mcp.mariomayerle.com/resources
```

**Response:**

```json
{
  "linkedin": {
    "profile": {
      "name": "Mario",
      "title": "Especialista em IA",
      "location": "Brasil"
    }
  },
  "github": {
    "repositories": [
      {
        "name": "mario-mcp-personal",
        "url": "https://github.com/seu-usuario/mario-mcp-personal"
      }
    ]
  },
  "blogposts": {
    "posts": [
      {
        "title": "Introdução ao MCP",
        "url": "https://seublog.com/mcp-intro"
      }
    ]
  }
}
```

---

### ➔ `GET /tools/get_project_details?repo_name={name}`

**Query details of a specific repository.**

**Parameter:**
- `repo_name` → Exact repository name.

**Example:**

```bash
GET https://mcp.mariomayerle.com/tools/get_project_details?repo_name=mario-mcp-personal
```

**Response:**

```json
{
  "name": "mario-mcp-personal",
  "url": "https://github.com/seu-usuario/mario-mcp-personal"
}
```

---

## 🤖 LLM Integration

1. Perform HTTP GET requests to:

```
https://mcp.mariomayerle.com
```

2. Receive JSON responses.
3. Ideal for integration with plugins (ChatGPT Plugins, Claude Tools, etc.).

**Example instruction for an LLM:**

> "Access `https://mcp.mariomayerle.com/resources` and return Mario's repositories."

---

## 📊 Consumption Examples

### Python:

```python
import requests

response = requests.get("https://mcp.mariomayerle.com/resources")
data = response.json()
print(data["github"]["repositories"])
```

### JavaScript:

```javascript
fetch('https://mcp.mariomayerle.com/resources')
  .then(response => response.json())
  .then(data => console.log(data.github.repositories));
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

## 📄 License

MIT License © Mario

