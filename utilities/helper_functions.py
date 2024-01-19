# helper_functions.py

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

def wait_for_element(driver, locator, timeout=10):
    try:
        element = WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located(locator)
        )
        return element
    except TimeoutException:
        print(f"Element with locator {locator} not found within {timeout} seconds.")
        return None

def click_element(driver, locator):
    element = wait_for_element(driver, locator)
    if element:
        element.click()

def input_text(driver, locator, text):
    element = wait_for_element(driver, locator)
    if element:
        element.clear()
        element.send_keys(text)
