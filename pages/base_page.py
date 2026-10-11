from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from config import Config


class BasePage:
   """Base class for all Page Objects with common helper methods"""


   def __init__(self, driver):
       self.driver = driver
       self.wait = WebDriverWait(driver, Config.EXPLICIT_WAIT)


   def open(self, url: str):
       self.driver.get(url)


   def find(self, locator, timeout=None):
       wait = WebDriverWait(self.driver, timeout or Config.EXPLICIT_WAIT)
       return wait.until(EC.presence_of_element_located(locator))


   def find_visible(self, locator, timeout=None):
       wait = WebDriverWait(self.driver, timeout or Config.EXPLICIT_WAIT)
       return wait.until(EC.visibility_of_element_located(locator))


   def click(self, locator):
       element = self.find(locator)
       element.click()


   def type_text(self, locator, text: str):
       element = self.find(locator)
       element.clear()
       element.send_keys(text)


   def get_text(self, locator) -> str:
       return self.find(locator).text


   def is_visible(self, locator, timeout=2) -> bool:
       try:
           wait = WebDriverWait(self.driver, timeout)
           element = wait.until(EC.visibility_of_element_located(locator))
           return element.is_displayed()
       except (TimeoutException, NoSuchElementException):
           return False


   def is_hidden(self, locator, timeout=2) -> bool:
       """Returns True if the element is either absent or has class 'hidden'"""
       try:
           element = self.driver.find_element(*locator)
           classes = element.get_attribute("class") or ""
           return "hidden" in classes or not element.is_displayed()
       except NoSuchElementException:
           return True


   def get_attribute(self, locator, attr_name: str) -> str:
       return self.find(locator).get_attribute(attr_name)


   def get_alert_text(self, timeout=3) -> str:
       try:
           wait = WebDriverWait(self.driver, timeout)
           alert = wait.until(EC.alert_is_present())
           text = alert.text
           alert.accept()
           return text
       except TimeoutException:
           return ""


   def execute_script(self, script: str, *args):
       return self.driver.execute_script(script, *args)



