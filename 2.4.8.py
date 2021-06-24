import math
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
browser = webdriver.Chrome(options=options)

link = "http://suninjuly.github.io/explicit_wait2.html"

browser.get(link)

price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))

button = browser.find_element(By.ID, "book").click()

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

input_answer = browser.find_element_by_id("answer")
input_value = browser.find_element_by_id("input_value")
btn = browser.find_element_by_id("solve")

x_element = input_value
x = x_element.text
y = calc(x)

browser.execute_script("return arguments[0].scrollIntoView(true);", btn)
input_answer.send_keys(y)

btn.click()