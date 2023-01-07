from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()

try:
    browser.get(link)

    button = browser.find_element_by_css_selector('button.btn')
    button.click()

    new_window = browser.window_handles[-1]
    browser.switch_to.window(new_window)

    x = browser.find_element_by_id('input_value').text
    y = str(math.log(abs(12*math.sin(int(x)))))

    answ = browser.find_element_by_id('answer')
    answ.send_keys(y)

    button = browser.find_element_by_css_selector('[type="submit"]')
    button.click()

    print(browser.switch_to.alert.text)
finally:
    time.sleep(1)
    browser.quit()