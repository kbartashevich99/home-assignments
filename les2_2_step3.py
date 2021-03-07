from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    num1_el = browser.find_element_by_css_selector("#num1")
    num1 = int(num1_el.text)
    num2_el = browser.find_element_by_css_selector("#num2")
    num2 = int(num2_el.text)
    summa = str(num1 + num2)
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(summa)
    browser.find_element_by_css_selector("button").click()

finally:
    time.sleep(10)
    browser.quit()
