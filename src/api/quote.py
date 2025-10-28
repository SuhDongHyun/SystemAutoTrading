from datetime import datetime, timedelta

from src.http import api_get
from src.model.quote import InquirePrice2Body, InquireDailyItemchartpriceBody, InquireCcnlBody

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

def get_daily_itemchartprice(
        mrkt: str = 'J',
        code: str = '005930',
        start_date: datetime = datetime.now() - timedelta(weeks=4),
        end_date: datetime = datetime.now(),
        period: str = 'D'):
    if (end_date - start_date).days > 100:
        RuntimeError(f'❌ 국내주식기간별시세 조회 일자 초과')

    path = 'uapi/domestic-stock/v1/quotations/inquire-daily-itemchartprice'
    params = {
        'FID_COND_MRKT_DIV_CODE': mrkt,
        'FID_INPUT_ISCD': code,
        'FID_INPUT_DATE_1': start_date.strftime('%Y%m%d'),
        'FID_INPUT_DATE_2': end_date.strftime('%Y%m%d'),
        'FID_PERIOD_DIV_CODE': period,
        'FID_ORG_ADJ_PRC': '1'
    }
    resp = api_get(
        path=path,
        params=params,
        tr_id='FHKST03010100'
    )
    return InquireDailyItemchartpriceBody.model_validate(resp.json())

def get_ccnl(mrkt: str = 'J', code: str = '005930'):
    path = 'uapi/domestic-stock/v1/quotations/inquire-ccnl'
    params = {
        'FID_COND_MRKT_DIV_CODE': mrkt,
        'FID_INPUT_ISCD': code
    }
    resp = api_get(
        path=path,
        params=params,
        tr_id='FHKST01010300'
    )
    return InquireCcnlBody.model_validate(resp.json())
