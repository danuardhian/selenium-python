from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("https://www.saucedemo.com/")

username = driver.find_element(By.ID,"user-name")
password = driver.find_element(By.ID, "password")

# input username
username.clear
username.send_keys("standard_user")

# input password
password.clear
password.send_keys("secret_sauce")

# click login button
button = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "login-button"))
    )
button.click()

# assert
element = driver.find_element(By.ID, "inventory_container")

# Check if the element is displayed
if element.is_displayed():
    print("Element is displayed.")
else:
    print("Element is not displayed.")

driver.quit()