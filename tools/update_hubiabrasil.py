import feedparser
import json
import os

# Configurações
RSS_FEED_URL = "https://hubiabrasil.substack.com/feed"
OUTPUT_PATH = os.path.join("resources", "blogposts.json")

# Extrair dados do feed
print("🔄 Buscando posts do Substack...")
feed = feedparser.parse(RSS_FEED_URL)

posts = []
for entry in feed.entries:
    post = {
        "title": entry.title,
        "description": entry.description if 'description' in entry else "",
        "url": entry.link,
        "published": entry.published if 'published' in entry else "",
        "author": entry.author if 'author' in entry else "",
        "image": entry.enclosures[0].href if 'enclosures' in entry and entry.enclosures else "",
        "content": entry.content[0].value if 'content' in entry else ""
    }
    posts.append(post)

# Atualizar arquivo JSON
output_data = {"posts": posts}

with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
    json.dump(output_data, f, indent=4, ensure_ascii=False)

print(f"✅ Blogposts atualizados com sucesso em '{OUTPUT_PATH}'!")
