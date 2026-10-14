import os
from dotenv import load_dotenv
load_dotenv();

class Config:
   FE_DIR = os.path.abspath(
       os.path.join(os.path.dirname(__file__), "..", "Blog-Poster-Project-FE")
   )
   PORT = int(os.getenv("PORT", "5500"))
   BASE_URL = os.getenv("BASE_URL", f"")


   # Browser configurations
   BROWSER = os.getenv("BROWSER", "").lower()
   HEADLESS = os.getenv("HEADLESS", "").lower() in ("true", "1", "yes")
   EXPLICIT_WAIT = int(os.getenv("EXPLICIT_WAIT", "10"))


