from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class AdminPage(BasePage):
    USERS_TAB = (By.XPATH, "//h6[normalize-space()='User Management'] | //h6[normalize-space()='Users']")
    #ADD_BTN = (By.XPATH, "//button[.//i[contains(@class,'bi-plus') or contains(@class,'plus')]] | //button[normalize-space()='Add']")
    SAVE_BTN = (By.XPATH, "//button[normalize-space()='Save']")
    ADD_BTN = (By.XPATH, "//button[normalize-space()='Add']")
    SEARCH_BTN = (By.XPATH, "//button[@type='submit']")

    # Add User form fields (new UI)
    ROLE_DROPDOWN = (By.XPATH, "//label[normalize-space()='User Role']/following::div[contains(@class,'oxd-select-dropdown')] | //label[normalize-space()='User Role']/following::div[contains(@class,'oxd-select-text')][1]")
    STATUS_DROPDOWN = (By.XPATH, "//label[normalize-space()='Status']/following::div[contains(@class,'oxd-select-text')][1]")
    EMPLOYEE_NAME = (By.XPATH, "//label[normalize-space()='Employee Name']/following::input[1] | //label[normalize-space()='Employee Name']/following::div//input")
    USERNAME = (By.XPATH, "//label[normalize-space()='Username']/following::input[1]")
    PASSWORD = (By.XPATH, "//label[normalize-space()='Password']/following::input[1]")
    CONFIRM_PASSWORD = (By.XPATH, "//label[normalize-space()='Confirm Password']/following::input[1]")

    SEARCH_USERNAME = (By.XPATH, "//label[normalize-space()='Username']/following::input[1]")
    SEARCH_BTN = (By.XPATH, "//button[normalize-space()='Search']")
    RESULT_ROW = (By.XPATH, "//div[contains(@class,'oxd-table-card')]")

    def open_add_user(self):
        # click Add on Users grid
        self.click(self.ADD_BTN)

    def create_user(self, employee_name, username, password, user_role=None, status=None):
        # open role dropdowns if present
        try:
            if user_role:
                self.click(self.ROLE_DROPDOWN)
            if status:
                self.click(self.STATUS_DROPDOWN)
        except Exception:
            pass
        self.type(self.EMPLOYEE_NAME, employee_name)
        # choose first suggestion if any
        try:
            from selenium.webdriver.common.by import By
            self.click((By.XPATH, "//div[@role='listbox']//span"))
        except Exception:
            pass
        self.type(self.USERNAME, username)
        self.type(self.PASSWORD, password)
        self.type(self.CONFIRM_PASSWORD, password)
        self.click(self.SAVE_BTN)

    def search_user(self, username):
        self.type((By.XPATH, "//input[@placeholder='Type for hints...']"), username)
        self.click(self.SEARCH_BTN)
        return True