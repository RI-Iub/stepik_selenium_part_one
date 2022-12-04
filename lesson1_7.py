import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

LINK = 'http://suninjuly.github.io/get_attribute.html'


def calc(x: float | int) -> str:
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = None
try:
    browser = webdriver.Firefox()
    browser.get(LINK)

    x_value = browser.find_element(By.ID, 'treasure').get_attribute('valuex')
    answer = calc(x_value)

    browser.find_element(By.ID, 'answer').send_keys(answer)
    browser.find_element(By.ID, 'robotCheckbox').click()
    browser.find_element(By.ID, 'robotsRule').click()
    browser.find_element(By.TAG_NAME, 'button').click()

finally:
    if browser is not None:
        time.sleep(10)
        browser.quit()
