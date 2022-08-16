import os

from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as condition
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait

url = "https://www.techlistic.com/p/selenium-practice-form.html"
image_path = os.path.join(os.getcwd(), 'js.png')
os.environ['PATH'] += r"C:\selenium-chrome-drivers\chromedriver_win32"
downloads_directory = os.path.join(os.getcwd(), "test_downloads")
options = webdriver.ChromeOptions()
download_preference = {"download.default_directory": downloads_directory}
driver_wait_in_seconds = 10
options.add_experimental_option("prefs", download_preference)

firstname = "John"
lastname = "Doe"
driver = webdriver.Chrome(options=options)
# open url and maximize window
try:
    driver.get(url)
    driver.maximize_window()
except Exception as e:
    print(e)
    driver.quit()

# assert 'Demo Sign-Up Selenium Automation Practice Form' in driver.page_source
try:
    popup = WebDriverWait(driver, driver_wait_in_seconds).until(
        condition.presence_of_element_located((By.ID, "ez-accept-all"))
    ).click()

    cookie = WebDriverWait(driver, driver_wait_in_seconds).until(
        condition.presence_of_element_located((By.ID, 'cookieChoiceDismiss'))
    ).click()
except NoSuchElementException as e:
    print(e)
    driver.quit()

# firstname input field
try:
    inp_field1 = WebDriverWait(driver, driver_wait_in_seconds).until(
        condition.presence_of_element_located((By.NAME, 'firstname'))
    )
    inp_field1.clear()
    inp_field1.send_keys(firstname, Keys.RETURN)
except NoSuchElementException as e:
    print(e)

# lastname input field
inp_field2 = WebDriverWait(driver, driver_wait_in_seconds).until(
    condition.presence_of_element_located((By.NAME, 'lastname'))
)
inp_field2.clear()
inp_field2.send_keys(lastname, Keys.RETURN)

# find and select the gender male
driver.find_element(By.ID, 'sex-0').click()

# click on the year of experience check box
driver.find_element(By.CSS_SELECTOR, "input#exp-1").click()

# entering date
date_input = driver.find_element(By.CSS_SELECTOR, "input#datepicker")
date_input.clear()
date_input.send_keys('2022-03-19')

# choosing profession
driver.find_element(By.CSS_SELECTOR, "input#profession-0").click()

# selecting tools
driver.find_element(By.CSS_SELECTOR, "input#tool-2").click()

# get continent dropdown by CSS_SELECTOR
drop_down_menu_1 = driver.find_element(By.CSS_SELECTOR, "select#continents")
# selecting dropdown
drop_1 = Select(drop_down_menu_1)
# loop through the options and select the desired one
for i in drop_1.options:
    if i.text == 'Australia':
        i.click()

# get commands dropdown
drop_down_menu_2 = driver.find_element(By.ID, 'selenium_commands')
# selecting dropdown
drop_2 = Select(drop_down_menu_2)
# loop through the options and select the one that contains 'Browser'
for j in drop_2.options:
    j.click() if 'Browser' in j.text else print("expected option not found")

try:
    image_upload = driver.find_element(By.NAME, 'photo')
    image_upload.send_keys(image_path)

except Exception as e:
    print(e)
    driver.quit()

try:
    download_file = driver.find_element(By.XPATH,
                                        "//*[@id=\"post-body-3077692503353518311\"]/div[1]/div/div/h2[2]/div[1]/div/div[28]/div[2]/div/a")
    download_file.click()
except NoSuchElementException as e:
    print(e)
    driver.quit()
