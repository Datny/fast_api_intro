import json
from pathlib import Path

import fastapi
import uvicorn
from starlette.staticfiles import StaticFiles

from api import weather_api
from services import openweather_service
from views import home

api = fastapi.FastAPI()


def configure():
    configure_routing()
    configure_apikeys()

def configure_apikeys():
    file = Path('settings.json').absolute()
    if file.exists() is False:
        print(f"WARNING: {file} not found u cannot continute. please see settings_template.json")
        raise Exception("settings.json not found, please see settings_template.json")

    with open('settings.json') as fin:
        settings = json.load(fin)
        openweather_service.api_key = settings.get('api_key')

def configure_routing():
    api.mount('/static', StaticFiles(directory='static'), name='static')
    api.include_router(home.router)
    api.include_router(weather_api.router)

if __name__ == '__main__':
    configure()
    uvicorn.run("main:api", port=8000, host="127.0.0.1", reload=True)
else:
    configure()
