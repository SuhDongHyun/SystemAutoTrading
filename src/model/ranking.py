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
