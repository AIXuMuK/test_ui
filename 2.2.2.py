import os
from selenium import webdriver

browser = webdriver.Chrome()

link = "http://suninjuly.github.io/file_input.html"

browser.get(link)

first_name = browser.find_element_by_name("firstname")
last_name = browser.find_element_by_name("lastname")
e_mail = browser.find_element_by_name("email")
file_input = browser.find_element_by_id("file")
btn = browser.find_element_by_tag_name("button")

first_name.send_keys("Ivan")
last_name.send_keys("Ivanov")
e_mail.send_keys("Ivanov@mail.ru")

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'file.txt')
file_input.send_keys(file_path)

btn.click()