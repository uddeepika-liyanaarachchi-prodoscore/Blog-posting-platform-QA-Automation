from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class Navbar(BasePage):
   """Navbar component for top-level navigation"""


   HOME_BTN = (By.ID, "navhome-btn")
   LOGIN_BTN = (By.ID, "navlogin-btn")
   DASHBOARD_BTN = (By.ID, "navdashboard-btn")


   def click_home(self):
       self.click(self.HOME_BTN)


   def click_login(self):
       self.click(self.LOGIN_BTN)


   def click_dashboard(self):
       self.click(self.DASHBOARD_BTN)


   def is_login_btn_visible(self) -> bool:
       return self.is_visible(self.LOGIN_BTN)


   def is_dashboard_btn_visible(self) -> bool:
       return self.is_visible(self.DASHBOARD_BTN)


   def is_dashboard_btn_hidden(self) -> bool:
       return self.is_hidden(self.DASHBOARD_BTN)
