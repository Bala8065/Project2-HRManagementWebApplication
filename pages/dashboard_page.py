from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class DashboardPage(BasePage):
    HEADER = (By.XPATH, "//h6[text()='Dashboard']")
    MENU_ITEM = lambda self, name: (By.XPATH, f"//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name' and normalize-space()='{name}']")

    def is_loaded(self):
        return self.is_visible(self.HEADER)

    def open_menu(self, name):
        self.click(self.MENU_ITEM(name))