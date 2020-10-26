# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 09:10:35 2020

@author: HP
"""
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


def search_term(text):
    options = webdriver.ChromeOptions() 
    driver = webdriver.Chrome(executable_path="C:\\bin\\chromedriver.exe", options=options)
    driver.set_window_size(1120, 1000)
    url= 'https://www.google.com/'
    driver.get(url)
    somthing=driver.find_elements_by_class_name("gsfi")
    somthing[1].send_keys(text)
    somthing[1].send_keys(Keys.ENTER)
    time.sleep(20)
    driver.quit()

def search_youtube(text):
    options = webdriver.ChromeOptions() 
    driver = webdriver.Chrome(executable_path="C:\\bin\\chromedriver.exe", options=options)
    driver.set_window_size(1120, 1000)
    url= 'https://www.youtube.com/results?search_query='
    driver.get(url+text)
    link=driver.find_element_by_tag_name("img")
    link.click()
     
def search_website(text):
    options = webdriver.ChromeOptions() 
    driver = webdriver.Chrome(executable_path="C:\\bin\\chromedriver.exe", options=options)
    driver.set_window_size(1120, 1000)
    url= 'https://www.google.com/'
    driver.get(url)
    somthing=driver.find_elements_by_class_name("gsfi")
    somthing[1].send_keys(text)
    somthing[1].send_keys(Keys.ENTER)
    link=driver.find_element_by_tag_name("cite")
    link.click()
    






