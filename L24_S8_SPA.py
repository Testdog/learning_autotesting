from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))



browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")
wait = WebDriverWait(browser, 15)

try: 

    element = wait.until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))

    #elem = driver.find_element_by_class_name("myclassname")
    #print (element.text)



    print("1000")

    button = browser.find_element_by_id("book")
    button.click()
    browser.execute_script("window.scrollBy(0, 100);")
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)
    button1 = browser.find_element_by_id("solve")
    button1.click()

finally:
    
    time.sleep(30)
    
    browser.quit()