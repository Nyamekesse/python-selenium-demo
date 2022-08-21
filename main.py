import logging
import os.path
import sys
import traceback
import time


from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as condition
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait

from config import (browser, driver_wait_in_seconds, IMAGE_PATH, logs, URL)
from functions import (remove_ads, save_extracted_to_file, cookieDismiss, get_text_from_github)
from user_data import *

logger = logging.getLogger('logger')
file_handler = logging.FileHandler(os.path.join(logs, 'logs.log'))
logger.addHandler(file_handler)


def exc_handler(exctype, value, tb):
    logger.exception(''.join(traceback.format_exception(exctype, value, tb)))


sys.excepthook = exc_handler

# open url and maximize window
try:
    browser.get(URL)
    browser.maximize_window()
except Exception:
    print(f'An error occurred check {logs} for more info')
    browser.quit()

# assert 'Demo Sign-Up Selenium Automation Practice Form' in driver.page_source
try:
    if browser.find_element(By.ID, 'ez-accept-all').is_displayed():
        popup = browser.find_element(By.ID, 'ez-accept-all')
        popup.click()

except Exception:
    print(f'check {logs} for more info')

# check and click on accept cookie button
cookieDismiss()
# firstname input field
try:
    inp_field1 = WebDriverWait(browser, driver_wait_in_seconds).until(
        condition.presence_of_element_located((By.NAME, 'firstname'))
    )
    inp_field1.clear()
    inp_field1.send_keys(FIRSTNAME, Keys.RETURN)
except Exception:
    print(f'An error occurred check {logs} for more info')
    browser.quit()

# lastname input field
inp_field2 = WebDriverWait(browser, driver_wait_in_seconds).until(
    condition.presence_of_element_located((By.NAME, 'lastname'))
)
inp_field2.clear()
inp_field2.send_keys(LASTNAME, Keys.RETURN)

# find and select the gender male
browser.find_element(By.ID, 'sex-0').click()

# click on the year of experience check box
browser.find_element(By.CSS_SELECTOR, "input#exp-1").click()

# entering date
date_input = browser.find_element(By.CSS_SELECTOR, "input#datepicker")
date_input.clear()
date_input.send_keys(DATE)

# choosing profession
browser.find_element(By.CSS_SELECTOR, "input#profession-0").click()

# selecting tools
browser.find_element(By.CSS_SELECTOR, "input#tool-2").click()

# get continent dropdown by CSS_SELECTOR
continents_dropdown = browser.find_element(By.CSS_SELECTOR, "select#continents")
# selecting dropdown
continents_drop_list = Select(continents_dropdown)
# loop through the options and select the desired continent
for continent in continents_drop_list.options:
    if continent.text == CONTINENT:
        continent.click()

# get commands dropdown
commands_dropdown = browser.find_element(By.ID, 'selenium_commands')
# selecting dropdown
command_drop_list = Select(commands_dropdown)
# loop through the options and select the one that contains 'Browser'
for commands in command_drop_list.options:
    commands.click() if 'Browser' in commands.text else print('searching for target node')

try:
    image_upload = browser.find_element(By.NAME, 'photo')
    image_upload.send_keys(IMAGE_PATH)

except Exception:
    print(f'An error occurred check {logs} for more info')
    browser.quit()

try:
    download_file = browser.find_element(By.XPATH,
                                         "//*[@id=\"post-body-3077692503353518311\"]/div[1]/div/div/h2[2]/div["
                                         "1]/div/div[28]/div[2]/div/a")
    download_file.click()

except Exception:
    print(f'An error occurred check {logs} for more info')
    browser.quit()

try:
    # if driver.find_element(By.XPATH, '/html/ins').is_displayed():
    driver_5 = remove_ads(browser, "ins")
    if browser:
        click_2 = WebDriverWait(browser, 10).until(
            condition.presence_of_element_located(
                (By.XPATH, "//*[@id=\"post-body-3077692503353518311\"]/div[1]/div/div/h2[2]/div["
                           "1]/div/div[28]/div[2]/div/a")))
        click_2.click()
except Exception:
    print(f'An error occurred check {logs} for more info')
    browser.quit()

extract_text = get_text_from_github()
if len(extract_text) > 0:
    save_file = save_extracted_to_file(extract_text)
    if save_file:
        time.sleep(3)
        browser.back()
        browser.close()
        print('Done extracting information')
