from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import pytest

@pytest.mark.sanity
def test_locked_user_login():
    # Use webdriver-manager to automatically get the right ChromeDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    try:
        driver.get("https://www.saucedemo.com/")

        # Login with locked_out_user
        driver.find_element(By.ID, "user-name").send_keys("locked_out_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        time.sleep(2)  # wait for error message to appear
        error_message = driver.find_element(By.XPATH, "//h3[@data-test='error']").text
        expected_message = "Epic sadface: Sorry, this user has been locked out."

        assert error_message == expected_message, f"Expected: {expected_message}, Got: {error_message}"

    finally:
        driver.quit()



