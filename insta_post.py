from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import datetime
import time

"""
TODO:
Create functions that parse config.txt file in order to keep passwords private
Change source of memes
Finish insta_post
"""

browser = webdriver.Safari()

browser.get("https://www.instagram.com/accounts/login/")

""" TODO """
username = 'username'
password = 'password'

time.sleep(3)

browser.find_element_by_xpath("//input[@name='username']").send_keys(username)
browser.find_element_by_xpath("//input[@name='password']").send_keys(password)
browser.find_element_by_xpath("//button[contains(.,'Log in')]").click()
time.sleep(3)
browser.find_element_by_xpath("//button[contains(.,'Save Info')]").click()
time.sleep(3)
browser.find_element_by_xpath("//button[contains(.,'Turn On')]").click()

print("Succesfully logged in\n")