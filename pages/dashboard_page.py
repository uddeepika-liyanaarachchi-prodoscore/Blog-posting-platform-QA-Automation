from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class DashboardPage(BasePage):
   """Dashboard / My View interactions and locators"""


   VIEW = (By.ID, "my-view")
   HEADING = (By.ID, "HI")
   LOGOUT_BTN = (By.ID, "logout-btn")
   PINS_GRID = (By.CSS_SELECTOR, "#my-view .pins-grid")


   def is_view_displayed(self) -> bool:
       return self.is_visible(self.VIEW) and not self.is_hidden(self.VIEW)


   def get_heading_text(self) -> str:
       return self.get_text(self.HEADING)


   def click_logout(self):
       self.click(self.LOGOUT_BTN)


   def set_mock_session(self, access_token="mock_token_123", user_id="1"):
       """Sets auth tokens in localStorage and reloads to simulate authenticated session"""
       script = f"""
       localStorage.setItem('accessToken', '{access_token}');
       localStorage.setItem('refreshToken', 'mock_refresh_456');
       localStorage.setItem('userID', '{user_id}');
       """
       self.execute_script(script)
       self.driver.refresh()


   def clear_session(self):
       self.execute_script("localStorage.clear();")
       self.driver.refresh()


   def get_local_storage_item(self, key: str):
       return self.execute_script(f"return localStorage.getItem('{key}');")



