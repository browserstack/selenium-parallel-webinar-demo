from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


def test_login(remote):
    remote.find_element(By.ID, "id_username").send_keys("bs-demo")
    remote.find_element(By.ID, "id_password").send_keys("hunter1234")
    remote.find_element(By.ID, "login").click()
    assert len(remote.find_elements(By.ID, "id_username")) == 0


def test_first_question_first_choice(remote, remote_login):
    remote.get("http://bs-local.com:8000/polls/1/")
    remote.find_element(By.ID, "choice1").click()
    remote.find_element(By.ID, "vote").click()
    WebDriverWait(remote, 10).until(
        lambda x: x.find_element(By.ID, "vote_again"))
    el = remote.find_element(
        By.CSS_SELECTOR, "body > ul:nth-child(3) > li:nth-child(1)")
    import time
    time.sleep(3)
    assert "votes" in el.text


def test_first_question_second_choice(remote, remote_login):
    remote.get("http://bs-local.com:8000/polls/1/")
    remote.find_element(By.ID, "choice2").click()
    remote.find_element(By.ID, "vote").click()
    WebDriverWait(remote, 10).until(
        lambda x: x.find_element(By.ID, "vote_again"))
    el = remote.find_element(
        By.CSS_SELECTOR, "body > ul:nth-child(3) > li:nth-child(1)")
    import time
    time.sleep(3)
    assert "votes" in el.text


def test_second_question(remote, remote_login):
    remote.get("http://bs-local.com:8000/polls/2/")
    remote.find_element(By.ID, "choice1").click()
    remote.find_element(By.ID, "vote").click()
    WebDriverWait(remote, 10).until(
        lambda x: x.find_element(By.ID, "vote_again"))
    el = remote.find_element(
        By.CSS_SELECTOR, "body > ul:nth-child(3) > li:nth-child(1)")
    import time
    time.sleep(3)
    assert "votes" in el.text


def test_second_question_second_choice(remote, remote_login):
    remote.get("http://bs-local.com:8000/polls/2/")
    remote.find_element(By.ID, "choice2").click()
    remote.find_element(By.ID, "vote").click()
    WebDriverWait(remote, 10).until(
        lambda x: x.find_element(By.ID, "vote_again"))
    el = remote.find_element(
        By.CSS_SELECTOR, "body > ul:nth-child(3) > li:nth-child(1)")
    import time
    time.sleep(3)
    assert "votes" in el.text
