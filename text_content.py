from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# Navigate to url
driver.get("https://www.selenium.dev/selenium/web/linked_image.html")

# Retrieves the text of the element
text = driver.find_element(By.ID, "justanotherLink").text
print(text)