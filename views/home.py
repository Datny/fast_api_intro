import fastapi
from starlette.requests import Request
from starlette.templating import Jinja2Templates

from services import report_service

router = fastapi.APIRouter()
templates = Jinja2Templates(directory='templates')


@router.get('/', include_in_schema=False)
async def index(request: Request):
    events = await report_service.get_reports()
    data = {'request': request, 'events': events}
    return templates.TemplateResponse('home/index.html', data)


@router.get('/favicon.ico', include_in_schema=False)
def favicon():
    return fastapi.responses.FileResponse('static/img')