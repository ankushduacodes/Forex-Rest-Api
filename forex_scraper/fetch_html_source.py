from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os


def fetch_html_source():
    """Fetches html source from the required page

    Returns:
        HTML source: Returns HTML source for the required page
    """

    # Change the path to the driver accordingly
    path = os.getenv('path')

    # initial webdriver
    driver = webdriver.Chrome(path)

    # placing request to initial page
    driver.get("https://www.investing.com/currencies/single-currency-crosses")

    # xpath to select the option by value not by index because if a new currency is added in the future the index
    # will change but the value will remain same
    xpath_EUR = "//select[@id='symbols']//option[@value='17']"

    # simulating click functionality to select desired option by value
    driver.find_element_by_xpath(xpath_EUR).click()

    # Waiting for a desired element to appear, as the data is being loaded from ajax requests, it may take web server
    # few seconds extra to load all the content of the site thats why we wait for a desired element to show up before
    # picking the source code of the page, if the element doesnot show up with in 10 seconds a timeout exception is
    # raised as soon as the desired element show up we pick the page source and return it
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "pair_6")))
    return driver.page_source
