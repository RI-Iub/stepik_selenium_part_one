import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


LINK = 'https://suninjuly.github.io/math.html'


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Firefox()
    browser.get(LINK)

    x_element = browser.find_element(By.ID, 'input_value')
    x_value = x_element.text

    answer: str = calc(x_value)

    browser.find_element(By.ID, 'answer').send_keys(answer)

    browser.find_element(By.ID, 'robotCheckbox').click()

    browser.find_element(By.ID, 'robotsRule').click()

    browser.find_element(By.CSS_SELECTOR, 'button').click()

finally:
    time.sleep(10)
    browser.quit()
