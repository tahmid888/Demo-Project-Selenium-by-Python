import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from basePages.Login_Admin_Page import Login_Admin_Page
from utilities.read_properties import Read_Config
from utilities.custom_logger import Log_Maker
from utilities import excel_utils


class Test_02_AdminLoginDDT:
    admin_page_url = Read_Config.get_admin_page_url()
    logger = Log_Maker.log_gen()
    PATH = ".//testData//adminData.xlsx"

    def test_valid_admin_login_DDT(self, setup):
        self.logger.info("***** test_valid_admin_login DDT *****")
        self.driver = setup
        self.driver.implicitly_wait(10)
        self.driver.get(self.admin_page_url)
        self.admin_lp = Login_Admin_Page(self.driver)

        self.rows=excel_utils.get_row_count(".//testData//adminData.xlsx","Sheet1")
        print("Number of rows: ", self.rows)

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
