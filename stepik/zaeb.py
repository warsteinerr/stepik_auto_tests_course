from selenium import  webdriver
from selenium.webdriver.common.by import By
import time
import os


try:
    link = 'http://suninjuly.github.io/file_input.html'
    browser = webdriver.Chrome()
    browser.get(link)
    name = browser.find_element(By.CSS_SELECTOR, "[placeholder='Enter first name']")
    name.send_keys('pupkin')
    surname = browser.find_element(By.CSS_SELECTOR, "[placeholder='Enter last name']")
    surname.send_keys('zalupkin')
    mail = browser.find_element(By.CSS_SELECTOR, "[placeholder='Enter email']")
    mail.send_keys('mail@mail.ru')
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    input = browser.find_element(By.ID, 'file')
    input.send_keys(file_path)
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()