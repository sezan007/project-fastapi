from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    #model_config = ConfigDict(extra='ignore')
    database_hostname:str
    database_port:str
    database_password:str
    database_name:str
    database_username:str
    secret_key:str
    algorithm:str
    access_token_expire_minutes:int
    class Config:
        env_file= ".env"

settings=Settings()
#print(settings.access_token_expire_minutes)
