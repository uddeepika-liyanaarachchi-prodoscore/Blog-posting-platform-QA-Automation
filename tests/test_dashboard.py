import pytest
from pages.navbar import Navbar
from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage


class TestDashboardUI:
   """Test Suite: User Dashboard and Session Management"""


   def test_tc_dash_01_authenticated_session_ui(self, driver, live_server_url):
       """TC_DASH_01: Verify authenticated UI state when accessToken is present in session"""
       driver.get(live_server_url)


       dashboard_page = DashboardPage(driver)
       navbar = Navbar(driver)


       # Simulate logged in user by storing accessToken in localStorage
       dashboard_page.set_mock_session(access_token="valid_jwt_token_example", user_id="101")


       assert navbar.is_dashboard_btn_visible() is True
       assert navbar.is_login_btn_visible() is False
       assert dashboard_page.is_view_displayed() is True
       assert "Welcome to Blog Poster" in dashboard_page.get_heading_text()


   def test_tc_dash_02_logout_session_cleanup(self, driver, live_server_url):
       """TC_DASH_02: Verify clicking logout clears localStorage and returns to login view"""
       driver.get(live_server_url)


       dashboard_page = DashboardPage(driver)
       navbar = Navbar(driver)
       login_page = LoginPage(driver)


       # Set logged in state
       dashboard_page.set_mock_session()
       assert dashboard_page.is_view_displayed() is True


       # Perform logout
       dashboard_page.click_logout()


       # Check localStorage was cleared
       token = dashboard_page.get_local_storage_item("accessToken")
       assert token is None


       # Check UI transitions to login view
       assert login_page.is_view_displayed() is True
       assert navbar.is_dashboard_btn_hidden() is True
       assert navbar.is_login_btn_visible() is True



