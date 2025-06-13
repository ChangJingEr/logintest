import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@pytest.mark.parametrize(
    "username,password,expect_result",
    [
        ("standard_user","secret_sauce","Products"),             #TC001
        ("","secret_sauce","Username is required"),              #TC002
        ("standard_user","","Password is required"),             #TC003
        ("","","Username is required")                          #TC004
    ]
)

def test_login(username,password,expect_result):
    driver=webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")

    try:
        driver.find_element(By.ID,"user-name").clear()
        driver.find_element(By.ID,"user-name").send_keys(username)

        driver.find_element(By.ID,"password").clear()
        driver.find_element(By.ID,"password").send_keys(password)

        driver.find_element(By.ID,"login-button").click()

        time.sleep(3)

        
        

        if expect_result=="Products":
            loginmessage=driver.find_element(By.CLASS_NAME,"title").text
            assert "Products" in loginmessage
        elif expect_result=="Username is required":
            message=driver.find_element(By.CSS_SELECTOR,"[data-test='error']").text
            assert "Username is required" in message
        elif expect_result=="Password is required":
            message=driver.find_element(By.CSS_SELECTOR,"[data-test='error']").text
            assert "Password is required" in message
        elif expect_result=="Username is required":
            message=driver.find_element(By.CSS_SELECTOR,"[data-test='error']").text
            assert "Username is required" in message
        else:
            pytest.fail("未知的預期結果代碼")

    finally:
        driver.quit()


