import os
import pytest
from utils.driver_factory import DriverFactory

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser: chrome or firefox")
    parser.addoption("--base_url", action="store", default="https://opensource-demo.orangehrmlive.com")

@pytest.fixture(scope="session")
def base_url(pytestconfig):
    return pytestconfig.getoption("--base_url")

@pytest.fixture
def driver(pytestconfig):
    browser = pytestconfig.getoption("--browser")
    driver = DriverFactory.get_driver(browser)
    yield driver
    driver.quit()