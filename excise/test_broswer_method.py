import time
from selenium import webdriver
#打开浏览器
driver=webdriver.Chrome("C:\\Users\\Administrator\\PycharmProjects\\seleniuma\\driver\\chromedriver.exe")
#网页最大化
driver.maximize_window()
#输入要测试地址登录页
driver.get("http://59.110.232.6/orangehrm/symfony/web/index.php/auth/login")
#输入账号密码
driver.find_element_by_id ( "frmLogin" ).click ()
driver.find_element_by_id ( "txtUsername" ).click ()
driver.find_element_by_id ( "txtUsername" ).clear ()
driver.find_element_by_id ( "txtUsername" ).send_keys ( "root" )
driver.find_element_by_id ( "txtPassword" ).clear ()
driver.find_element_by_id ( "txtPassword" ).send_keys ( "password1" )
driver.find_element_by_id ( "btnLogin" ).click ()
#刷新网页
driver.refresh()
#后退
driver.back()
#前进
driver.forward()
#
assert  "Welcome dxc" == driver.find_element_by_id("welcome").text
#截屏
filename = time.strftime('%Y-%m-%d',time.localtime(time.time()))
driver.save_screenshot(filename+".png")
driver.quit()