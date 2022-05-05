import requests

from commands import ElementEvent, SetXMICommand


BASE_URL = "http://localhost:8080/monitor"


def send_event(event: ElementEvent):
    resp = requests.post(f"{BASE_URL}/event", json=event.to_dict())
    print(resp.text)


def send_model(model_data: SetXMICommand):
    resp = requests.post(f"{BASE_URL}/set_model", json=model_data.to_dict())
    print(resp.text)
