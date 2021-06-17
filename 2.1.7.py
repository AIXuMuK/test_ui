import math
from selenium import webdriver

browser = webdriver.Chrome()

link = "http://suninjuly.github.io/get_attribute.html"

browser.get(link)

input_answer = browser.find_element_by_id("answer")
input_value = browser.find_element_by_id("treasure")
robot_checkbox = browser.find_element_by_id("robotCheckbox")
robot_rule = browser.find_element_by_id("robotsRule")
btn = browser.find_element_by_tag_name("button")

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

x_element = input_value
x = x_element.get_attribute("valuex")
y = calc(x)

input_answer.send_keys(y)
robot_checkbox.click()
robot_rule.click()
btn.click()

# people_radio = browser.find_element_by_id("peopleRule")

# people_checked = people_radio.get_attribute("checked")
# print("value of people radio: ", people_checked)
# assert people_checked is not None, "People radio is not selected by default"

