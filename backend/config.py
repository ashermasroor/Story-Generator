from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):

    SAVE_DIR: str
    LLM_API_KEY: str
    LLM_BASE_URL: str

    model_config = SettingsConfigDict(env_file="story_gen/backend/.env",extra="ignore")

Config = Settings()
