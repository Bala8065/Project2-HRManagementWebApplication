import allure
import pytest
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.myinfo_page import MyInfoPage
from selenium.webdriver.common.by import By

@allure.feature("Menu")
@allure.story("TC4 - Main menu visibility & clickability")
@pytest.mark.menu
def test_main_menu_items(driver, base_url):
    login = LoginPage(driver, base_url)
    login.login("Admin", "admin123")
    dash = DashboardPage(driver)
    assert dash.is_loaded()

    for item in ["Admin", "PIM", "Leave", "Time", "Recruitment", "My Info", "Performance", "Dashboard"]:
        dash.open_menu(item)

@allure.feature("My Info")
@allure.story("TC8 - My Info sub-sections present")
@pytest.mark.myinfo
def test_myinfo_sections(driver, base_url):
    login = LoginPage(driver, base_url)
    login.login("Admin", "admin123")
    dash = DashboardPage(driver)
    dash.open_menu("My Info")
    my = MyInfoPage(driver)

    expected_sections = [
        "Personal Details",
        "Contact Details",
        "Emergency Contacts",
    ]
    for sec in expected_sections:
        assert my.is_section_present(sec), f"Missing My Info section: {sec}"