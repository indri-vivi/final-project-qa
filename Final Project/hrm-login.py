## Indriani Final Project

import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestLogin(unittest.TestCase): 

    def setUp(self): 
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        
    def TC_002(self): #login with the correct username and password

        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com") # open the site
        driver.find_element(By.ID,"txtUsername").send_keys("Admin") # fill username
        time.sleep(2)
        driver.find_element(By.ID,"txtPassword").send_keys("admin123") # fill password
        time.sleep(2)
        driver.find_element(By.XPATH,"/html/body/div[1]/div/div[3]/div[2]/div[2]/form/div[5]/input").click() #click the login button
        time.sleep(2)

    def TC_005(self): #login with no input 

        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com") # open the site
        time.sleep(2)
        driver.find_element(By.XPATH,"/html/body/div[1]/div/div[3]/div[2]/div[2]/form/div[5]/input").click() #click the login button
        time.sleep(2)
        response_message = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[3]/div[2]/div[2]/form/div[5]/span").text #find the response message
        self.assertEqual(response_message, "Username cannot be empty") # validate the message
        time.sleep(2)

    def TC_003(self): #login with wrong username

        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com") # open the site
        driver.find_element(By.ID,"txtUsername").send_keys("----vb") # fill username
        time.sleep(2)
        driver.find_element(By.ID,"txtPassword").send_keys("") # fill password
        time.sleep(2)
        driver.find_element(By.XPATH,"/html/body/div[1]/div/div[3]/div[2]/div[2]/form/div[5]/input").click() #click the login button
        time.sleep(2)
        response_message = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[3]/div[2]/div[2]/form/div[5]/span").text #find the response message
        self.assertEqual(response_message, "Password cannot be empty") # validate the message
        time.sleep(2)

    def tearDown(self): 
        self.driver.close() 

if __name__ == "__main__": 
    unittest.main()