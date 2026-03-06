import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


class Test_Keyboards:

    def test_keyboards(self):

        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()

        driver.get("https://www.facebook.com/")
        time.sleep(3)

        actions = ActionChains(driver)

        email = driver.find_element(By.XPATH, "//input[@name='email']")
        password = driver.find_element(By.XPATH, "//input[@name='pass']")

        email.click()
        actions.send_keys("hello").perform()
        time.sleep(2)

        actions.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
        time.sleep(2)

        actions.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()
        time.sleep(2)

        password.click()
        time.sleep(1)

        actions.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
        time.sleep(3)

        driver.quit()