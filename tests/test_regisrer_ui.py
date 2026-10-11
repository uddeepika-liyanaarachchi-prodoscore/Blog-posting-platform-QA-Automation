import pytest
from pages.navbar import Navbar
from pages.login_page import LoginPage
from pages.register_page import RegisterPage


class TestRegisterUI:
   """Test Suite: Register / Sign-Up View UI Components"""


   def test_tc_reg_01_elements_presence(self, driver, live_server_url):
       """TC_REG_01: Verify registration form inputs and submit button presence"""
       driver.get(live_server_url)


       navbar = Navbar(driver)
       login_page = LoginPage(driver)
       register_page = RegisterPage(driver)


       navbar.click_login()
       login_page.click_sign_up_toggle()


       assert register_page.is_view_displayed() is True


       email_input = register_page.find(register_page.EMAIL_INPUT)
       password_input = register_page.find(register_page.PASSWORD_INPUT)


       assert email_input.get_attribute("type") == "email"
       assert "email" in email_input.get_attribute("placeholder").lower()
       assert "password" in password_input.get_attribute("placeholder").lower()


   def test_tc_reg_02_fill_registration_fields(self, driver, live_server_url):
       """TC_REG_02: Verify inputs accept typed values properly"""
       driver.get(live_server_url)


       navbar = Navbar(driver)
       login_page = LoginPage(driver)
       register_page = RegisterPage(driver)


       navbar.click_login()
       login_page.click_sign_up_toggle()


       test_email = "newuser@example.com"
       test_pass = "SecurePass@2026"


       register_page.enter_email(test_email)
       register_page.enter_password(test_pass)


       email_val = register_page.find(register_page.EMAIL_INPUT).get_attribute("value")
       pwd_val = register_page.find(register_page.PASSWORD_INPUT).get_attribute("value")


       assert email_val == test_email
       assert pwd_val == test_pass


   def test_tc_reg_03_navigation_back_to_login(self, driver, live_server_url):
       """TC_REG_03: Verify clicking 'Sign In' returns user to login view"""
       driver.get(live_server_url)


       navbar = Navbar(driver)
       login_page = LoginPage(driver)
       register_page = RegisterPage(driver)


       navbar.click_login()
       login_page.click_sign_up_toggle()
       assert register_page.is_view_displayed() is True


       register_page.click_sign_in_toggle()
       assert login_page.is_view_displayed() is True
       assert register_page.is_view_displayed() is False



