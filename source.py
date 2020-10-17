from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def make_source_file():
    # Change the path to the driver accordingly
    path = "/Users/ankushdua/chromedriver"
    driver = webdriver.Chrome(path)

    driver.get("https://www.investing.com/currencies/single-currency-crosses")
    driver.find_element_by_xpath("//*[@id='symbols']/option[40]").click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "pair_6")))
    return driver.page_source
