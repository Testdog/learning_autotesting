import pytest
from selenium import webdriver
import time
import math

#link = ["https://stepik.org/lesson/236895/step/1", "https://stepik.org/lesson/236896/step/1", "https://stepik.org/lesson/236897/step/1", "https://stepik.org/lesson/236898/step/1", "https://stepik.org/lesson/236899/step/1", "https://stepik.org/lesson/236903/step/1", "https://stepik.org/lesson/236904/step/1", "https://stepik.org/lesson/236905/step/1"

@pytest.fixture(scope="function")
def browser():
    print ("\n start browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(1)
    yield browser
    print ("\n quit browser..")
    browser.quit()

    
@pytest.mark.parametrize('link', ["https://stepik.org/lesson/236895/step/1", "https://stepik.org/lesson/236896/step/1", "https://stepik.org/lesson/236897/step/1", "https://stepik.org/lesson/236898/step/1", "https://stepik.org/lesson/236899/step/1", "https://stepik.org/lesson/236903/step/1", "https://stepik.org/lesson/236904/step/1", "https://stepik.org/lesson/236905/step/1"] )
def test_guest_should_see_login_link(browser, link):
    links = {link}
    browser.get(links)
    browser.implicitly_wait(5)
    inp = browser.find_element_by_id("#ember94.ember")
    answer = math.log(int(time.time()-27.4))
    inp.send_key(answer)
    button = browser.find_element_by_css_selector("button.submit")
    button.click()
    browser.implicitly_wait(5)
    idcj = browser.find_element_by_css_selector("pre.smart")
    stt = idcj.get_attribute("value")
    assert stt == "Correct!", "ok"