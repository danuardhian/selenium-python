from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# Navigate to url
driver.get("https://www.selenium.dev/selenium/web/inputs.html")

# get boolean value is displayed
is_email_visible = driver.find_element(By.NAME,"email_input").is_displayed()
is_password_visible = driver.find_element(By.NAME,"password_input").is_displayed()

# Returns true if element is enabled else returns false
button_input = driver.find_element(By.NAME, 'button_input').is_enabled()
reset_input = driver.find_element(By.NAME, 'reset_input').is_enabled()

# Returns true if element is checked else returns false
checkbox_input = driver.find_element(By.NAME, "checkbox_input").is_selected()
radio_input = driver.find_element(By.XPATH, "/html/body/form/input[12]").is_selected()