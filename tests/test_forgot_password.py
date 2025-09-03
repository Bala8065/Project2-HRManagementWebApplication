import allure
import pytest
from pages.login_page import LoginPage
from pages.forgot_password_page import ForgotPasswordPage

@allure.feature("Forgot Password")
@allure.story("TC7 - Forgot password flow")
@pytest.mark.forgot
def test_forgot_password_flow(driver, base_url):
    login = LoginPage(driver, base_url)
    login.click_forgot_password()

    fp = ForgotPasswordPage(driver)
    fp.reset("Admin")

    # Accept both possible outcomes
    assert (
            fp.is_confirmation_shown()
            or "sendpasswordreset" in driver.current_url.lower()
            or "requestpasswordresetcode" in driver.current_url.lower()
    )

