import os
import time
import math
from selenium import webdriver

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_css_selector('button')
    button.click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    input = browser.find_element_by_css_selector("#input_value")
    input_number = input.text
    output = browser.find_element_by_css_selector("#answer")
    output.send_keys(calc(input_number))

    button2 = browser.find_element_by_css_selector("button")
    button2.click()

finally:
    time.sleep(10)
    browser.quit()

