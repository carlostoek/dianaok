import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    def __init__(self):
        self.bot_token = os.getenv("BOT_TOKEN")
        self.database_url = os.getenv("DATABASE_URL")

def load_config():
    return Config()