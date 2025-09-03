from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ForgotPasswordPage(BasePage):
    USERNAME = (By.NAME, "username")
    RESET_BTN = (By.CSS_SELECTOR, "button[type='submit']")
    CONFIRM_TEXT = (By.XPATH, "//*[contains(text(),'reset link') or contains(text(),'instructions')]")


    def reset(self, username):
        self.type(self.USERNAME, username)
        self.click(self.RESET_BTN)

    def is_confirmation_shown(self):
        return self.is_visible(self.CONFIRM_TEXT)