
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class RegisterPage(BasePage):
   """Register / Sign-up view interactions and locators"""


   VIEW = (By.ID, "sign-up-view")
   FORM = (By.ID, "sign-up-form")
   EMAIL_INPUT = (By.ID, "signup_mail")
   PASSWORD_INPUT = (By.ID, "register_password")
   SUBMIT_BTN = (By.CSS_SELECTOR, "#sign-up-form button.sign")
   SIGN_IN_LINK = (By.ID, "sign-in-btn")


   def is_view_displayed(self) -> bool:
       return self.is_visible(self.VIEW) and not self.is_hidden(self.VIEW)


   def enter_email(self, email: str):
       self.type_text(self.EMAIL_INPUT, email)


   def enter_password(self, password: str):
       self.type_text(self.PASSWORD_INPUT, password)


   def click_submit(self):
       self.click(self.SUBMIT_BTN)


   def click_sign_in_toggle(self):
       self.click(self.SIGN_IN_LINK)


   def register(self, email: str, password: str):
       self.enter_email(email)
       self.enter_password(password)
       self.click_submit()


