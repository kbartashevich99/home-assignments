import os
import time
from selenium import webdriver

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    fn = browser.find_element_by_css_selector('[name="firstname"]')
    fn.send_keys("Kate")
    ln = browser.find_element_by_css_selector('[name="lastname"]')
    ln.send_keys("Smith")
    email = browser.find_element_by_css_selector('[name="email"]')
    email.send_keys("aveiro@gmail.com")

    current_directory = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_directory, 'text.txt')

    file = browser.find_element_by_css_selector('[type="file"]')
    file.send_keys(file_path)

    button = browser.find_element_by_css_selector("button")
    button.click()
finally:
    time.sleep(10)
    browser.quit()

