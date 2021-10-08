import os
from pathlib import Path
import time
import unittest
import sys
from telnetlib import EC

import selenium
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

username = "nam.ngh94"  # Replace the username
access_key = "ejo6MCaviJiCqzYNwhY5rGxuwsKGjkdDlMEzhufOHzXlr5JbK0"  # Replace the access key


class FirstSampleTest(unittest.TestCase):
    # Generate capabilites from here: https://www.lambdatest.com/capabilities-generator/
    # setUp runs before each test case and
    def setUp(self):
        desired_caps = {
            "build": 'PyunitTest sample build',  # Change your build name here
            "name": 'Py-unittest',  # Change your test name here
            "platform": 'Windows 10',  # Change your OS version here
            "browserName": 'Chrome',  # Change your browser here
            "version": '92.0',  # Change your browser version here
            "resolution": '1024x768',  # Change your resolution here
            "console": 'true',  # Enable or disable console logs
            "network": 'true'  # Enable or disable network logs
        }
        #self.driver = webdriver.Remote(
            #command_executor="https://{}:{}@hub.lambdatest.com/wd/hub".format(username, access_key),
            #desired_capabilities=desired_caps)
        self.driver = webdriver.Chrome()

    # tearDown runs after each test case
    def tearDown(self):
        self.driver.quit()

    # """ You can write the test cases here """
    def test_unit_user_should_able_to_add_item(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("https://test.bbcincorp.com/make-payment")

        # login
        your_name = driver.find_element_by_xpath("//input[@name='your-name']").send_keys('Khanh Do')
        company = driver.find_element_by_xpath("//input[@name='your-order']").send_keys('KMS COMPANY')
        email = driver.find_element_by_xpath("//input[@name='your-email']").send_keys('khanhdo@gmail.com')
        note = driver.find_element_by_xpath("//textarea[@name='your-message']").send_keys('abcde')
        amount = driver.find_element_by_xpath("//input[@name='amount']").send_keys('500')

        # payment
        driver.find_element_by_xpath("//input[@value='New Incorporation']").click()
        driver.find_element_by_xpath("//input[@value='Banking Service']").click()
        credit_card = driver.find_element_by_xpath("//div[@class='form-group payment-type']//input[@value='Card']")
        driver.execute_script("arguments[0].click();", credit_card)
        driver.find_element_by_id('make-payment-submit').click()
        time.sleep(1)

        # Enter info to the Credit card
        frame_01 = driver.find_element_by_xpath("(//iframe[@allow='payment *'])[1]")
        driver.switch_to.frame(frame_01)

        driver.find_element_by_xpath("//form[@class='ElementsApp is-empty']//input[@name='cardnumber']").send_keys(
            '5555555555554444')
        driver.find_element_by_xpath("//input[@name='exp-date']").send_keys('1221')
        driver.find_element_by_xpath("//input[@name='cvc']").send_keys('127')
        driver.find_element_by_xpath("//input[@name='postal']").send_keys('70000')
        driver.switch_to.default_content()

        # pay button
        driver.find_element_by_xpath("//button[@id='make-paymentStripe-submit']").submit()
        time.sleep(5)
        title_success = driver.find_element_by_xpath("//h1[text()='Successful Payment']")
        assert 'Successful Payment' == title_success.text


if __name__ == "__main__":
    unittest.main()
