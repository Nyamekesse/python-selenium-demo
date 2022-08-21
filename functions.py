from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as condition
from selenium.common.exceptions import *
import os
from config import (browser, driver_wait_in_seconds, downloads_directory)


def remove_ads(driver, selector: str):
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
        if browser.find_element(By.ID, 'cookieChoiceDismiss').is_displayed():
            cookie = browser.find_element(By.ID, 'cookieChoiceDismiss')
            cookie.click()

    except NoSuchElementException as e:
        print(e)


def get_text_from_github():
    try:
        elem = []
        if 'GitHub' in browser.title:
            for tags in WebDriverWait(browser, driver_wait_in_seconds).until(
                    condition.visibility_of_all_elements_located((By.CSS_SELECTOR,
                                                                  "#repo-content-pjax-container > div > div > div.Box.mt-3.position-relative > div.Box-body.p-0.blob-wrapper.data.type-yaml.gist-border-0 > div > table > tbody > tr"))):
                elem.append(tags)
            return elem
    except Exception as e:
        print(e)


def save_extracted_to_file(extract_info):
    try:
        with open(os.path.join(downloads_directory, 'extracted_info.txt'), 'a+') as file:
            for info in extract_info:
                file.write(f"{info.text} \n")
        return True
    except Exception as e:
        print(e)
