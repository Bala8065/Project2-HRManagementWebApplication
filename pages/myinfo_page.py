from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class MyInfoPage(BasePage):
    SECTION = lambda self, text: (By.XPATH, f"//a[contains(@class,'orangehrm-tabs-item') and normalize-space()='{text}']")

    def is_section_present(self, text):
        return self.is_visible(self.SECTION(text))