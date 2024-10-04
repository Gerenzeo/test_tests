
import time

from selenium.webdriver.common.by import By
from selenium import webdriver

from pages.homepage import HomePage
from pages.product import ProductPage

# Fixture getting from conftest.py

def test_open_s6(driver: webdriver.Chrome):
    homepage = HomePage(driver)
    homepage.open()
    homepage.click_galaxy_s6()
    product_page = ProductPage(driver)
    product_page.check_title_is("Samsung galaxy s6")


    
def test_two_monitors(driver: webdriver.Chrome):
    homepage = HomePage(driver)
    homepage.open()
    homepage.click_monitor()
    time.sleep(3)
    homepage.check_products_count(2)
