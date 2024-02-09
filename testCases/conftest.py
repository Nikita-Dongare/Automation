import pytest
from selenium import webdriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
@pytest.fixture
def setup():

    driver = webdriver.Chrome(options=chrome_options)
    #driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://automation.credence.in/login")
    return driver

