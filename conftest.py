import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture()
def driver():
    options = Options()
    options.add_argument("--headline") # Running in deamon (Running without opening browser)
    browser = webdriver.Chrome() # Open browser Chroome
    browser.maximize_window() # Open window on full size
    browser.implicitly_wait(3) # Wait 3 seconds
    yield browser
    browser.close() # Close browser