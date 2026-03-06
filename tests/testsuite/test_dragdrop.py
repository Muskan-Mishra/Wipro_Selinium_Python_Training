import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


class Test_DragDrop:

    def test_dragdrop(self):

        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()


        driver.get("https://the-internet.herokuapp.com/drag_and_drop")
        time.sleep(3)

        actions = ActionChains(driver)

        source = driver.find_element(By.XPATH, "//div[@id='column-a']")
        dest = driver.find_element(By.XPATH, "//div[@id='column-b']")

        actions.drag_and_drop(source, dest).perform()
        time.sleep(4)

        driver.quit()