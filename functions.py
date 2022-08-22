from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as condition
from selenium.common.exceptions import *
import os
from config import (browser, driver_wait_in_seconds, downloads_directory, logs)


def remove_ads(driver, selector: str):
    i = 0
    # Parsing content using beautifulsoup
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    check_for_ads = soup.find(selector)
    if check_for_ads:
        while soup.find(selector):
            script = """
                var element = document.querySelector(""" + "'" + selector + "'" + """);
                if (element)
                    element.parentNode.removeChild(element);
                """
            driver.execute_script(script)
            # Parsing content using beautifulsoup
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            i += 1

        print('Removed ' + str(i) + ' tags with the selector ' + "'" + selector + "'" + " and all it's children tags.")

        return True
    else:
        return False



def cookieDismiss():
    try:
        if browser.find_element(By.ID, 'cookieChoiceDismiss').is_displayed():
            cookie = browser.find_element(By.ID, 'cookieChoiceDismiss')
            cookie.click()

    except NoSuchElementException as e:
        print(f'check {logs} for more info')


def get_text_from_github():
    try:
        elem = []
        if 'GitHub' in browser.title:
            for tags in WebDriverWait(browser, driver_wait_in_seconds).until(
                    condition.visibility_of_all_elements_located((By.CSS_SELECTOR,
                                                                  "#repo-content-pjax-container > div > div > div.Box.mt-3.position-relative > div.Box-body.p-0.blob-wrapper.data.type-yaml.gist-border-0 > div > table > tbody > tr"))):
                elem.append(tags)
            return elem
    except Exception:
        print(f'check {logs} for more info')


def save_extracted_to_file(extract_info):
    try:
        with open(os.path.join(downloads_directory, 'extracted_info.txt'), 'a+') as file:
            for info in extract_info:
                file.write(f"{info.text} \n")
        return True
    except Exception:
        print(f'something occurred check {logs} for more info')
