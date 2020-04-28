import os

from selenium import webdriver
import pytest


drivers = (
    'BlackBerry',
    'Chrome',
    'Edge',
    'Firefox',
    'IE',
    'Marionette',
    'Remote',
    'Safari',
    'WebKitGTK',
    'ChromiumEdge',
    'Galaxy S20'
)


def pytest_addoption(parser):
    parser.addoption('--driver',
                     action='store',
                     choices=drivers,
                     dest='drivers',
                     metavar='DRIVER',
                     help='driver to run tests against ()')
    parser.addoption('--browser-args', action='store', dest='args',
                     help='arguments to start the browser with')


@pytest.fixture(scope='function')
def login(driver):

    class Login():

        def __init__(self):
            from selenium.webdriver.common.by import By
            from selenium.common.exceptions import NoSuchElementException
            driver.get("http://127.0.0.1:8000/polls")
            try:
                driver.find_element(By.ID, "id_username").send_keys("bs-demo")
                driver.find_element(By.ID, "id_password").send_keys("hunter1234")
                driver.find_element(By.ID, "login").click()
            except NoSuchElementException:
                # If we can't find these elements then we've probably have
                # got through without needing to login
                pass

    return Login()


@pytest.fixture(scope='function')
def remote_login(remote):

    class Login():

        def __init__(self):
            from selenium.webdriver.common.by import By
            from selenium.common.exceptions import NoSuchElementException
            remote.get("http://127.0.0.1:8000/polls")
            try:
                remote.find_element(By.ID, "id_username").send_keys("bs-demo")
                remote.find_element(
                    By.ID, "id_password").send_keys("hunter1234")
                remote.find_element(By.ID, "login").click()
            except NoSuchElementException:
                # If we can't find these elements then we've probably have
                # got through without needing to login
                pass

    return Login()



@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Firefox()
    driver.get("http://127.0.0.1:8000/polls/")
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def remote(request):
    browser = request.config.getoption('drivers')
    desired_cap = {
        "build": "serial to parallel",
        "project": "Selenium Parallel Webinar",
        "browser": browser,
        "browserstack.local": "true",
        "name": "Serial to Parallel with {}".format(browser),
    }
    if browser == "Galaxy S20":
        del desired_cap['browser']
        desired_cap["device"] = "Samsung Galaxy S20"
        desired_cap["real_mobile"] = "true"
        desired_cap["os_version"] = "10.0"

    if browser == "ios":
        del desired_cap['browser']
        desired_cap["device"] = "iPhone XS"
        desired_cap["real_mobile"] = "true"

    bs_username = os.environ['BSUSERNAME']
    bs_password = os.environ['BSPASSWORD']
    if bs_username is None or bs_password is None:
        raise Exception("Username and Password env vars need setting")
    bs_endpoint = "https://{}:{}@hub-cloud.browserstack.com/wd/hub"\
        .format(bs_username, bs_password)
    driver = webdriver.Remote(
        command_executor=bs_endpoint, desired_capabilities=desired_cap)
    driver.get("http://127.0.0.1:8000/polls/")
    yield driver
    driver.quit()
