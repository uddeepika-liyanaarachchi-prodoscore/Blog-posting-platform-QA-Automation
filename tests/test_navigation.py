import pytest
from pages.navbar import Navbar
from pages.login_page import LoginPage
from pages.register_page import RegisterPage
from pages.explore_page import ExplorePage


class TestNavigation:
   """Test Suite: Navigation Bar and View Toggling"""


   def test_tc_nav_01_default_page_load(self, driver, live_server_url):
       """TC_NAV_01: Verify default page load state and visibility of views"""
       driver.get(live_server_url)


       explore_page = ExplorePage(driver)
       login_page = LoginPage(driver)
       register_page = RegisterPage(driver)
       navbar = Navbar(driver)


       assert "Blog Poster Project" in driver.title
       assert explore_page.is_view_displayed() is True
       assert login_page.is_view_displayed() is False
       assert register_page.is_view_displayed() is False
       assert navbar.is_login_btn_visible() is True
       assert navbar.is_dashboard_btn_hidden() is True


   def test_tc_nav_02_navigate_to_login(self, driver, live_server_url):
       """TC_NAV_02: Verify clicking login nav button displays the login view"""
       driver.get(live_server_url)


       navbar = Navbar(driver)
       login_page = LoginPage(driver)
       explore_page = ExplorePage(driver)


       navbar.click_login()
       assert login_page.is_view_displayed() is True
       assert explore_page.is_view_displayed() is False


   def test_tc_nav_03_navigate_back_to_home(self, driver, live_server_url):
       """TC_NAV_03: Verify clicking home nav button returns to the explore view"""
       driver.get(live_server_url)


       navbar = Navbar(driver)
       login_page = LoginPage(driver)
       explore_page = ExplorePage(driver)


       navbar.click_login()
       assert login_page.is_view_displayed() is True


       navbar.click_home()
       assert explore_page.is_view_displayed() is True
       assert login_page.is_view_displayed() is False


   def test_tc_nav_04_toggle_login_and_register(self, driver, live_server_url):
       """TC_NAV_04: Verify toggling between Sign-In and Sign-Up views"""
       driver.get(live_server_url)


       navbar = Navbar(driver)
       login_page = LoginPage(driver)
       register_page = RegisterPage(driver)


       navbar.click_login()
       assert login_page.is_view_displayed() is True


       login_page.click_sign_up_toggle()
       assert register_page.is_view_displayed() is True
       assert login_page.is_view_displayed() is False


       register_page.click_sign_in_toggle()
       assert login_page.is_view_displayed() is True
       assert register_page.is_view_displayed() is False



