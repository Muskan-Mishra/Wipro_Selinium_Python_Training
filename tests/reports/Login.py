import time
from selenium import  webdriver
from  selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from  webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.chrome(service = Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

time.sleep(4)

name =driver.find_element(By.NAME,"username")
name.send_keys("Admin")

password = driver.find_element(By.NAME,"password")
password.send_keys("admin123")

time.sleep(4)

Login = driver.find_element(By.XPATH,"button[normalize-space()='login']")
Login.click()

assert "OrangeHRM" in driver.title


