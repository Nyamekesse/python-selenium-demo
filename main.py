import os

from bs4 import BeautifulSoup
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
downloads_directory = os.path.join(os.getcwd(), "saved_files")
options = webdriver.ChromeOptions()

driver_wait_in_seconds = 10

firstname = "John"
lastname = "Doe"
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(driver_wait_in_seconds)


def kill(driver, selector: str):
    i = 0
    soup = BeautifulSoup(driver.page_source, 'html.parser')  # Parsing content using beautifulsoup
    while soup.find(selector):
        # print(soup.find(selector))
        js = """
            var element = document.querySelector(""" + "'" + selector + "'" + """);
            if (element)
                element.parentNode.removeChild(element);
            """
        driver.execute_script(js)
        soup = BeautifulSoup(driver.page_source, 'html.parser')  # Parsing content using beautifulsoup
        i += 1
        # print('Removed tag with selector ' + "'" + selector + "'" + ' with nr: ', i)
    print('Removed ' + str(i) + ' tags with the selector ' + "'" + selector + "'" + " and all it's children tags.")
    return driver


def cookieDismiss():
    try:
        if driver.find_element(By.ID, 'cookieChoiceDismiss').is_displayed():
            cookie = driver.find_element(By.ID, 'cookieChoiceDismiss')
            cookie.click()

    except NoSuchElementException as e:
        print(e)


def checker():
    try:
        if driver.find_element(By.ID, 'ad_position_box').is_displayed():
            print('found')
        else:
            print('not found')
    except Exception as e:
        print(e)


# open url and maximize window
try:
    driver.get(url)
    driver.maximize_window()
except Exception as e:
    print(e)
    driver.quit()

# assert 'Demo Sign-Up Selenium Automation Practice Form' in driver.page_source
try:
    if driver.find_element(By.ID, 'ez-accept-all').is_displayed():
        popup = driver.find_element(By.ID, 'ez-accept-all')
        popup.click()

except NoSuchElementException as e:
    print(e)

cookieDismiss()
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
    j.click() if 'Browser' in j.text else print('searching for target node')

try:
    image_upload = driver.find_element(By.NAME, 'photo')
    image_upload.send_keys(image_path)

except Exception as e:
    print(e)
    driver.quit()

try:
    download_file = driver.find_element(By.XPATH,
                                        "//*[@id=\"post-body-3077692503353518311\"]/div[1]/div/div/h2[2]/div["
                                        "1]/div/div[28]/div[2]/div/a")
    download_file.click()

except NoSuchElementException as e:
    print(e)
    driver.quit()

try:
    # if driver.find_element(By.XPATH, '/html/ins').is_displayed():
    driver_5 = kill(driver, "ins")
    if driver:
        click_2 = WebDriverWait(driver, 10).until(
            condition.presence_of_element_located(
                (By.XPATH, "//*[@id=\"post-body-3077692503353518311\"]/div[1]/div/div/h2[2]/div["
                           "1]/div/div[28]/div[2]/div/a")))
        click_2.click()
except Exception as e:
    print(e)


def opened_github_window():
    try:
        elem = []
        if 'GitHub' in driver.title:
            for my_text_elem in WebDriverWait(driver, 5).until(
                    condition.visibility_of_all_elements_located((By.CSS_SELECTOR,
                                                                  "#repo-content-pjax-container > div > div > div.Box.mt-3.position-relative > div.Box-body.p-0.blob-wrapper.data.type-yaml.gist-border-0 > div > table > tbody > tr"))):
                elem.append(my_text_elem)
            for text in elem:
                print(text.text)
    except Exception as e:
        print(e)


opened_github_window()
