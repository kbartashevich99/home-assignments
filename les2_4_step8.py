from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = 'http://suninjuly.github.io/explicit_wait2.html'
    browser = webdriver.Chrome()
    browser.get(link)

    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), '$100')
    )

    button = browser.find_element_by_css_selector("#book")
    button.click()

    input_elt = browser.find_element_by_css_selector("#input_value")
    input = input_elt.text
    output = browser.find_element_by_css_selector("#answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", output)
    output.send_keys(calc(input))
    button2 = browser.find_element_by_css_selector("#solve")
    button2.click()

finally:
    time.sleep(10)
    browser.quit()
