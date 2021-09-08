import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default=None,
                     help="Choose browser: chrome or firefox or ie11")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        options = Options()
        options.add_argument("--start-maximized")
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        options.add_experimental_option('prefs', {'intl.accept_languages': "en"})
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", "ru, en")
        browser = webdriver.Firefox(firefox_profile=fp)
    elif browser_name == "ie11":
        print("\nstart ie11 browser for test..")
        browser = webdriver.Ie()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox or ie11")
    yield browser
    print("\nquit browser..")
    browser.quit()