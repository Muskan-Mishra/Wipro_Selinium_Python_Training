import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_multiple_windows(driver):

    # Open URL
    driver.get("https://the-internet.herokuapp.com/windows")
    time.sleep(2)

    # Click on "Click Here"
    driver.find_element(By.LINK_TEXT, "Click Here").click()
    time.sleep(2)

    # Get all window handles
    windows = driver.window_handles

    # Switch to child window
    driver.switch_to.window(windows[1])
    time.sleep(2)

    wait = WebDriverWait(driver, 10)

    # Wait for child window heading
    heading = wait.until(
        EC.visibility_of_element_located((By.TAG_NAME, "h3"))
    )

    print("Child Window Text:", heading.text)
    assert heading.text == "New Window"

    time.sleep(2)

    # Close child window
    driver.close()
    time.sleep(2)

    # Switch back to parent window
    driver.switch_to.window(windows[0])
    time.sleep(2)

    parent_text = driver.find_element(By.TAG_NAME, "h3")

    print("Parent Window Text:", parent_text.text)
    assert parent_text.text == "Opening a new window"

    time.sleep(2)