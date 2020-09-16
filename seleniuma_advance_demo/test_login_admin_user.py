import select
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time
import pytest
import unittest

from selenium.webdriver.support.select import Select


class TestHrmLoginAdduser(unittest.TestCase):
    #@pytest.fixture(scope='module',autouse=True)
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome (
            executable_path="C:\\Users\Administrator\PycharmProjects\seleniuma\driver\chromedriver.exe" )
        cls.driver.get ( "http://59.110.232.6/orangehrm/symfony/web/index.php/auth/login" )
        cls.driver.maximize_window ()
        # cls.driver.find_element_by_id ( "txtUsername" ).send_keys ( "root" )
        # cls.driver.find_element ( By.ID , "txtPassword" ).send_keys ( "password1" )
        # cls.driver.find_element_by_id ( "btnLogin" ).click ()
        # time.sleep ( 2 )
        # assert 'Welcome dxc' == cls.driver.find_element ( By.ID , "welcome" ).text
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


    def setUp(self):
        self.driver.find_element_by_id ( "txtUsername" ).send_keys ( "root" )
        self.driver.find_element ( By.ID , "txtPassword" ).send_keys ( "password1" )
        self.driver.find_element_by_id ( "btnLogin" ).click ()
        time.sleep ( 2 )
        assert 'Welcome dxc' == self.driver.find_element(By.ID,"welcome").text

    def test_adduser(self):
        driver=self.driver
        menu_admin_viewAdminModule=driver.find_element(By.ID,'menu_admin_viewAdminModule')
        menu_admin_UserManagement=driver.find_element(By.ID,'menu_admin_UserManagement')
        menu_admin_viewSystemUsers=driver.find_element(By.ID,'menu_admin_viewSystemUsers')
        ActionChains (driver ) \
            .move_to_element ( menu_admin_viewAdminModule ) \
            .move_to_element ( menu_admin_UserManagement ) \
            .click ( menu_admin_viewSystemUsers ).perform ()
        assert 'Username'in driver.page_source
        self.driver.find_element_by_id('btnAdd').click()
        systemUser_userType=self.driver.find_element_by_id("systemUser_userType")
        Select( systemUser_userType ).select_by_value("1")
        self.driver.find_element_by_id("systemUser_employeeName_empName").send_keys("dxc d")
        self.driver.find_element_by_id("systemUser_userName").click()
        self.driver.find_element_by_id("systemUser_userName").send_keys("rootafa")
        systemUser_status=self.driver.find_element_by_id("systemUser_status")
        Select(systemUser_status).select_by_index(1)
        self.driver.find_element_by_id("systemUser_password").send_keys("password1")
        self.driver.find_element_by_id ( "systemUser_confirmPassword" ).send_keys ( "password1" )
        self.driver.find_element_by_id ( "btnSave" ).click ()
        time.sleep(5)
        self.driver.refresh()
    #def test_pim(self):
        #悬停到pimdaoEmployee List

        menu_pim_viewPimModule = driver.find_element ( By.ID , 'menu_pim_viewPimModule' )
        menu_pim_viewEmployeeList = driver.find_element ( By.ID , 'menu_pim_viewEmployeeList' )
        ActionChains ( driver ) \
            .move_to_element ( menu_pim_viewPimModule ) \
            .click ( menu_pim_viewEmployeeList ).perform ()
        time.sleep(3)
        self.driver.execute_script("window.scrollBy(0,500)")
        time.sleep(3)
        self.driver.find_element_by_id ( 'ohrmList_chkSelectRecord_77' ).click ()
        time.sleep(2)
        ohrmList_chkSelectRecord=self.driver.find_elements_by_name("chkSelectRow[]")
        # for ohrmList  in    ohrmList_chkSelectRecord:
        #     print(ohrmList.get)
        ohrmList_chkSelectRecord[-1].click()
        self.driver.save_screenshot("1.png")
        time.sleep(3)






