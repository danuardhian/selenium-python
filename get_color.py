from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# Navigate to Url
driver.get('https://www.selenium.dev/selenium/web/colorPage.html')

# Retrieves the computed style property 'color' of linktext
cssValue = driver.find_element(By.ID, "hexShort").value_of_css_property('background-color')
print(cssValue)