from dotenv import load_dotenv
import os

load_dotenv()

APP_NAME = os.getenv("APP_NAME", "FinVerse API")
APP_VERSION = os.getenv("APP_VERSION", "0.1.0")
DEBUG = os.getenv("DEBUG", "False") == "True"