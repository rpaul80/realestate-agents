import requests

from state import AgentState


def fetch_url(state: AgentState):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    url = state.get("listing_url").listing_detail_url
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return {"html_content": response.content}
