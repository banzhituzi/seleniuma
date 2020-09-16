#页面元素的定位方式
from selenium.webdriver.common.by import By


class LoginPageLocators(object):
    txtUsername=(By.ID,"txtUsername")
    txtPassword=(By.ID,"txtPassword")
    btnLogin=(By.ID,"btnLogin")

class WelcomePageLocators(object):
    welcome=(By.ID,"welcome")

class AdminUserPageLocators(object):
    menu_admin_viewAdminModule = ( By.ID , 'menu_admin_viewAdminModule' )
    menu_admin_UserManagement =  ( By.ID , 'menu_admin_UserManagement' )
    menu_admin_viewSystemUsers =  ( By.ID , 'menu_admin_viewSystemUsers' )
    btnAdd=(By.ID,"btnAdd")
    systemUser_userType =  (By.ID, "systemUser_userType" )
    systemUser_employeeName_empName=(By.ID,"systemUser_employeeName_empName")
    systemUser_userName=(By.ID,"systemUser_userName")
    systemUser_status_select=(By.ID,"systemUser_status_select")
    systemUser_password=(By.ID," systemUser_password")
    systemUser_confirmPassword=(By.ID,"systemUser_confirmPassword")
    btnSave=(By.ID,"btnSave")

class PimemployPageLocators(object):
     menu_pim_viewPimModule=(By.ID,"menu_pim_viewPimModule")
     menu_pim_viewEmployeeList = ( By.ID , 'menu_pim_viewEmployeeList' )
