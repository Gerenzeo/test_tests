from selenium.webdriver.common.by import By

class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get("https://www.demoblaze.com/")
    
    def click_galaxy_s6(self):
        galaxy_s6 = self.driver.find_element(By.XPATH, "/html/body/div[5]/div/div[2]/div/div[1]/div/div/h4/a")
        galaxy_s6.click()

    def click_monitor(self):
        monitor_link = self.driver.find_element(By.CSS_SELECTOR, """[onclick="byCat('monitor')"]""")
        monitor_link.click()
    
    def check_products_count(self, count):
        monitors = self.driver.find_elements(By.CSS_SELECTOR, ".card")
        assert len(monitors) == count