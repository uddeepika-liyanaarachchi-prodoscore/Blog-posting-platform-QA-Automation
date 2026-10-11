import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from pages.explore_page import ExplorePage


class TestModalUI:
   """Test Suite: Blog Post Details Modal Interactions"""


   def test_tc_modal_01_open_modal(self, driver, live_server_url):
       """TC_MODAL_01: Verify opening modal displays correct title and content"""
       driver.get(live_server_url)


       explore_page = ExplorePage(driver)
       assert explore_page.is_modal_visible() is False


       # Open post modal
       explore_page.open_sample_modal(title="Exploring Automation", desc="Deep dive into functional testing.")
       time.sleep(0.3)


       assert explore_page.is_modal_visible() is True
       modal_title = explore_page.get_text(explore_page.MODAL_TITLE)
       modal_desc = explore_page.get_text(explore_page.MODAL_DESC)


       assert modal_title == "Exploring Automation"
       assert "Deep dive into functional testing." in modal_desc


   def test_tc_modal_02_close_via_close_button(self, driver, live_server_url):
       """TC_MODAL_02: Verify clicking the 'x' close button closes the modal"""
       driver.get(live_server_url)


       explore_page = ExplorePage(driver)
       explore_page.open_sample_modal()
       time.sleep(0.3)
       assert explore_page.is_modal_visible() is True


       explore_page.click_modal_close_btn()
       time.sleep(0.3)
       assert explore_page.is_modal_visible() is False


   def test_tc_modal_03_close_via_backdrop(self, driver, live_server_url):
       """TC_MODAL_03: Verify clicking modal backdrop closes the modal"""
       driver.get(live_server_url)


       explore_page = ExplorePage(driver)
       explore_page.open_sample_modal()
       time.sleep(0.3)
       assert explore_page.is_modal_visible() is True


       # Click backdrop directly
       driver.execute_script("document.getElementById('modal-close-backdrop').click();")
       time.sleep(0.3)
       assert explore_page.is_modal_visible() is False


   def test_tc_modal_04_close_via_escape_key(self, driver, live_server_url):
       """TC_MODAL_04: Verify pressing Escape key closes the modal"""
       driver.get(live_server_url)


       explore_page = ExplorePage(driver)
       explore_page.open_sample_modal()
       time.sleep(0.3)
       assert explore_page.is_modal_visible() is True


       # Send Escape key to document
       ActionChains(driver).send_keys(Keys.ESCAPE).perform()
       time.sleep(0.3)
       assert explore_page.is_modal_visible() is False



