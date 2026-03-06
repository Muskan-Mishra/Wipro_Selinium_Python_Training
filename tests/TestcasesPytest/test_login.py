import pytest
from pages.login_page import LoginPage
from utilities.logger import get_logger

logger = get_logger()


class TestLogin:

    def test_valid_login(self, driver):
        logger.info("Opening application")
        driver.get("https://opensource-demo.orangehrmlive.com/")

        lp = LoginPage(driver)

        logger.info("Entering valid credentials")
        lp.login(username="Admin", password="admin123")

        assert "OrangeHRM" in driver.title
        logger.info("Valid login test passed")

    def test_invalid_login(self, driver):
        logger.info("Opening application")
        driver.get("https://opensource-demo.orangehrmlive.com/")

        lp = LoginPage(driver)

        logger.info("Entering invalid credentials")
        lp.login(username="Admin", password="wrongpassword")

        error_message = lp.get_error_message()
        assert "Invalid credentials" in error_message
        logger.info("Invalid login test passed")
