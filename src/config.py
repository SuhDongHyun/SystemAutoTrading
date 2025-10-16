import os
from dataclasses import dataclass
from dotenv import load_dotenv, find_dotenv

# .env 파일 로드
env_path = find_dotenv(".env", raise_error_if_not_found=False)

if not env_path or not os.path.exists(env_path):
    raise FileNotFoundError(
        "⚠️ 환경설정 파일(.env)을 찾을 수 없습니다. "
        "프로젝트 루트 경로에 .env 파일을 생성해 주세요."
    )

# .env → os.environ 로드
load_dotenv(env_path, override=False)

@dataclass(frozen=True)
class Settings:
    # 한국투자증권 API 기본 설정
    BASE_URL: str | None = os.getenv("BASE_URL")
    APP_KEY: str | None = os.getenv("APP_KEY")
    APP_SECRET: str | None = os.getenv("APP_SECRET")

    def validate(self):
        missing = [
            key for key in ["BASE_URL", "APP_KEY", "APP_SECRET"]
            if not getattr(self, key)
        ]
        if missing:
            raise ValueError(f"❌ 필수 환경변수 누락: {', '.join(missing)}")

settings = Settings()
settings.validate()
