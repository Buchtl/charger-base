import requests
from urllib.parse import urljoin
from src.charger_models import StatusPoll, Cdi


api_base = "http://go-echarger/api/status"
api_status = urljoin(api_base, "status")


def status_err() -> int:
    response = requests.get(f"{api_status}?filter=err").json()["err"]
    return int(response)


def status_energy_total_wh() -> int:
    response = requests.get(f"{api_status}?filter=eto").json()["eto"]
    return int(response)


def status_polling() -> StatusPoll:
    response = requests.get(f"{api_status}?filter=err,eto,tma").json()
    return StatusPoll(**response)
