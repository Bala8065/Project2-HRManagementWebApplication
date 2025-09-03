from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

class DriverFactory:
    @staticmethod
    def get_driver(browser="chrome", headless=False):
        if browser.lower() == "chrome":
            options = ChromeOptions()
            if headless:
                options.add_argument("--headless=new")
            options.add_argument("--start-maximized")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        elif browser.lower() == "firefox":
            options = FirefoxOptions()
            if headless:
                options.add_argument("-headless")
            driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)
            driver.maximize_window()
        else:
            raise ValueError(f"Unsupported browser: {browser}")
        driver.implicitly_wait(5)
        return driver