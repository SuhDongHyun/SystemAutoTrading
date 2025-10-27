from src.http import api_get
from src.model.quote import InquirePrice2Body

def get_price_v2(mrkt: str = 'J', code: str = '005930'):
    path = 'uapi/domestic-stock/v1/quotations/inquire-price-2'
    params = {
        'FID_COND_MRKT_DIV_CODE': mrkt,
        'FID_INPUT_ISCD': code
    }
    resp = api_get(
        path=path,
        params=params,
        tr_id='FHPST01010000'
    )
    return InquirePrice2Body.model_validate(resp.json())
