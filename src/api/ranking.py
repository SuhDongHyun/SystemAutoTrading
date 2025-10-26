from src.http import api_get
from src.model.ranking import HtsTopViewBody

# --- 3) HTS 조회 상위 20종목 ---
def get_hts_top_view() -> HtsTopViewBody:
    path = "uapi/domestic-stock/v1/ranking/hts-top-view"
    resp = api_get(
        path=path,
        tr_id='HHMCM000100C0'
    )
    return HtsTopViewBody.model_validate(resp.json())
