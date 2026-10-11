from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage


class ExplorePage(BasePage):
   """Explore / Main view interactions and Post Modal locators"""


   VIEW = (By.ID, "main-view")
   HEADING = (By.CSS_SELECTOR, "#main-view header h1")
   PINS_GRID = (By.CSS_SELECTOR, "#main-view .pins-grid")


   # Post Modal elements
   MODAL = (By.ID, "post-modal")
   MODAL_CLOSE_BTN = (By.ID, "modal-close-btn")
   MODAL_BACKDROP = (By.ID, "modal-close-backdrop")
   MODAL_TITLE = (By.ID, "modal-post-title")
   MODAL_DESC = (By.ID, "modal-post-desc")
   MODAL_IMG = (By.ID, "modal-post-img")


   def is_view_displayed(self) -> bool:
       return self.is_visible(self.VIEW) and not self.is_hidden(self.VIEW)


   def get_heading_text(self) -> str:
       return self.get_text(self.HEADING)


   def is_modal_visible(self) -> bool:
       return self.is_visible(self.MODAL) and not self.is_hidden(self.MODAL)


   def click_modal_close_btn(self):
       self.click(self.MODAL_CLOSE_BTN)


   def click_modal_backdrop(self):
       self.click(self.MODAL_BACKDROP)


   def press_escape_key(self):
       self.find(self.MODAL).send_keys(Keys.ESCAPE)


   def open_sample_modal(self, title="Test Blog", desc="Sample content"):
       """Calls the frontend's native openPostModal function to test modal UI behavior"""
       script = f"""
       import('./js/posts.js').then(module => {{
           module.openPostModal({{
               id: 999,
               title: '{title}',
               content: '{desc}',
               image_url: ''
           }});
       }});
       """
       self.execute_script(script)



