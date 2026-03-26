import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from basePages.Login_Admin_Page import Login_Admin_Page
from utilities.read_properties import Read_Config
from utilities.custom_logger import Log_Maker


class Test_01_AdminLogin:
    admin_page_url = Read_Config.get_admin_page_url()
    username = Read_Config.get_username()
    password = Read_Config.get_password()
    invalid_username = Read_Config.get_invalid_username()
    logger = Log_Maker.log_gen()

    def test_title_verification(self, setup):
        self.logger.info("***** Test_01_AdminLogin *****")
        self.logger.info("***** test_title_verification *****")
        self.driver = setup
        self.driver.get(self.admin_page_url)
        act_title = self.driver.title
        exp_title = "FoodKing - Restaurant Food Ordering & Delivery App"
        if act_title == exp_title:
            self.logger.info("***** test_title_verification title matched *****")
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\test_title_verification.png")
            self.logger.info("***** test_title_verification title not matched *****")
            self.driver.close()
            assert False

    def test_valid_admin_login(self, setup):
        self.logger.info("***** test_valid_admin_login *****")
        self.driver = setup
        self.driver.get(self.admin_page_url)
        self.admin_lp = Login_Admin_Page(self.driver)
        self.admin_lp.enter_username(self.username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login()
        # act_dashboard_text = self.driver.find_element(By.XPATH, "//div[@class='content-header']/h1").text
        # if act_dashboard_text == "Dashboard":
        #     assert True
        #     self.driver.close()
        # else:
        #     self.driver.close()
        #     assert False
        act_title = self.driver.title
        exp_title = "FoodKing - Restaurant Food Ordering & Delivery App"
        if act_title == exp_title:
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\test_valid_admin_login.png")
            self.driver.close()
            assert False

    def test_invalid_admin_login(self, setup):
        self.logger.info("***** test_invalid_admin_login *****")
        self.driver = setup
        self.driver.get(self.admin_page_url)
        self.admin_lp = Login_Admin_Page(self.driver)
        self.admin_lp.enter_username(self.invalid_username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login()
        # error_message = self.driver.find_element(By.XPATH, "li").tect
        # if error_message == "No customer account found":
        #     assert True
        #     self.driver.close()
        # else:
        #     self.driver.close()
        #     assert False
        act_title = self.driver.title
        exp_title = "FoodKing - Restaurant Food Ordering & Delivery App"
        if act_title == exp_title:
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\test_invalid_admin_login.png")
            self.driver.close()
            assert False
