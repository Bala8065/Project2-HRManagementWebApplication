from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class LoginPage(BasePage):
    USERNAME = (By.NAME, "username")  # double-check in browser DevTools
    PASSWORD = (By.NAME, "password")
    LOGIN_BTN = (By.XPATH, "//button[@type='submit']")
    ERROR_MSG = (By.CSS_SELECTOR, "p.oxd-text.oxd-alert-content-text")
    FORGOT_LINK = (By.XPATH, "//p[@class='oxd-text oxd-text--p orangehrm-login-forgot-header']")  # <-- updated

    def __init__(self, driver, base_url):
        super().__init__(driver)
        driver.get(f"{base_url}/web/index.php/auth/login")

    def login(self, username, password):
        """Login to OrangeHRM with proper waits."""
        wait = WebDriverWait(self.driver, 10)  # <- Now this is defined

        # Wait for username field
        username_field = wait.until(EC.visibility_of_element_located(self.USERNAME))
        username_field.clear()
        username_field.send_keys(username)

        # Wait for password field
        password_field = wait.until(EC.visibility_of_element_located(self.PASSWORD))
        password_field.clear()
        password_field.send_keys(password)

        # Wait for login button and click
        login_btn = wait.until(EC.element_to_be_clickable(self.LOGIN_BTN))
        login_btn.click()

    def click_forgot_password(self):
        self.click(self.FORGOT_LINK)

    def get_error_message(self):
        if self.is_visible(self.ERROR_MSG):
            return self.get_text(self.ERROR_MSG)
        return ""