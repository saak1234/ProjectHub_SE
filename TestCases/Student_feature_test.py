# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestStudentfeaturetest():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_studentfeaturetest(self):
    # Test name: Student_feature_test
    # Step # | name | target | value
    # 1 | open | http://localhost:3000/ | 
    self.driver.get("http://localhost:3000/")
    # 2 | setWindowSize | 1296x736 | 
    self.driver.set_window_size(1296, 736)
    # 3 | click | css=.mentee-section .bg-blue-500 | 
    self.driver.find_element(By.CSS_SELECTOR, ".mentee-section .bg-blue-500").click()
    # 4 | type | id=email | 123@gmail.com
    self.driver.find_element(By.ID, "email").send_keys("123@gmail.com")
    # 5 | click | id=password | 
    self.driver.find_element(By.ID, "password").click()
    # 6 | mouseOver | css=.MuiButtonBase-root | 
    element = self.driver.find_element(By.CSS_SELECTOR, ".MuiButtonBase-root")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 7 | type | id=password | 123
    self.driver.find_element(By.ID, "password").send_keys("123")
    # 8 | click | css=.MuiButtonBase-root | 
    self.driver.find_element(By.CSS_SELECTOR, ".MuiButtonBase-root").click()
    # 9 | click | css=.bg-blue-500 | 
    self.driver.find_element(By.CSS_SELECTOR, ".bg-blue-500").click()
    # 10 | mouseOver | css=.bg-blue-500 | 
    element = self.driver.find_element(By.CSS_SELECTOR, ".bg-blue-500")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 11 | mouseOut | css=.bg-blue-500 | 
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    # 12 | click | linkText=Browse Quiz | 
    self.driver.find_element(By.LINK_TEXT, "Browse Quiz").click()
    # 13 | click | css=.bg-white:nth-child(1) .block | 
    self.driver.find_element(By.CSS_SELECTOR, ".bg-white:nth-child(1) .block").click()
    # 14 | click | css=.w-full:nth-child(1) | 
    self.driver.find_element(By.CSS_SELECTOR, ".w-full:nth-child(1)").click()
    # 15 | click | css=.mt-4 | 
    self.driver.find_element(By.CSS_SELECTOR, ".mt-4").click()
    # 16 | click | css=.w-full:nth-child(2) | 
    self.driver.find_element(By.CSS_SELECTOR, ".w-full:nth-child(2)").click()
    # 17 | click | css=.mt-4 | 
    self.driver.find_element(By.CSS_SELECTOR, ".mt-4").click()
    # 18 | click | css=.w-full:nth-child(3) | 
    self.driver.find_element(By.CSS_SELECTOR, ".w-full:nth-child(3)").click()
    # 19 | click | css=.mt-4 | 
    self.driver.find_element(By.CSS_SELECTOR, ".mt-4").click()
    # 20 | click | css=.w-full:nth-child(4) | 
    self.driver.find_element(By.CSS_SELECTOR, ".w-full:nth-child(4)").click()
    # 21 | click | css=.mt-4 | 
    self.driver.find_element(By.CSS_SELECTOR, ".mt-4").click()
    # 22 | click | css=.w-full:nth-child(1) | 
    self.driver.find_element(By.CSS_SELECTOR, ".w-full:nth-child(1)").click()
    # 23 | click | css=.mt-4 | 
    self.driver.find_element(By.CSS_SELECTOR, ".mt-4").click()
    # 24 | click | css=.px-6 | 
    self.driver.find_element(By.CSS_SELECTOR, ".px-6").click()
  