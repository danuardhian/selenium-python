# page_objects/login_page.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.username_locator = (By.ID, 'user-name')
        self.password_locator = (By.ID, 'password')
        self.login_button_locator = (By.XPATH, '//*[@id="login-button"]')

    def login(self, username, password):
        username_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.username_locator)
        )
        username_input.send_keys(username)

        password_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.password_locator)
        )
        password_input.send_keys(password)

        login_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.login_button_locator)
        )
        login_button.click()
