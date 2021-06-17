import time
import math
from selenium import webdriver

browser = webdriver.Chrome()

link = "http://suninjuly.github.io/math.html"

browser.get(link)

input_answer = browser.find_element_by_id("answer")
input_value = browser.find_element_by_id("input_value")
robot_checkbox = browser.find_element_by_id("robotCheckbox")
robot_rule = browser.find_element_by_id("robotsRule")
btn = browser.find_element_by_tag_name("button")

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

x_element = input_value
x = x_element.text
y = calc(x)

input_answer.send_keys(y)
robot_checkbox.click()
robot_rule.click()
btn.click()


