# -*- coding: utf-8 -*-
from selenium import webdriver

import unittest , time , re
from ddt import ddt,file_data
from HTMLTestRunner import HTMLTestRunner

@ddt
class test_sele( unittest.TestCase ):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome (executable_path ='C:\\Users\\Administrator\\PycharmProjects\\seleniuma\\driver\\chromedriver.exe')
        cls.driver.implicitly_wait ( 30 )
        cls.base_url = "http://59.110.232.6"

    def test_login(self):
        driver = self.driver
        driver.get ( self.base_url + "/orangehrm/symfony/web/index.php/admin/viewJobTitleList" )
        driver.find_element_by_id ( "frmLogin" ).click ()
        driver.find_element_by_id ( "txtUsername" ).click ()
        driver.find_element_by_id ( "txtUsername" ).clear ()
        driver.find_element_by_id ( "txtUsername" ).send_keys ( "root" )
        driver.find_element_by_id ( "txtPassword" ).clear ()
        driver.find_element_by_id ( "txtPassword" ).send_keys ( "password1" )
        driver.find_element_by_id ( "btnLogin" ).click ()
        driver.find_element_by_id ( "menu_admin_Job" ).click ()  # 点击管理员job
        driver.find_element_by_id ( "menu_admin_viewJobTitleList" ).click ()  # 点击JobTitl
    @file_data("login.yaml")
    def test_sele(self,jobtitle):
        print(jobtitle)
        driver = self.driver
        driver.find_element_by_id ( "btnAdd" ).click ()
        driver.find_element_by_id ( "jobTitle_jobTitle" ).click ()
        driver.find_element_by_id ( "jobTitle_jobTitle" ).clear ()
        driver.find_element_by_id ( "jobTitle_jobTitle" ).send_keys (jobtitle)
        driver.find_element_by_id ( "btnSave" ).click ()
        #driver.find_element_by_xpath ( "//a[@id='menu_recruitment_viewRecruitmentModule']/b" ).click ()
        #assert  "Welcome dxc" == driver.find_element_by_id("welcome").text

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit ()
        #self.assertEqual ( [] , self.verificationErrors )


if __name__ == "__main__":
   # unittest.main ()
   #添加报告
   #suite套件，有多个测试用例组成
    suite=unittest.TestSuite()
   #通过类名把要测试类及类中方法加载到套件中
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(test_sele ))
   #执行测试用例
    with open("test_report.html",'wb')as fp:
        runner=HTMLTestRunner(
               stream=fp,
               title='测试报告',
               description="ui测试",
        )
        runner.run(suite)