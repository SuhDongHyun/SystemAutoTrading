from src.http import api_get
from src.model.ranking import HtsTopViewBody, FluctuationBody, VolumeRankBody

# --- HTS 조회 상위 20종목 ---
def get_hts_top_view() -> HtsTopViewBody:
    path = 'uapi/domestic-stock/v1/ranking/hts-top-view'
    resp = api_get(
        path=path,
        tr_id='HHMCM000100C0'
    )
    return HtsTopViewBody.model_validate(resp.json())

# --- 등락률 상위 30종목 ---
def get_fluctuation() -> FluctuationBody:
    path = 'uapi/domestic-stock/v1/ranking/fluctuation'
    params = {
        'fid_cond_mrkt_div_code': 'J',
        'fid_cond_scr_div_code': '20170',
        'fid_input_iscd': '0000',
        'fid_rank_sort_cls_code': '0',
        'fid_input_cnt_1': '0',
        'fid_prc_cls_code': '1',
        'fid_input_price_1': '',
        'fid_input_price_2': '',
        'fid_vol_cnt': '',
        'fid_rsfl_rate1': '',
        'fid_rsfl_rate2': '',
        'fid_trgt_cls_code': '0',
        'fid_trgt_exls_cls_code': '0',
        'fid_div_cls_code': '0'
    }
    resp = api_get(
        path=path,
        params=params,
        tr_id='FHPST01700000'
    )
    return FluctuationBody.model_validate(resp.json())

# --- 거래량 상위 30종목 ---
def get_volume_rank() -> VolumeRankBody:
    path = 'uapi/domestic-stock/v1/quotations/volume-rank'
    params = {
        'FID_COND_MRKT_DIV_CODE': 'J',
        'FID_COND_SCR_DIV_CODE': '20171',
        'FID_INPUT_ISCD': '0000',
        'FID_DIV_CLS_CODE': '0',
        'FID_BLNG_CLS_CODE': '0',
        'FID_TRGT_CLS_CODE': '111111111',
        'FID_TRGT_EXLS_CLS_CODE': '0000000000',
        'FID_INPUT_PRICE_1': '',
        'FID_INPUT_PRICE_2': '',
        'FID_VOL_CNT': '',
        'FID_INPUT_DATE_1': ''
    }
    resp = api_get(
        path=path,
        params=params,
        tr_id='FHPST01710000'
    )
    return VolumeRankBody.model_validate(resp.json())
