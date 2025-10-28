from src.model import *

class InquirePrice2Output(BaseModel):
    rprs_mrkt_kor_name: str    #대표 시장 한글 명
    new_hgpr_lwpr_cls_code: Optional[str] = None   #신 고가 저가 구분 코드
    mxpr_llam_cls_code: Optional[str] = None    #상하한가 구분 코드
    crdt_able_yn: str    #신용 가능 여부
    stck_mxpr: str    #주식 상한가
    elw_pblc_yn: str    #ELW 발행 여부
    prdy_clpr_vrss_oprc_rate: str    #전일 종가 대비 시가2 비율
    crdt_rate: str    #신용 비율
    marg_rate: str    #증거금 비율
    lwpr_vrss_prpr: str    #최저가 대비 현재가
    lwpr_vrss_prpr_sign: str    #최저가 대비 현재가 부호
    prdy_clpr_vrss_lwpr_rate: str    #전일 종가 대비 최저가 비율
    stck_lwpr: str    #주식 최저가
    hgpr_vrss_prpr: str    #최고가 대비 현재가
    hgpr_vrss_prpr_sign: str    #최고가 대비 현재가 부호
    prdy_clpr_vrss_hgpr_rate: str    #전일 종가 대비 최고가 비율
    stck_hgpr: str    #주식 최고가
    oprc_vrss_prpr: str    #시가2 대비 현재가
    oprc_vrss_prpr_sign: str    #시가2 대비 현재가 부호
    mang_issu_yn: str    #관리 종목 여부
    divi_app_cls_code: str    #동시호가배분처리코드
    short_over_yn: str    #단기과열여부
    mrkt_warn_cls_code: str    #시장경고코드
    invt_caful_yn: str    #투자유의여부
    stange_runup_yn: str    #이상급등여부
    ssts_hot_yn: str    #공매도과열 여부
    low_current_yn: str    #저유동성 종목 여부
    vi_cls_code: str    #VI적용구분코드
    short_over_cls_code: str    #단기과열구분코드
    stck_llam: str    #주식 하한가
    new_lstn_cls_name: str    #신규 상장 구분 명
    vlnt_deal_cls_name: str    #임의 매매 구분 명
    flng_cls_name: Optional[str] = None    #락 구분 이름
    revl_issu_reas_name: Optional[str] = None    #재평가 종목 사유 명
    mrkt_warn_cls_name: Optional[str] = None    #시장 경고 구분 명
    stck_sdpr: str    #주식 기준가
    bstp_cls_code: str    #업종 구분 코드
    stck_prdy_clpr: str    #주식 전일 종가
    insn_pbnt_yn: str    #불성실 공시 여부
    fcam_mod_cls_name: Optional[str] = None    #액면가 변경 구분 명
    stck_prpr: str    #주식 현재가
    prdy_vrss: str    #전일 대비
    prdy_vrss_sign: str    #전일 대비 부호
    prdy_ctrt: str    #전일 대비율
    acml_tr_pbmn: str    #누적 거래 대금
    acml_vol: str    #누적 거래량
    prdy_vrss_vol_rate: str    #전일 대비 거래량 비율
    bstp_kor_isnm: str    #업종 한글 종목명
    sltr_yn: str    #정리매매 여부
    trht_yn: str    #거래정지 여부
    oprc_rang_cont_yn: str    #시가 범위 연장 여부
    vlnt_fin_cls_code: str    #임의 종료 구분 코드
    stck_oprc: str    #주식 시가2
    prdy_vol: str    #전일 거래량

class InquirePrice2Body(BaseModel):
    rt_cd: str    #성공 실패 여부
    msg_cd: str    #응답코드
    msg1: str    #응답메세지
    output: InquirePrice2Output    #응답상세

class InquireDailyItemchartpriceOutput1(BaseModel):
    prdy_vrss: str    #전일 대비
    prdy_vrss_sign: str    #전일 대비 부호
    prdy_ctrt: str    #전일 대비율
    stck_prdy_clpr: str    #주식 전일 종가
    acml_vol: str    #누적 거래량
    acml_tr_pbmn: str    #누적 거래 대금
    hts_kor_isnm: str    #HTS 한글 종목명
    stck_prpr: str    #주식 현재가
    stck_shrn_iscd: str    #주식 단축 종목코드
    prdy_vol: str    #전일 거래량
    stck_mxpr: str    #주식 상한가
    stck_llam: str    #주식 하한가
    stck_oprc: str    #주식 시가2
    stck_hgpr: str    #주식 최고가
    stck_lwpr: str    #주식 최저가
    stck_prdy_oprc: str    #주식 전일 시가
    stck_prdy_hgpr: str    #주식 전일 최고가
    stck_prdy_lwpr: str    #주식 전일 최저가
    askp: str    #매도호가
    bidp: str    #매수호가
    prdy_vrss_vol: str    #전일 대비 거래량
    vol_tnrt: str    #거래량 회전율
    stck_fcam: str    #주식 액면가
    lstn_stcn: str    #상장 주수
    cpfn: str    #자본금
    hts_avls: str    #HTS 시가총액
    per: str    #PER
    eps: str    #EPS
    pbr: str    #PBR
    itewhol_loan_rmnd_ratem: str = Field(alias='itewhol_loan_rmnd_ratem name')    #전체 융자 잔고 비율

class InquireDailyItemchartpriceOutput2(BaseModel):
    stck_bsop_date: str    #주식 영업 일자
    stck_clpr: str    #주식 종가
    stck_oprc: str    #주식 시가2
    stck_hgpr: str    #주식 최고가
    stck_lwpr: str    #주식 최저가
    acml_vol: str    #누적 거래량
    acml_tr_pbmn: str    #누적 거래 대금
    flng_cls_code: str    #락 구분 코드
    prtt_rate: str    #분할 비율
    mod_yn: str    #변경 여부
    prdy_vrss_sign: str    #전일 대비 부호
    prdy_vrss: str    #전일 대비
    revl_issu_reas: str    #재평가사유코드

class InquireDailyItemchartpriceBody(BaseModel):
    rt_cd: str    #성공 실패 여부
    msg_cd: str    #응답코드
    msg1: str    #응답메세지
    output1: InquireDailyItemchartpriceOutput1    #응답상세
    output2: List[InquireDailyItemchartpriceOutput2]    #응답상세

class InquireCcnlOutput(BaseModel):
    stck_cntg_hour: str    #주식 체결 시간
    stck_prpr: str    #주식 현재가
    prdy_vrss: str    #전일 대비
    prdy_vrss_sign: str    #전일 대비 부호
    cntg_vol: str    #체결 거래량
    tday_rltv: str    #당일 체결강도
    prdy_ctrt: str    #전일 대비율

class InquireCcnlBody(BaseModel):
    rt_cd: str    #성공 실패 여부
    msg_cd: str    #응답코드
    msg1: str    #응답메세지
    output: List[InquireCcnlOutput]    #응답상세
