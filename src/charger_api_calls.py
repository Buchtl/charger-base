import requests
from urllib.parse import urljoin
from src.charger_models import StatusPoll


api_base = "http://go-echarger/api/status"
api_status = urljoin(api_base, "status")


def status_polling() -> StatusPoll:
    response = requests.get(f"{api_status}?filter=err,eto,tma").json()
    return StatusPoll(**response)
