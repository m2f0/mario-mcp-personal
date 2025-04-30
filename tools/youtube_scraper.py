import requests
import re
import json
from bs4 import BeautifulSoup

def buscar_videos_do_canal(url_canal, max_videos=10):
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    response = requests.get(url_canal, headers=headers)
    html = response.text

    # Extrai o JSON que está embutido na página
    match = re.search(r'var ytInitialData = ({.*?});</script>', html)
    if not match:
        return {"error": "Não foi possível extrair os dados iniciais do YouTube"}

    yt_data = json.loads(match.group(1))
    
    try:
        videos = []
        items = yt_data["contents"]["twoColumnBrowseResultsRenderer"]["tabs"][1]["tabRenderer"]["content"] \
            ["sectionListRenderer"]["contents"][0]["itemSectionRenderer"]["contents"][0] \
            ["gridRenderer"]["items"]

        for item in items[:max_videos]:
            video = item.get("gridVideoRenderer")
            if not video:
                continue

            video_id = video["videoId"]
            title = video["title"]["runs"][0]["text"]
            thumb = video["thumbnail"]["thumbnails"][-1]["url"]

            videos.append({
                "title": title,
                "url": f"https://www.youtube.com/watch?v={video_id}",
                "thumbnail": thumb
            })

        return videos

    except Exception as e:
        return {"error": f"Erro ao processar estrutura do YouTube: {str(e)}"}
