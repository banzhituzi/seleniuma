from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from pages.Locators import LoginPageLocators , WelcomePageLocators , AdminUserPageLocators

from pages.base_operate import  BasePage
class AdminUserPage(BasePage):
    def enter_username(self,username):
        WebDriverWait(self.driver,10).until(lambda driver:driver.find_element(*AdminUserPageLocators.txtUsername))
        menu = self.driver.find_element(*AdminUserPageLocators.menu_admin_viewAdminModule)
        menu1= self.driver.find_element(*AdminUserPageLocators.menu_admin_UserManagement)
        users = self.driver.find_element(*AdminUserPageLocators.menu_admin_viewSystemUsers)
        ActionChains(self.driver).move_to_element(menu).move_to_element(menu1).click(users).perform()

    def systemUser_userType_select(self , index):
        # systemUser_userType=self.driver.find_element(By.ID,"systemUser_userType")
        systemUser_userType = self.driver.find_element ( *AdminUserPageLocators.systemUser_userType_select )
        Select ( systemUser_userType ).select_by_index ( index )
