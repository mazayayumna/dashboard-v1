from fastapi import APIRouter, HTTPException

from services.who_services import (
    WHOService,
    WHO_GHO_INDICATORS
)
router = APIRouter()

# based on api url
@router.get("/fetch-id-indicators")
def fetch_id_indicators(disease: str, year: int):
    disease = disease.lower()
    if disease not in WHO_GHO_INDICATORS:
        raise HTTPException(status_code=400,
                            details='Disease not supported')

    results = []
    for indicator in WHO_GHO_INDICATORS[disease]:
        data = WHOService().fetch_statistics(indicator, year)
        results.append({
            "indicator": indicator,
            "data": data,
        })