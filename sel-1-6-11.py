from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "https://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, '.trollface.btn.btn-primary').click()
    browser.switch_to.window(browser.window_handles[1])
    x = int(browser.find_element(By.ID, 'input_value').text)
    browser.find_element(By.ID, 'answer').send_keys(str(math.log(abs(12*math.sin(x)))))
    browser.find_element(By.CSS_SELECTOR, '.btn.btn-primary').click()
finally:
    time.sleep(10)
    browser.quit()
