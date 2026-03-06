from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Setup WebDriver
driver = webdriver.Chrome()
driver.maximize_window()

# Practice form page (update if needed)
driver.get("https://testautomationpractice.blogspot.com/")  # Example practice site :contentReference[oaicite:1]{index=1}

wait = WebDriverWait(driver, 10)

# ----------------------------
# Select Radio Button
# ----------------------------

# Wait for radio button (example: "Male")
radio_male = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@type='radio' and @value='Male']")))
radio_male.click()

# Verify selection
print("Radio 'Male' selected:", radio_male.is_selected())

# ----------------------------
# Select Multiple Checkboxes
# ----------------------------

# Example: Days checkboxes (Sunday, Monday)
checkbox_sunday = driver.find_element(By.XPATH, "//input[@type='checkbox' and @value='Sunday']")
checkbox_monday = driver.find_element(By.XPATH, "//input[@type='checkbox' and @value='Monday']")

checkbox_sunday.click()
checkbox_monday.click()

print("Sunday checkbox selected:", checkbox_sunday.is_selected())
print("Monday checkbox selected:", checkbox_monday.is_selected())

time.sleep(2)

driver.quit()