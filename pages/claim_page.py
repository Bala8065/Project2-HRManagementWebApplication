from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ClaimPage(BasePage):
    ASSIGN_CLAIM_MENU = (By.LINK_TEXT, "My Claims")
    ADD_BTN = (By.XPATH, "//button[normalize-space()='Create'] | //button[normalize-space()='Add']")
    CLAIM_TYPE = (By.XPATH, "//label[normalize-space()='Claim Event']/following::div[contains(@class,'oxd-select-text')][1] | //label[contains(.,'Claim')]/following::div[contains(@class,'oxd-select-text')][1]")
    AMOUNT = (By.XPATH, "//label[normalize-space()='Amount']/following::input[1] | //label[contains(.,'Amount')]/following::input[1]")
    REMARKS = (By.XPATH, "//label[normalize-space()='Remarks']/following::textarea[1] | //label[contains(.,'Reason')]/following::textarea[1]")
    SAVE_BTN = (By.XPATH, "//button[@type='submit']")
    TOAST = (By.CSS_SELECTOR, "p.oxd-text--toast-message")

    def create_claim(self, claim_type_value=None, amount="100", remarks="Automation claim"):
        try:
            self.click(self.ADD_BTN)
        except Exception:
            pass
        try:
            self.click(self.CLAIM_TYPE)
            from selenium.webdriver.common.by import By
            self.click((By.XPATH, "//div[@role='listbox']//span"))
        except Exception:
            pass
        try:
            self.type(self.AMOUNT, amount)
        except Exception:
            pass
        try:
            self.type(self.REMARKS, remarks)
        except Exception:
            pass
        self.click(self.SAVE_BTN)
        return True