import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager


class Test_Practice_Page:

    def test_complete_practice_page(self):

        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://rahulshettyacademy.com/AutomationPractice/")
        driver.maximize_window()
        driver.implicitly_wait(5)

        wait = WebDriverWait(driver, 10)

        # =====================================================
        # 1️⃣ SCROLL DOWN
        # =====================================================

        driver.execute_script("window.scrollBy(0,600);")
        time.sleep(1)

        # =====================================================
        # 2️⃣ MOUSE HOVER
        # =====================================================

        hover_button = driver.find_element(By.ID, "mousehover")
        actions = ActionChains(driver)
        actions.move_to_element(hover_button).perform()
        time.sleep(1)

        # Click Top option after hover
        driver.find_element(By.LINK_TEXT, "Top").click()
        time.sleep(1)

        # =====================================================
        # 3️⃣ SWITCH WINDOW
        # =====================================================

        parent_window = driver.current_window_handle
        driver.find_element(By.ID, "openwindow").click()

        wait.until(lambda d: len(d.window_handles) > 1)

        for window in driver.window_handles:
            if window != parent_window:
                driver.switch_to.window(window)
                break

        driver.close()
        driver.switch_to.window(parent_window)

        # =====================================================
        # 4️⃣ SWITCH TAB
        # =====================================================

        driver.find_element(By.ID, "opentab").click()

        wait.until(lambda d: len(d.window_handles) > 1)

        for window in driver.window_handles:
            if window != parent_window:
                driver.switch_to.window(window)
                break

        driver.close()
        driver.switch_to.window(parent_window)

        # =====================================================
        # 5️⃣ HANDLE ALERT
        # =====================================================

        driver.find_element(By.ID, "name").send_keys("Muskan")
        driver.find_element(By.ID, "alertbtn").click()

        alert = driver.switch_to.alert
        assert "Muskan" in alert.text
        alert.accept()

        # =====================================================
        # 6️⃣ FIXED HEADER TABLE - CHENNAI ROW
        # =====================================================

        driver.execute_script("window.scrollBy(0,800);")
        time.sleep(1)

        fixed_rows = driver.find_elements(
            By.XPATH,
            "//div[@class='tableFixHead']//tbody/tr"
        )

        chennai_found = False

        for row in fixed_rows:
            city = row.find_element(By.XPATH, "./td[3]").text
            if city == "Chennai":
                amount = row.find_element(By.XPATH, "./td[4]").text
                assert int(amount) > 0
                chennai_found = True

        assert chennai_found

        # =====================================================
        # 7️⃣ WEB TABLE - ADVANCED SELENIUM COURSE ROW
        # =====================================================

        driver.execute_script("window.scrollBy(0,400);")
        time.sleep(1)

        course_rows = driver.find_elements(
            By.XPATH,
            "//table[@name='courses']//tbody/tr"
        )

        target_course = "Advanced Selenium Framework Pageobject, TestNG, Maven, Jenkins,C"
        course_found = False

        for row in course_rows:
            columns = row.find_elements(By.TAG_NAME, "td")

            if len(columns) > 0 and columns[1].text == target_course:
                instructor = columns[0].text
                price = columns[2].text

                assert instructor == "Rahul Shetty"
                assert price == "20"
                course_found = True
                break

        assert course_found

        time.sleep(2)
        driver.quit()