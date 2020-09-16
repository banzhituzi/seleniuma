# import pytest
# from selenium import webdriver
# @pytest.fixture(scope='module',autouse=True)
# #@pytest.fixture()
# class conftest():
#     def open_browser(self):
#      self.driver = webdriver.Chrome ( "C:\\Users\\Administrator\\PycharmProjects\\seleniuma\\driver\\chromedriver.exe" )
#
# @pytest.fixture()
#
# def login():
#     self.driver.get ( "http://59.110.232.6/orangehrm/symfony/web/index.php/auth/login" )
#     # 输入账号密码
#     driver.find_element_by_id ( "frmLogin" ).click ()
#     driver.find_element_by_id ( "txtUsername" ).click ()
#     driver.find_element_by_id ( "txtUsername" ).clear ()
#     driver.find_element_by_id ( "txtUsername" ).send_keys ( "root" )
#     driver.find_element_by_id ( "txtPassword" ).clear ()
#     driver.find_element_by_id ( "txtPassword" ).send_keys ( "password1" )
#     driver.find_element_by_id ( "btnLogin" ).click ()
#     yield
#     print ( "关闭浏览器" )