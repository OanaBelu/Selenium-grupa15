from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

#initializam un browser
chrome = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
chrome.get('https://formy-project.herokuapp.com/form')

first_name_input = chrome.find_element(By.ID, "first-name")
# dupa id,dupa class name, dupa tagname,dupa name, dupa linktext, dupa partial text, dupa css selector, dupa xpath
first_name_input.send_keys("petruta")
first_name_input.clear()
first_name_input.send_keys("ioana")
last_name_input = chrome.find_element(By.ID, "last-name")
last_name_input.send_keys("morar")
sleep(5)
chrome.quit()






