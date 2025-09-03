from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from pages.base_page import BasePage


class LeavePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)


    ASSIGN_LEAVE_BTN = (By.LINK_TEXT, "Assign Leave")
    EMPLOYEE_NAME = (By.XPATH, "//input[@placeholder='Type for hints...']")
    EMPLOYEE_SUGGESTION = "//div[@role='listbox']//span[text()='{}']"
    LEAVE_TYPE = (By.XPATH, "//label[text()='Leave Type']/../following-sibling::div//div[@class='oxd-select-text-input']")
    LEAVE_TYPE_OPTION = "//div[@role='listbox']//span[text()='{}']"
    FROM_DATE = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/input[1]")
    TO_DATE = (By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div/form/div[3]/div/div[2]/div/div[2]/div/div/input")
    COMMENT = (By.XPATH, "//textarea")
    ASSIGN_BTN = (By.XPATH, "//button[@type='submit']")
    SUCCESS_TOAST = (By.XPATH, "//div[contains(@class,'oxd-toast') and contains(.,'Success')]")
    CONFIRM_BTN = (By.XPATH, "/html[1]/body[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[3]/button[2]")  # popup OK button


    def open_assign_leave(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.ASSIGN_LEAVE_BTN)
        ).click()

    def assign_leave(self, employee_name, leave_type, from_date, to_date, comment=""):
        wait = WebDriverWait(self.driver, 10)

        # Employee name (autocomplete handling with fallback)
        emp = wait.until(EC.visibility_of_element_located(self.EMPLOYEE_NAME))
        emp.clear()
        emp.send_keys(employee_name)

        suggestion_locator = (By.XPATH, self.EMPLOYEE_SUGGESTION.format(employee_name))
        try:
            wait.until(EC.element_to_be_clickable(suggestion_locator)).click()
        except TimeoutException:
            # Fallback: just press ENTER if no suggestion pops up
            emp.send_keys("\n")

        # Leave type
        wait.until(EC.element_to_be_clickable(self.LEAVE_TYPE)).click()
        option_locator = (By.XPATH, self.LEAVE_TYPE_OPTION.format(leave_type))
        wait.until(EC.element_to_be_clickable(option_locator)).click()

        # Dates
        from_input = wait.until(EC.visibility_of_element_located(self.FROM_DATE))
        from_input.clear()
        from_input.send_keys(from_date)

        to_input = wait.until(EC.visibility_of_element_located(self.TO_DATE))
        to_input.clear()
        to_input.send_keys(to_date)

        # Comment
        if comment:
            com = wait.until(EC.visibility_of_element_located(self.COMMENT))
            com.clear()
            com.send_keys(comment)

        # Submit
        wait.until(EC.element_to_be_clickable(self.ASSIGN_BTN)).click()

        # Confirm success
        try:
            wait.until(EC.visibility_of_element_located(self.SUCCESS_TOAST))
            return True
        except Exception:
            return False
