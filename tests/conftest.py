import os
import shutil
import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from config import Config
from server import SimpleFEServer


@pytest.fixture(scope="session")
def live_server_url():
   """Starts local static server for the Frontend repository and stops it after tests"""
   server = SimpleFEServer()
   url = server.start()
   yield url
   server.stop()


@pytest.fixture
def driver():
   """Initializes and tears down the Selenium WebDriver"""
   browser = Config.BROWSER


   if browser == "firefox":
       options = FirefoxOptions()
       if Config.HEADLESS:
           options.add_argument("-headless")
       options.add_argument("--width=1920")
       options.add_argument("--height=1080")
       options.set_preference("dom.webnotifications.enabled", False)


       gecko_path = shutil.which("geckodriver") or "/snap/bin/geckodriver"
       if os.path.exists(gecko_path):
           service = FirefoxService(executable_path=gecko_path)
           drv = webdriver.Firefox(service=service, options=options)
       else:
           drv = webdriver.Firefox(options=options)


   elif browser == "chrome":
       options = ChromeOptions()
       if Config.HEADLESS:
           options.add_argument("--headless=new")
       options.add_argument("--no-sandbox")
       options.add_argument("--disable-dev-shm-usage")
       drv = webdriver.Chrome(options=options)


   else:
       raise ValueError(f"Unsupported browser: {browser}")


   drv.implicitly_wait(Config.EXPLICIT_WAIT)
   yield drv
   drv.quit()



