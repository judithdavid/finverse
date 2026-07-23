from dotenv import load_dotenv
import os
print("config.py:", __file__)
print("cwd:", os.getcwd())
load_dotenv()

APP_NAME = os.getenv("APP_NAME", "FinVerse API")
APP_VERSION = os.getenv("APP_VERSION", "0.1.0")
DEBUG = os.getenv("DEBUG", "False") == "True"

DATABASE_URL = os.getenv("DATABASE_URL")

print("DATABASE_URL:", DATABASE_URL)