import requests

BASE_URL = "https://ghoapi.azureedge.net/api"

WHO_GHO_INDICATORS = {
    "tb": [
        "TB_c_notified", #Total number of notified TB cases
        "TB_e_inc_tbhiv_num", #Number of incident tuberculosis cases,  (HIV-positive cases)
    ],
    "malaria": [
        "MALARIA_CONF_CASES", #Number of confirmed malaria cases
    ],
    "hiv": [
        "HIV_0000000001", #Estimated number of people (all ages) living with HIV
    ],
    "measles": [
        "WHS3_62" #Measles - number of reported cases
    ]
}

class WHOService:
    def get_indicators(self):
        params = {
            "$filter": (
                f"IndicatorCode eq '{indicator_code}'"
                f"and SpatialDim"
            )
        }
        response = requests.get(
            f"{BASE_URL}/Indicator"
        )
        response.raise_for_status()
        return response.json()["value"]

    def fetch_statistics(self, indicator_code: str, year: int):
        params = {
                    "$filter": (
                        f"IndicatorCode eq '{indicator_code}'"
                        f"and SpatialDim eq 'IDN'"
                        f"and TimeDim eq {year}"
                    )
                }
        """results = []

        for indicator in WHO_GHO_INDICATORS:
            url = (
                f"{BASE_URL}/{indicator}"
                "?$filter=SpatialDim eq 'IDN'"
                )"""

        response = requests.get(BASE_URL, params=params, timeout=30)
        response.raise_for_status()
        #data = response.json()["value"]
        #results.extend(data)
        return response.json()["value"]