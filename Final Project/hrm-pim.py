## Indriani Final Project

import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class testpim(unittest.TestCase): 

    def setUp(self): 
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        
    def TC_015(self): #add employee

        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com") # open the site
        driver.find_element(By.ID,"txtUsername").send_keys("Admin") # fill username
        time.sleep(2)
        driver.find_element(By.ID,"txtPassword").send_keys("admin123") # fill password
        time.sleep(2)
        driver.find_element(By.XPATH,"/html/body/div[1]/div/div[3]/div[2]/div[2]/form/div[5]/input").click() #click the login button
        time.sleep(2)
        driver.find_element(By.ID,"menu_pim_viewPimModule").click() #click PIM Menu
        time.sleep(2)
        driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[2]/div/form/div[1]/input[1]").click() #click add
        driver.find_element(By.ID,"firstName").send_keys("virtual") #add first name
        driver.find_element(By.ID,"lastName").send_keys("user")  #add last name
        driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/div[2]/form/fieldset/p/input").click() #click save


    def tearDown(self): 
        self.driver.close() 

if __name__ == "__main__": 
    unittest.main()