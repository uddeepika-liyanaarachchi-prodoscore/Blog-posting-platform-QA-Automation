import pytest
from pages.navbar import Navbar
from pages.login_page import LoginPage


class TestLoginUI:
   """Test Suite: Login View UI Components and Form Validations"""


   def test_tc_login_01_elements_presence(self, driver, live_server_url):
       """TC_LOGIN_01: Verify all required login form elements exist with proper attributes"""
       driver.get(live_server_url)


       navbar = Navbar(driver)
       login_page = LoginPage(driver)


       navbar.click_login()
       assert login_page.is_view_displayed() is True


       email_input = login_page.find(login_page.EMAIL_INPUT)
       password_input = login_page.find(login_page.PASSWORD_INPUT)


       assert email_input.get_attribute("type") == "email"
       assert email_input.get_attribute("required") == "true"
       assert password_input.get_attribute("type") == "password"
       assert password_input.get_attribute("required") == "true"


   def test_tc_login_02_empty_submission_validation(self, driver, live_server_url):
       """TC_LOGIN_02: Verify client-side HTML5 validation when submitting empty login form"""
       driver.get(live_server_url)


       navbar = Navbar(driver)
       login_page = LoginPage(driver)


       navbar.click_login()
       login_page.click_submit()


       msg = login_page.get_email_validation_message()
       assert len(msg) > 0, "Expected HTML5 validation message on required email field"


   def test_tc_login_03_invalid_email_format(self, driver, live_server_url):
       """TC_LOGIN_03: Verify browser validation error when entering malformed email"""
       driver.get(live_server_url)


       navbar = Navbar(driver)
       login_page = LoginPage(driver)


       navbar.click_login()
       login_page.enter_email("invalid-email-no-at")
       login_page.enter_password("SomePassword123")
       login_page.click_submit()


       msg = login_page.get_email_validation_message()
       assert "@" in msg or "email" in msg.lower() or len(msg) > 0


   def test_tc_login_04_fill_credentials(self, driver, live_server_url):
       """TC_LOGIN_04: Verify entering email and password correctly updates input values"""
       driver.get(live_server_url)


       navbar = Navbar(driver)
       login_page = LoginPage(driver)


       navbar.click_login()
       test_email = "tester@example.com"
       test_pwd = "SecretPassword123"


       login_page.enter_email(test_email)
       login_page.enter_password(test_pwd)


       email_val = login_page.find(login_page.EMAIL_INPUT).get_attribute("value")
       pwd_val = login_page.find(login_page.PASSWORD_INPUT).get_attribute("value")


       assert email_val == test_email
       assert pwd_val == test_pwd



