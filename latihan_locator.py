from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.selenium.dev/selenium/web/web-form.html")

driver.find_element(By.CLASS_NAME,"display-6")
driver.find_element(By.CSS_SELECTOR,"#my-text-id")
driver.find_element(By.ID,"my-text-id")
driver.find_element(By.NAME,"my-text")
driver.find_element(By.LINK_TEXT,"Return to index")
driver.find_element(By.PARTIAL_LINK_TEXT,"to index")
driver.find_element(By.TAG_NAME,"a")
driver.find_element(By.XPATH,"/html/body/main/div/form/div/div[1]/label[2]/input") 
