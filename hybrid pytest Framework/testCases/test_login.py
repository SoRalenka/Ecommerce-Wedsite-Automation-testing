import pytest
from selenium import webdriver
from pageObject.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_001_Login :
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getApplicationUsername()
    password = ReadConfig.getApplicationPassword()

    logger = LogGen.loggen()    

    def test_homePageTitle(self,setup):
        self.logger.info("************** Test_001_Login*****************")
        self.logger.info("************** Verifying Home Page Title *****************")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        if act_title == "Your store. Login":
            self.driver.close()
            self.logger.info("************** Login test passed *****************")
            assert True
        else : 
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homePageTitle.png")
            self.driver.close()
            self.logger.info("************** Login test Failed *****************")
            assert False

    def test_login(self,setup):
        self.logger.info("************** Verifying Login Test *****************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickRememberMe()
        self.lp.clickLogin()
        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            self.driver.close()
            self.logger.info("************** Login Test is passed *****************")
            assert True
        else :
            self.driver.save_screenshot(".\\Screenshots\\"+"test_login.png")
            self.driver.close()
            self.logger.info("************** Loggin test is failed *****************")
            assert False



# to run on terminal use : pytest -v -s -n=2 --html=Reports\report.html testCases\test_login.py
# by - sourabh kumar lenka 

