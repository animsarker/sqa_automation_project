import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

@pytest.mark.sanity
def test_login_invalid_password():
    # Setup Chrome
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    
    try:
        driver.get("https://www.saucedemo.com/")  # Example login page

        # Enter valid username
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        # Enter invalid password
        driver.find_element(By.ID, "password").send_keys("wrong_password")
        driver.find_element(By.ID, "login-button").click()

        # Check error message
        error_text = driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']").text
        assert "Epic sadface" in error_text

    finally:
        driver.quit()
