import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()


driver.get("https://trytestingthis.netlify.app/")
time.sleep(3)


print("Title:", driver.title)
print("URL:", driver.current_url)

# Navigate to another site (so back & forward works)
driver.get("https://www.google.com/")
time.sleep(3)


driver.back()
time.sleep(2)

driver.forward()
time.sleep(2)

driver.refresh()
time.sleep(2)

driver.quit()