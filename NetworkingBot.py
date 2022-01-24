from sqlite3 import connect
from selenium import webdriver
import time
import os

dir = os.getcwd()
dir = dir.replace(os.sep, "/")

# Make sure that the webdriver is the same version and the same OS . This on is version 97.0.4692.71 for Windows.
# You can get all versions at: https://chromedriver.storage.googleapis.com/index.html

### MAKE SURE YOU ARE ADDING THE DRIVER TO THE SAME DIRECTORY AS THE CODE ####
driver = webdriver.Chrome(
    dir+"/chromedriver.exe")
driver.get(
    "https://www.linkedin.com/login")
time.sleep(2)

username = driver.find_element_by_xpath("//input[@name='session_key']")
password = driver.find_element_by_xpath("//input[@name='session_password']")

username.send_keys("ADD YOUR USER NAME HERE")
password.send_keys("ADD YOUR PASSWORD HERE")


submit = driver.find_element_by_xpath("//button[@type='submit']").click()
time.sleep(2)

# Select the amount pages
pages = 100

for i in range(pages):

    # URL for the people tab when you make an empty search
    # Note: I used only 1st and 2nd connections

    url = "https://www.linkedin.com/search/results/people/?network=%5B%22F%22%2C%22S%22%5D&origin=FACETED_SEARCH&page=" + \
        str(i+1)
    driver.get(url)
    time.sleep(2)
    all_buttons = driver.find_elements_by_tag_name("button")
    connect_buttons = [btn for btn in all_buttons if btn.text == "Connect"]
    for btn in connect_buttons:
        driver.execute_script("arguments[0].click();", btn)
        time.sleep(2)
        send = driver.find_element_by_xpath("//button[@aria-label='Send now']")
        driver.execute_script("arguments[0].click();", send)
        close = driver.find_element_by_xpath("//button[@aria-label='Dismiss']")
        driver.execute_script("arguments[0].click();", close)
        time.sleep(2)

# Create an environment in Anaconda command using: conda create --name ENV_NAME
# Activate environment command using: activate ENV_NAME
# Make sure to install selenium on the enviroment using (runs only once): pip install selenium
# After that you can run the command: python NetworkingBot.py
