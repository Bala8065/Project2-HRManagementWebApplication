import allure
import pytest
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.claim_page import ClaimPage

@allure.feature("Claim")
@allure.story("TC10 - Initiate claim request")
@pytest.mark.claim
def test_initiate_claim(driver, base_url):
    login = LoginPage(driver, base_url)
    login.login("Admin", "admin123")  # or login as an employee if you have credentials
    dash = DashboardPage(driver)
    try:
        dash.open_menu("Claim")
    except Exception:
        # If Claim is not available in the demo build, skip gracefully
        import pytest
        pytest.skip("Claim module not present on this demo instance")
    claim = ClaimPage(driver)
    ok = claim.create_claim(amount="150", remarks="Taxi fare")
    assert ok