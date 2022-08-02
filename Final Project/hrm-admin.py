## Indriani Final Projectt

import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestAdmin(unittest.TestCase): 

    def setUp(self): 
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        
    def test_TC_006(self): #open the sub menu user

        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com") # open the site
        driver.find_element(By.ID,"txtUsername").send_keys("Admin") # fill username
        time.sleep(2)
        driver.find_element(By.ID,"txtPassword").send_keys("admin123") # fill password
        time.sleep(2)
        driver.find_element(By.XPATH,"/html/body/div[1]/div/div[3]/div[2]/div[2]/form/div[5]/input").click() #click the login button
        time.sleep(2)
        driver.find_element(By.ID,"menu_admin_viewAdminModule").click() # Open Admin Module
        driver.find_element(By.ID,"menu_admin_UserManagement").click() # Open User management
        time.sleep(3)        
        driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/ul/li[1]/ul/li[1]/ul/li/a").click() #click user
        time.sleep(2)


    def test_TC_007(self): #search existing user

        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com") # open the site
        driver.find_element(By.ID,"txtUsername").send_keys("Admin") # fill username
        time.sleep(2)
        driver.find_element(By.ID,"txtPassword").send_keys("admin123") # fill password
        time.sleep(2)
        driver.find_element(By.XPATH,"/html/body/div[1]/div/div[3]/div[2]/div[2]/form/div[5]/input").click() #click the login button
        time.sleep(2)
        driver.find_element(By.ID,"menu_admin_viewAdminModule").click() # Open Admin Module
        driver.find_element(By.ID,"menu_admin_UserManagement").click() # Open User management
        time.sleep(3)        
        driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/ul/li[1]/ul/li[1]/ul/li/a").click() #click user
        time.sleep(2)
        driver.find_element(By.ID,"searchSystemUser_userName").send_keys("ahmet53") # fill username
        time.sleep(2)
        driver.find_element(By.ID,"searchBtn").click() # click search
        time.sleep(2)

    def test_TC_009(self): #search by user role

        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com") # open the site
        driver.find_element(By.ID,"txtUsername").send_keys("Admin") # fill username
        time.sleep(2)
        driver.find_element(By.ID,"txtPassword").send_keys("admin123") # fill password
        time.sleep(2)
        driver.find_element(By.XPATH,"/html/body/div[1]/div/div[3]/div[2]/div[2]/form/div[5]/input").click() #click the login button
        time.sleep(2)
        driver.find_element(By.ID,"menu_admin_viewAdminModule").click() # Open Admin Module
        driver.find_element(By.ID,"menu_admin_UserManagement").click() # Open User management
        time.sleep(3)        
        driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/ul/li[1]/ul/li[1]/ul/li/a").click() #click user
        time.sleep(2)
        driver.find_element(By.ID,"searchSystemUser_userType").click() # click user type
        time.sleep(2)
        driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[1]/div[2]/form/fieldset/ol/li[2]/select/option[2]").click() #click admin
        time.sleep(2)
        driver.find_element(By.ID,"searchBtn").click() # click search
        time.sleep(2)

    def tearDown(self): 
        self.driver.close() 

if __name__ == "__main__": 
    unittest.main()
