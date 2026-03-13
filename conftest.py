import pytest
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# Download directory
DOWNLOAD_DIR = os.path.join(os.getcwd(), "downloads")
os.makedirs(DOWNLOAD_DIR, exist_ok=True)


@pytest.fixture(scope="session")
def download_dir():
    return DOWNLOAD_DIR


@pytest.fixture(scope="function")
def driver():

    chrome_options = webdriver.ChromeOptions()

    prefs = {
        "download.default_directory": DOWNLOAD_DIR,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True
    }

    chrome_options.add_experimental_option("prefs", prefs)
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--start-maximized")

    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()),
        options=chrome_options
    )

    driver.get("https://bstackdemo.com/")

    yield driver


    driver.quit()


# Screenshot on failure
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:

        driver = item.funcargs.get("driver")

        if driver:
            timestamp = time.strftime("%Y%m%d_%H%M%S")
            screenshot_path = os.path.join(
                DOWNLOAD_DIR, f"{item.name}_{timestamp}.png"
            )

            driver.save_screenshot(screenshot_path)

            print(f"\nScreenshot saved at: {screenshot_path}")