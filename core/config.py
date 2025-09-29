from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = ""
    JWT_SECRET_KEY: str = ""
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 1

    DB_SERVER: str = ""
    DB_USER: str = ""
    DB_PASSWORD: str = ""
    DB_NAME: str = "HSRPOEM"
    DB_PORT: str = ""

    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings()
