## Indriani Final Projectt

import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class Dashboard(unittest.TestCase): 

    def setUp(self): 
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def test_TC_030(self): #open the sub menu user

        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com") # open the site
        driver.find_element(By.ID,"txtUsername").send_keys("Admin") # fill username
        time.sleep(2)
        driver.find_element(By.ID,"txtPassword").send_keys("admin123") # fill password
        time.sleep(2)
        driver.find_element(By.XPATH,"/html/body/div[1]/div/div[3]/div[2]/div[2]/form/div[5]/input").click() #click the login button
        time.sleep(2)
        driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/ul/li[8]/a").click() #open the dashboard
        time.sleep (1)

if __name__ == "__main__": 
    unittest.main()
