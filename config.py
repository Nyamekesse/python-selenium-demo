import os

from selenium import webdriver

URL = "https://www.techlistic.com/p/selenium-practice-form.html"
IMAGE_PATH = os.path.join(os.getcwd(), 'js.png')
# add path to environment variables
os.environ['PATH'] += r"C:\selenium-chrome-drivers\chromedriver_win32"
downloads_directory = os.path.join(os.getcwd(), "saved_files")
logs = os.path.join(os.getcwd(), "LOGS")
options = webdriver.ChromeOptions()
if not os.path.exists(downloads_directory):
    os.mkdir(downloads_directory)

if not os.path.exists(logs):
    os.mkdir(logs)

# timeout in seconds
driver_wait_in_seconds = 10
browser = webdriver.Chrome(options=options)
browser.implicitly_wait(driver_wait_in_seconds)
