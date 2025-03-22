import requests
import json
import urllib.parse

# ---------------------------
# CONFIGURAÇÕES
client_id = "77a66s5kvj40at"
client_secret = "WPL_AP1.KJjauxCqS8X6D5qW.PTTqOg=="
redirect_uri = "https://localhost:8000/linkedin/callback"

# ---------------------------

# Passo 1: Gerar URL de autorização
def generate_auth_url():
    base_url = "https://www.linkedin.com/oauth/v2/authorization"
    params = {
        "response_type": "code",
        "client_id": client_id,
        "redirect_uri": redirect_uri,
        "scope": "openid profile email",
        "state": "MarioMCP123",
        "prompt": "consent"
    }
    url = f"{base_url}?{urllib.parse.urlencode(params)}"
    print(f"\n1️⃣  Abra no navegador e faça login para autorizar:\n\n{url}\n")
    print("Após autorizar, copie o código 'code=' da URL redirecionada e cole abaixo.\n")

# Passo 2: Trocar code por Access Token
def exchange_code_for_token(auth_code):
    token_url = "https://www.linkedin.com/oauth/v2/accessToken"
    data = {
        "grant_type": "authorization_code",
        "code": auth_code,
        "redirect_uri": redirect_uri,
        "client_id": client_id,
        "client_secret": client_secret
    }
    response = requests.post(token_url, data=data)

    if response.status_code != 200:
        print("\n❌ Erro ao obter token:")
        print(response.status_code, response.text)
        exit(1)

    token_data = response.json()
    print("\n✅ Token obtido com sucesso!")
    return token_data['access_token']

# Passo 3: Buscar dados do perfil e email
def fetch_profile(access_token):
    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    # Dados básicos
    profile_response = requests.get("https://api.linkedin.com/v2/me", headers=headers)
    profile_data = profile_response.json()

    print("\n🔍 Dados do perfil bruto:\n")
    print(json.dumps(profile_data, indent=4))

    linkedin_profile = {
        "profile": {
            "name": f"{profile_data.get('localizedFirstName', '')} {profile_data.get('localizedLastName', '')}",
            "title": profile_data.get('headline', ''),
            "location": "Brasil"
        }
    }

    # Email opcional
    email_response = requests.get(
        "https://api.linkedin.com/v2/emailAddress?q=members&projection=(elements*(handle~))",
        headers=headers
    )
    email_data = email_response.json()

    print("\n🔍 Retorno do email:\n")
    print(json.dumps(email_data, indent=4))

    try:
        email = email_data['elements'][0]['handle~']['emailAddress']
        linkedin_profile["profile"]["email"] = email
    except (KeyError, IndexError):
        print("⚠️  Email não disponível ou permissão não habilitada.")
        linkedin_profile["profile"]["email"] = "Não disponível"

    with open('../resources/linkedin.json', 'w', encoding='utf-8') as f:
        json.dump(linkedin_profile, f, indent=4)

    print("\n✅ Perfil salvo no arquivo 'resources/linkedin.json' com sucesso!")

# -------------------------
# Execução
generate_auth_url()

# Entrada manual do code
auth_code = input("Cole aqui o 'code' retornado pelo LinkedIn: ").strip()

access_token = exchange_code_for_token(auth_code)

fetch_profile(access_token)
