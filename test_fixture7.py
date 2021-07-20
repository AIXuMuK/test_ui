import pytest
import time
import math
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
# options.add_argument("--start-maximized")
options.add_experimental_option('excludeSwitches', ['enable-logging'])

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('url_test', ["https://stepik.org/lesson/236904/step/1",
                                 "https://stepik.org/lesson/236905/step/1"])
def test_ufo_feedback(browser, url_test):
    link = f"{url_test}"
    answer = math.log(int(time.time()))
    browser.get(link)

    WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.TAG_NAME, "textarea"))
    ).send_keys(str(answer))

    WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "submit-submission"))
    ).click()

    correct_msg = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "smart-hints__hint"))
    ).text


    assert correct_msg == "Correct!", "Ошибка равенства!"
    