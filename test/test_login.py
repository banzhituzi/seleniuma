import unittest
from selenium import webdriver

from pages import base_operate , login_operate


class TestLogin(unittest.TestCase):
    #打开浏览器，输入登录页
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome(executable_path="C:\\Users\Administrator\PycharmProjects\seleniuma\driver\chromedriver.exe")
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()
        cls.driver.get("http://59.110.232.6/orangehrm/symfony/web/index.php/auth/login")
        cls.base_page = base_operate.BasePage(cls.driver)
    def test_login_correct(self):
        #初始化登录页，按测试用例顺序编写代码加断言
        login_page=login_operate.LoginPage(self.driver)
        login_page.enter_username("root")
        login_page.enter_password("password1")
        login_page.click_login()
        self.base_page.save_picture("2.png")
        assert 'Welcome dxc' in login_page.login_sucess_result()
    @unittest.skip
    def test_login_error(self):
        login_page=login_operate.LoginPage(self.driver)
        login_page.enter_username("root")
        login_page.enter_password("password")
        login_page.click_login()
        self.base_page.save_picture("2.png")
        assert 'Welcome dxc' in login_page.login_sucess_result()
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()