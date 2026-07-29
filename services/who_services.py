import requests

BASE_URL = "https://ghoapi.azureedge.net/api"

WHO_INDICATORS = [
    "TB_c_notified", #Total number of notified TB cases
    "TB_e_inc_tbhiv_num", #Number of incident tuberculosis cases,  (HIV-positive cases)
    "MALARIA_CONF_CASES", #Number of confirmed malaria cases
    "HIV_0000000001", #Estimated number of people (all ages) living with HIV
    "WHS3_62" #Measles - number of reported cases
]

class WHOService:
    def get_indicators(self):
        response = requests.get(
            f"{BASE_URL}/Indicator"
        )
        response.raise_for_status()
        return response.json()["value"]

    def fetch_statistics(self):
        results = []

        for indicator in WHO_INDICATORS:
            url = (
                f"{BASE_URL}/{indicator}"
                "?$filter=SpatialDim eq 'IDN'"
                )

        response = requests.get(url)
        response.raise_for_status()
        data = response.json()["value"]
        results.extend(data)
        return results