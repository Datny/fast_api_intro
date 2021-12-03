from typing import Optional

import requests

api_key: Optional[str] = None

def get_report(city: str, state:Optional[str], country:str, units:str) -> dict:
    if state:
        q = f"{city},{state},{country}"
    else:
        q = f"{city},{country}"
    key = api_key
    url = f"https://api.openweathermap.org/data/2.5/weather?q={q}&appid={key}?units={units}"

    resp = requests.get(url)
    resp.raise_for_status()

    data = resp.json()

    print(data)
    return data
