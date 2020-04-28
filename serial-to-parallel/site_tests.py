from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


def test_login(driver):
    driver.find_element(By.ID, "id_username").send_keys("bs-demo")
    driver.find_element(By.ID, "id_password").send_keys("hunter1234")
    driver.find_element(By.ID, "login").click()
    assert len(driver.find_elements(By.ID, "id_username")) == 0


def test_first_question(driver, login):
    driver.get("http://127.0.0.1:8000/polls/1/")
    driver.find_element(By.ID, "choice1").click()
    driver.find_element(By.ID, "vote").click()
    WebDriverWait(driver, 10).until(
        lambda x: x.find_element(By.ID, "vote_again"))
    el = driver.find_element(
        By.CSS_SELECTOR, "body > ul:nth-child(3) > li:nth-child(1)")
    assert "votes" in el.text


def test_second_question(driver, login):
    driver.get("http://127.0.0.1:8000/polls/2/")
    driver.find_element(By.ID, "choice1").click()
    driver.find_element(By.ID, "vote").click()
    WebDriverWait(driver, 10).until(
        lambda x: x.find_element(By.ID, "vote_again"))
    el = driver.find_element(
        By.CSS_SELECTOR, "body > ul:nth-child(3) > li:nth-child(1)")
    assert "votes" in el.text
