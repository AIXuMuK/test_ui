import time
import math
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

answer = math.log(int(time.time()))

options = webdriver.ChromeOptions()
# options.add_argument("--start-maximized")
options.add_experimental_option('excludeSwitches', ['enable-logging'])
browser = webdriver.Chrome(options=options)

link = "https://stepik.org/lesson/236895/step/1"
browser.get(link)

textarea = WebDriverWait(browser, 5).until(
    EC.element_to_be_clickable((By.TAG_NAME, "textarea"))
).send_keys(str(answer))

button = WebDriverWait(browser, 5).until(
    EC.element_to_be_clickable((By.CLASS_NAME, "submit-submission"))
).click()

correct_msg = WebDriverWait(browser, 5).until(
    EC.element_to_be_clickable((By.CLASS_NAME, "smart-hints__hint"))
).text


assert correct_msg == "Correct!", "Ошибка равенства!"