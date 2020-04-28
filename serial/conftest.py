from selenium import webdriver
import pytest


@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Firefox()
    driver.get("http://127.0.0.1:8000/polls/")
    yield driver
    driver.quit()
