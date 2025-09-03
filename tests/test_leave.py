import allure
import pytest
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.leave_page import LeavePage


@allure.feature("Leave")
@allure.story("TC9 - Assign leave and verify")
@pytest.mark.leave
def test_assign_leave(driver, base_url):
    login = LoginPage(driver, base_url)
    login.login("Admin", "admin123")

    dash = DashboardPage(driver)
    dash.open_menu("Leave")

    leave = LeavePage(driver)
    leave.open_assign_leave()

    ok = leave.assign_leave(
        employee_name="Jobin Mathew Sam",
        leave_type="CAN - FMLA",
        from_date="2025-09-01",
        to_date="",
        comment="Automation assignment"
    )

    assert ok, "Warning Failed to submit – Success toast not found!"

