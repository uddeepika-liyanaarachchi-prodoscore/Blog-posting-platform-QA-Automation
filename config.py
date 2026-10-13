import os

class Config:
   # URL to the Frontend under test
   # By default, points to local test server serving the FE repository
   FE_DIR = os.path.abspath(
       os.path.join(os.path.dirname(__file__), "..", "Blog-Poster-Project-FE")
   )
   PORT = int(os.getenv("PORT", "5500"))
   BASE_URL = os.getenv("BASE_URL", f"")


   # Browser configurations
   BROWSER = os.getenv("BROWSER", "firefox").lower()
   HEADLESS = os.getenv("HEADLESS", "true").lower() in ("true", "1", "yes")
   EXPLICIT_WAIT = int(os.getenv("EXPLICIT_WAIT", "10"))


