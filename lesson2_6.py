import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

LINK = 'http://SunInJuly.github.io/execute_script.html'


def calc(x: float | int) -> str:
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = None
try:
    browser = webdriver.Firefox()
    browser.get(LINK)

    x_value = browser.find_element(By.ID, 'input_value').text
    answer = calc(x_value)

    text_field = browser.find_element(By.ID, 'answer')
    browser.execute_script("return arguments[0].scrollIntoView(true);",
                           text_field)
    text_field.send_keys(answer)

    checkbox = browser.find_element(By.ID, 'robotCheckbox')
    browser.execute_script("return arguments[0].scrollIntoView(true);",
                           checkbox)
    checkbox.click()

    radio_button = browser.find_element(By.ID, 'robotsRule')
    browser.execute_script("return arguments[0].scrollIntoView(true);",
                           radio_button)
    radio_button.click()

    submit_button = browser.find_element(By.TAG_NAME, 'button')
    browser.execute_script("return arguments[0].scrollIntoView(true);",
                           submit_button)
    submit_button.click()

finally:
    if browser is not None:
        time.sleep(10)
        browser.quit()
