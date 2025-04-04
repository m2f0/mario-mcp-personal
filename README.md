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
  Informações como nome, cargo, localização, experiências, certificações, publicações, idiomas e formação acadêmica (via LinkedIn).

- **📂 Repositórios Públicos**  
  Lista atualizada dos meus projetos no GitHub.

- **📝 Publicações e Artigos**  
  Conteúdos extraídos do meu blog no HUB IA Brasil.

---

## 📁 Como consumir esta API?

A API expõe **endpoints RESTful simples, em formato JSON**, projetados para consumo direto por:

- **LLMs (Claude, GPT, Llama, etc.)**  
- **Aplicações web, bots e integrações.**
- **Usuários interessados no meu perfil público.**

### 🔗 URL Base

```
https://mcp.mariomayerle.com
```

---

## 🌐 Endpoints Disponíveis

### ➔ `GET /resources`

Retorna todos os dados públicos.

```bash
GET https://mcp.mariomayerle.com/resources
```

### ➔ `GET /resources/linkedin`

Retorna somente os dados do LinkedIn.

```bash
GET https://mcp.mariomayerle.com/resources/linkedin
```

### ➔ `GET /resources/github`

Retorna somente os repositórios públicos do GitHub.

```bash
GET https://mcp.mariomayerle.com/resources/github
```

### ➔ `GET /resources/blogposts`

Retorna somente as publicações do blog.

```bash
GET https://mcp.mariomayerle.com/resources/blogposts
```

### ➔ `GET /tools/get_project_details?repo_name={nome}`

Consulta detalhes de um repositório específico.

```bash
GET https://mcp.mariomayerle.com/tools/get_project_details?repo_name=mario-mcp-personal
```

---

## 🧐 Integração com LLMs

### Exemplo de uso:

> "Use o endpoint `https://mcp.mariomayerle.com/resources/linkedin` para retornar todas as certificações listadas no perfil de Mario Mayerle."

### Exemplo de Manifesto (ChatGPT Plugin):

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

Esta API é **pública** e **não requer autenticação**.

---

## 📢 Limites

Sem limites atuais, contanto que o uso seja feito com responsabilidade.

---

## 🗕️ Roadmap Futuro

- Integração com Medium, Twitter e APIs externas.
- Busca personalizada por tópicos (em construção).
- Endpoint para resumo automático de perfil (LLM Ready).

---

## 📄 Política de Privacidade e Uso

[Leia aqui](https://mcp.mariomayerle.com/legal) os termos de privacidade e responsabilidade sobre o uso público da API.

---

# 🌐 Mario Personal MCP API

Welcome to **Mario Personal MCP (Model Context Protocol)**!  
This is a standardized public server exposing my open professional data — ideal for integration with applications, automations, and LLMs seeking structured information.

Now available at:

```
https://mcp.mariomayerle.com
```

---

## 🚀 What does this API offer?

- **📄 Public Professional Profile**  
  Information such as name, job title, location, experiences, certifications, publications, languages, and education (via LinkedIn).

- **📂 Public GitHub Repositories**  
  Updated list of my GitHub projects.

- **📝 Blogposts and Articles**  
  Content extracted from my blog on HUB IA Brasil.

---

## 📁 How to use this API?

The API exposes **simple RESTful endpoints in JSON format**, designed for direct consumption by:

- **LLMs (Claude, GPT, Llama, etc.)**  
- **Web apps, bots, and integrations.**
- **Users interested in my public profile.**

### 🔗 Base URL

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

### ➔ `GET /resources/linkedin`

Returns only LinkedIn data.

```bash
GET https://mcp.mariomayerle.com/resources/linkedin
```

### ➔ `GET /resources/github`

Returns only public GitHub repositories.

```bash
GET https://mcp.mariomayerle.com/resources/github
```

### ➔ `GET /resources/blogposts`

Returns only blog publications.

```bash
GET https://mcp.mariomayerle.com/resources/blogposts
```

### ➔ `GET /tools/get_project_details?repo_name={name}`

Query detailed information about a specific repository.

```bash
GET https://mcp.mariomayerle.com/tools/get_project_details?repo_name=mario-mcp-personal
```

---

## 🧐 LLM Integration

### Example usage:

> "Use the endpoint `https://mcp.mariomayerle.com/resources/linkedin` to return all certifications listed in Mario Mayerle's profile."

### Plugin Example (ChatGPT Manifest):

```json
{
  "schema_version": "v1",
  "name_for_human": "Mario MCP API",
  "name_for_model": "mario_mcp",
  "description_for_human": "Fetch public profile data from Mario Mayerle (LinkedIn, GitHub, Blogposts).",
  "description_for_model": "Allows access to Mario Mayerle's public profile, including LinkedIn, GitHub repositories, and blog posts.",
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

## 📊 Usage Examples

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

This API is **public** and **requires no authentication**.

---

## 📢 Rate Limits

No rate limits currently, as long as usage is responsible.

---

## 🗕️ Future Roadmap

- Integration with Medium, Twitter, and external APIs.
- Topic-based custom search (under development).
- Endpoint for automatic profile summarization (LLM Ready).

---

## 📄 Privacy Policy and Terms

[Click here](https://mcp.mariomayerle.com/legal) to read the privacy and usage terms for this public API.

---

