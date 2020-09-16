#登录要进行的操作
from selenium.webdriver.support.wait import WebDriverWait
from pages.Locators import LoginPageLocators,WelcomePageLocators

from pages.base_operate import  BasePage
class LoginPage(BasePage):
    #用户名输入用户名，输入密码，点击登陆
    def enter_username(self,username):
        WebDriverWait(self.driver,10).until(lambda driver:driver.find_element(*LoginPageLocators.txtUsername))
        usernameele=self.driver.find_element(*LoginPageLocators.txtUsername)
        usernameele.click()
        usernameele.clear()
        usernameele.send_keys(username)

    def enter_password(self,password):
        WebDriverWait ( self.driver , 10 ).until (
        lambda driver: driver.find_element ( *LoginPageLocators.txtPassword ) )
        usernameele = self.driver.find_element ( *LoginPageLocators.txtPassword )
        usernameele.click ()
        usernameele.clear ()
        usernameele.send_keys(password)

    def click_login(self):
        clickele=self.driver.find_element(*LoginPageLocators.btnLogin)
        clickele.click()

    def login_sucess_result(self):
        WebDriverWait ( self.driver , 10 ).until (lambda driver: driver.find_element (*WelcomePageLocators.welcome))
        return self.driver.find_element(*WelcomePageLocators.welcome).text
