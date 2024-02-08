import os.path
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from pathlib import Path
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

def defaultPage():
        options = webdriver.ChromeOptions()
        options.page_load_strategy = 'eager'
        driver = webdriver.Chrome(options=options)
        driver.get("https://codebeautify.org/generate-random-date")
        driver.maximize_window()
        action = ActionChains(driver)
        if (driver.title == "Random Date Generator"):
            print("Success on checking title of the page")
        else:
            print("ERR-001 incorrect page title")
        driver.implicitly_wait(5)

        #checking the default number of dates
        date_count_element = driver.find_element("id","count")
        driver.implicitly_wait(5)
        default_date_count = date_count_element.get_attribute("value")
        if default_date_count == '10':
            print("Success on checking the default count")
        else:
            print("ERR-002 Incorrect Default value for number of dates")

        #checking the default output Date Format
        date_format_element = driver.find_element("id","format")
        driver.implicitly_wait(5)
        date_format = date_format_element.get_attribute("value")
        if date_format == "mm-dd-yyyy":
             print("success on checking the default date format")
        else:
             print("ERR-003 Incorrect default date format")

        #checking the default custom format
        custom_date_element = driver.find_element("id","custom-format")
        driver.implicitly_wait(5)
        custom_date_format = custom_date_element.get_attribute("value")
        if custom_date_format == "YY-MM-DD":
             print("Success on checking the custom date format")
        else:
             print("ERR-004 Incorrect default custom date format")

        #checking the default start date
        start_date_element = driver.find_element("id","start")
        driver.implicitly_wait(5)
        start_date = start_date_element.get_attribute("value")
        if start_date == "2020-01-01 00:00:00":
             print("Success on checking the default start date value")
        else:
             print("ERR-004 Incorrect default start date ")

         #checking the default end date
        end_date_element = driver.find_element("id","end")
        driver.implicitly_wait(5)
        end_date = end_date_element.get_attribute("value")
        if end_date == "2099-12-31 23:59:59":
             print("Success on checking the default end date value")
        else:
             print("ERR-004 Incorrect default end date ")
        c = 0
        #checking copy to clipboard
        console_output_element = driver.find_element("id","generatedRandomDateTextArea")
        console_output = console_output_element.get_attribute("value")
        print(console_output)
        if len(console_output) == 109:
             print("success on checking the number of dates on the console")
        else:
             print("ERR-005 Incorrect numder of dates displayed on the console")

        #checking download to file
        downloads_path = str(Path.home() / "Downloads")
        filepath = downloads_path + '/generate-random-date.txt'
        if os.path.exists(filepath):
            os.remove(filepath)
            print("Already existing file deleted")
        else:
            print("File does not exists , good to download")
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, ".//*[contains(@onclick,'download')]"))).click()
        time.sleep(30)
        if os.path.exists(filepath):
            print("File Successfully downloaded")
        else:
            print("ERR-006 Download file not working properly")
        driver.quit()



defaultPage()

