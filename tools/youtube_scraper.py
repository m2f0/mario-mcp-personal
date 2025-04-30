import requests
import re
import json

def buscar_videos_do_canal(url_canal, max_videos=10):
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    try:
        response = requests.get(url_canal, headers=headers, timeout=10)
        response.raise_for_status()
    except Exception as e:
        return {"error": f"Erro ao acessar o canal: {str(e)}"}

    html = response.text

    # Extrai o JSON que está embutido na página
    match = re.search(r"var ytInitialData = ({.*?});</script>", html)
    if not match:
        return {"error": "Não foi possível extrair os dados iniciais (ytInitialData)"}

    try:
        yt_data = json.loads(match.group(1))

        # Busca a aba que contém gridRenderer (vídeos)
        tabs = yt_data["contents"]["twoColumnBrowseResultsRenderer"]["tabs"]
        grid_items = None

        for tab in tabs:
            tab_renderer = tab.get("tabRenderer")
            if not tab_renderer:
                continue

            # Verifica se tem gridRenderer dentro da estrutura
            try:
                grid_items = tab_renderer["content"]["richGridRenderer"]["contents"]
                break
            except KeyError:
                continue

        if not grid_items:
            return {"error": "Não foi possível encontrar a seção de vídeos (richGridRenderer)"}

        # Extrair os vídeos válidos
        videos = []
        for item in grid_items:
            video_data = item.get("richItemRenderer", {}).get("content", {}).get("videoRenderer")
            if not video_data:
                continue

            video_id = video_data.get("videoId")
            title = video_data.get("title", {}).get("runs", [{}])[0].get("text", "")
            thumb = video_data.get("thumbnail", {}).get("thumbnails", [{}])[-1].get("url", "")

            videos.append({
                "title": title,
                "url": f"https://www.youtube.com/watch?v={video_id}",
                "thumbnail": thumb
            })

            if len(videos) >= max_videos:
                break

        return videos

    except Exception as e:
        return {"error": f"Erro ao processar estrutura da página: {str(e)}"}
