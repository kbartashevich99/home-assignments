import os
import time
import math
from selenium import webdriver

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_css_selector('[type="submit"]')
    button.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    x_elt = browser.find_element_by_css_selector("#input_value")
    x = x_elt.text
    y = calc(x)
    output = browser.find_element_by_css_selector("#answer")
    output.send_keys(y)
    button2 = browser.find_element_by_css_selector("button")
    button2.click()

finally:
    time.sleep(10)
    browser.quit()

