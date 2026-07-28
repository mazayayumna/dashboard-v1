import requests

BASE_URL = "https://ghoapi.azureedge.net/api"

class WHOService:
    def get_indicator(self):
        response = requests.get(
            f"{BASE_URL}/Indicator"
        )
        response.raise_for_status()
        return response.json()["value"]