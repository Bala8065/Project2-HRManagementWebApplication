import csv
import allure
import pytest
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

@allure.feature("Login")
@allure.story("TC2 - Home URL accessible")
@pytest.mark.login
@pytest.mark.smoke
def test_home_url_accessible(driver, base_url):
    driver.get(base_url)
    assert base_url in driver.current_url or "/auth/login" in driver.current_url

@allure.feature("Login")
@allure.story("TC3 - Login fields present")
@pytest.mark.login
def test_login_fields_present(driver, base_url):
    login = LoginPage(driver, base_url)
    # If we reached here without error, fields are visible by BasePage waits during typing
    assert login.is_visible(LoginPage.USERNAME)
    assert login.is_visible(LoginPage.PASSWORD)

@allure.feature("Login")
@allure.story("TC1 - Data-driven login")
@pytest.mark.login
@pytest.mark.parametrize("username,password,valid", [
    ("Admin", "admin123", True),
    ("Admin", "wrongpass", False),
    ("invalidUser", "admin123", False),
    ("", "", False),
])
def test_login_multiple_credentials(driver, base_url, username, password, valid):
    login = LoginPage(driver, base_url)
    login.login(username, password)
    dash = DashboardPage(driver)
    if valid:
        assert dash.is_loaded(), "Expected successful login with valid credentials"
    else:
        assert "Invalid" in login.get_error_message() or not dash.is_loaded(), "Expected invalid login to be rejected"

@allure.feature("Login")
@allure.story("TC1.1 - Logout after successful login")
@pytest.mark.login
def test_logout_after_login(driver, base_url):
    login = LoginPage(driver, base_url)
    login.login("Admin", "admin123")
    dash = DashboardPage(driver)
    assert dash.is_loaded()
    # open user dropdown and logout
    from selenium.webdriver.common.by import By
    USER_DROPDOWN = (By.CSS_SELECTOR, "p.oxd-userdropdown-name")
    LOGOUT = (By.XPATH, "//a[normalize-space()='Logout']")
    dash.click(USER_DROPDOWN)
    dash.click(LOGOUT)
    assert "/auth/login" in driver.current_url