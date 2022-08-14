import os

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait

url = "https://www.techlistic.com/p/selenium-practice-form.html"
image_path = r"C:\Users\LordPhoenix\Pictures\js.png"
os.environ['PATH'] += r"C:\selenium-chrome-drivers\chromedriver_win32"

driver = webdriver.Chrome()
driver.get(url)

# assert 'Demo Sign-Up Selenium Automation Practice Form' in driver.page_source
try:
    popup = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.ID, "ez-accept-all"))
    ).click()

    cookie = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.ID, 'cookieChoiceDismiss'))
    ).click()
except NoSuchElementException as e:
    print(e)
    pass

# firstname input field
inp_field1 = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.NAME, 'firstname'))
)
inp_field1.clear()
inp_field1.send_keys('Samuel', Keys.RETURN)

# lastname input field
inp_field2 = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.NAME, 'lastname'))
)
inp_field2.clear()
inp_field2.send_keys('Nyamekesse', Keys.RETURN)

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
        break
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

except:
    print("something went wrong")
