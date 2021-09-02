import unittest
#import requests
from selenium import webdriver
import time

class TestAbs(unittest.TestCase):
    def test_1(self):
      link = "http://suninjuly.github.io/registration1.html"
      browser = webdriver.Chrome()
      browser.get(link)

      input1 = browser.find_element_by_css_selector("div.first_block > div.first_class > input.first")
      input1.send_keys("Ivan")
      input2 = browser.find_element_by_css_selector("div.first_block > div.second_class > input.second")
      input2.send_keys("Petrov")
      input3 = browser.find_element_by_css_selector("div.first_block > div.third_class> input.third")
      input3.send_keys("Smolensk@dd.r")

      button = browser.find_element_by_css_selector("button.btn")
      button.click()
      welcome_text_elt = browser.find_element_by_tag_name("h1")
   
      welcome_text = welcome_text_elt.text

      self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "test 1 failed")
      browser.quit()
        
    def test_2(self):
      link = "http://suninjuly.github.io/registration2.html"
      browser = webdriver.Chrome()
      browser.get(link)

      input1 = browser.find_element_by_css_selector("div.first_block > div.first_class > input.first")
      input1.send_keys("Ivan")
      input2 = browser.find_element_by_css_selector("div.first_block > div.second_class > input.second")
      input2.send_keys("Petrov")
      input3 = browser.find_element_by_css_selector("div.first_block > div.third_class> input.third")
      input3.send_keys("Smolensk@dd.r")

      button = browser.find_element_by_css_selector("button.btn")
      button.click() 
      
      welcome_text_elt = browser.find_element_by_tag_name("h1")
   
      welcome_text = welcome_text_elt.text

      self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "test 2 failed")
      browser.quit()
        
if __name__ == "__main__":
    unittest.main()