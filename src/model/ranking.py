from src.model import *

@dataclass
class HtsTopViewOutput1():
    mrkt_div_cls_code: str    #시장구분
    mksc_shrn_iscd: str    #종목코드

@dataclass
class HtsTopViewBody(BaseModel):
    rt_cd: str    #성공 실패 여부
    msg_cd: str    #응답코드
    msg1: str    #응답메세지
    output1: List[HtsTopViewOutput1]    #응답상세

@dataclass
class FluctuationOutput:
    stck_shrn_iscd: str    #주식 단축 종목코드
    data_rank: str    #데이터 순위
    hts_kor_isnm: str    #HTS 한글 종목명
    stck_prpr: str    #주식 현재가
    prdy_vrss: str    #전일 대비
    prdy_vrss_sign: str    #전일 대비 부호
    prdy_ctrt: str    #전일 대비율
    acml_vol: str    #누적 거래량
    stck_hgpr: str    #주식 최고가
    hgpr_hour: str    #최고가 시간
    acml_hgpr_date: str    #누적 최고가 일자
    stck_lwpr: str    #주식 최저가
    lwpr_hour: str    #최저가 시간
    acml_lwpr_date: str    #누적 최저가 일자
    lwpr_vrss_prpr_rate: str    #최저가 대비 현재가 비율
    dsgt_date_clpr_vrss_prpr_rate: str    #지정 일자 종가 대비 현재가 비
    cnnt_ascn_dynu: str    #연속 상승 일수
    hgpr_vrss_prpr_rate: str    #최고가 대비 현재가 비율
    cnnt_down_dynu: str    #연속 하락 일수
    oprc_vrss_prpr_sign: str    #시가2 대비 현재가 부호
    oprc_vrss_prpr: str    #시가2 대비 현재가
    oprc_vrss_prpr_rate: str    #시가2 대비 현재가 비율
    prd_rsfl: str    #기간 등락
    prd_rsfl_rate: str    #기간 등락 비율

@dataclass
class FluctuationBody(BaseModel):
    rt_cd: str    #성공 실패 여부
    msg_cd: str    #응답코드
    msg1: str    #응답메세지
    output: List[FluctuationOutput]    #응답상세

@dataclass
class VolumeRankOutput:
    hts_kor_isnm: str    #HTS 한글 종목명
    mksc_shrn_iscd: str    #유가증권 단축 종목코드
    data_rank: str    #데이터 순위
    stck_prpr: str    #주식 현재가
    prdy_vrss_sign: str    #전일 대비 부호
    prdy_vrss: str    #전일 대비
    prdy_ctrt: str    #전일 대비율
    acml_vol: str    #누적 거래량
    prdy_vol: str    #전일 거래량
    lstn_stcn: str    #상장 주수
    avrg_vol: str    #평균 거래량
    n_befr_clpr_vrss_prpr_rate: str    #N일전종가대비현재가대비율
    vol_inrt: str    #거래량증가율
    vol_tnrt: str    #거래량 회전율
    nday_vol_tnrt: str    #N일 거래량 회전율
    avrg_tr_pbmn: str    #평균 거래 대금
    tr_pbmn_tnrt: str    #거래대금회전율
    nday_tr_pbmn_tnrt: str    #N일 거래대금 회전율
    acml_tr_pbmn: str    #누적 거래 대금

@dataclass
class VolumeRankBody(BaseModel):
    rt_cd: str    #성공 실패 여부
    msg_cd: str    #응답코드
    msg1: str    #응답메세지
    output: List[VolumeRankOutput]    #응답상세
