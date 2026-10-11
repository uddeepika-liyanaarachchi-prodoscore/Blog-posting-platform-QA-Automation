from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
   """Login view interactions and locators"""


   VIEW = (By.ID, "login-view")
   FORM = (By.ID, "login-form")
   EMAIL_INPUT = (By.ID, "login_email")
   PASSWORD_INPUT = (By.ID, "password")
   SIGN_IN_BTN = (By.CSS_SELECTOR, "#login-form button.sign")
   SIGN_UP_LINK = (By.ID, "sign-up-btn")


   def is_view_displayed(self) -> bool:
       return self.is_visible(self.VIEW) and not self.is_hidden(self.VIEW)


   def enter_email(self, email: str):
       self.type_text(self.EMAIL_INPUT, email)


   def enter_password(self, password: str):
       self.type_text(self.PASSWORD_INPUT, password)


   def click_submit(self):
       self.click(self.SIGN_IN_BTN)


   def click_sign_up_toggle(self):
       self.click(self.SIGN_UP_LINK)


   def login(self, email: str, password: str):
       self.enter_email(email)
       self.enter_password(password)
       self.click_submit()


   def get_email_validation_message(self) -> str:
       element = self.find(self.EMAIL_INPUT)
       return self.execute_script("return arguments[0].validationMessage;", element)


   def get_password_validation_message(self) -> str:
       element = self.find(self.PASSWORD_INPUT)
       return self.execute_script("return arguments[0].validationMessage;", element)


