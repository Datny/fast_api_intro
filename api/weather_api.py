from typing import Optional, List

from fastapi import Depends
import fastapi


from models.location import Location
from models.reports import Report, ReportSubmittal
from models.validation_error import ValidationError
from services import openweather_service, report_service

router = fastapi.APIRouter()


@router.get('/api/weather/{city}')
async def weather(loc: Location = Depends(), units: Optional[str] = 'metric'):
    try:
        return await openweather_service.get_report(loc.city, loc.state, loc.country, units)
    except ValidationError as ve:
        return fastapi.Response(content=ve.error_msg, status_code=ve.status_code)
    except Exception as x:
        print(f"Server crashed while processing request {x}")
        return fastapi.Response(content="Error processing your request.", status_code=500)


@router.get('/api/reports', name='all_reports', response_model=List[Report])
async def reports_get() -> List[Report]:
    return await report_service.get_reports()


@router.post('/api/reports', name='add_report', status_code=201, response_model=Report)
async def report_post(report_submit: ReportSubmittal) -> Report:
    description = report_submit.description
    location = report_submit.location
    return await report_service.add_report(description, location)