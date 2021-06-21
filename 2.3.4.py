import time
import math
from selenium import webdriver

browser = webdriver.Chrome()

link = "http://suninjuly.github.io/redirect_accept.html"

browser.get(link)

btn = browser.find_element_by_tag_name("button")
btn.click()

new_window = browser.window_handles[1]
browser.switch_to.window(new_window)

btn2 = browser.find_element_by_tag_name("button")
input_answer = browser.find_element_by_id("answer")
input_value = browser.find_element_by_id("input_value")

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

x_element = input_value
x = x_element.text
y = calc(x)

input_answer.send_keys(y)

btn2.click()

