from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# Navigate to url
driver.get("https://www.selenium.dev/selenium/web/inputs.html")

# get boolean value is displayed
is_email_visible = driver.find_element(By.NAME,"email_input").is_displayed()
is_password_visible = driver.find_element(By.NAME,"password_input").is_displayed()

if is_email_visible:
    print("The email input is visible.")
else:
    print("The email input is not visible.")

# Returns true if element is enabled else returns false
button_input = driver.find_element(By.NAME, 'button_input').is_enabled()
reset_input = driver.find_element(By.NAME, 'reset_input').is_enabled()

# Returns true if element is checked else returns false
checkbox_input = driver.find_element(By.NAME, "checkbox_input").is_selected()

# Returns TagName of the element
attr = driver.find_element(By.NAME, "email_input").tag_name

# return height, width, x y coordinate referenced element
element = driver.find_element(By.NAME, "range_input")
size = element.size
location = element.location
rect = {'width': size['width'], 'height': size['height'], 'x': location['x'], 'y': location['y']}
print(rect)


# Navigate to Url
driver.get('https://www.selenium.dev/selenium/web/colorPage.html')

# Retrieves the computed style property 'color' of linktext
cssValue = driver.find_element(By.ID, "namedColor").value_of_css_property('background-color')
print(cssValue)

