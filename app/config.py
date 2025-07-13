import os
from dotenv import load_dotenv

load_dotenv()

VERSION = "0.0.1"
API_BASE_URL = os.getenv("API_BASE_URL", "http://localhost:8000/api")
ADMIN_USERNAME = os.getenv("ADMIN_USERNAME", "admin")
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD", "admin")
SECRET_KEY = os.getenv("SECRET_KEY", "supersecretkey")