from selenium import webdriver
import time
#打开浏览器
driver=webdriver.Chrome("C:\\Users\\Administrator\\PycharmProjects\\seleniuma\\driver\\chromedriver.exe")
#输入要测试地址登录页
driver.get("http://59.110.232.6/orangehrm/symfony/web/index.php/recruitment/addJobVacancy/Id/49")
#输入用户名，找到用户名所有文本框，定位方式id，name，xpath，css
driver.find_element_by_id("txtUsername").send_keys("root")
driver.find_element_by_id("txtPassword").send_keys("password1")
driver.find_element_by_id("btnLogin").click()
time.sleep(2)
assert  "Welcome dxc" == driver.find_element_by_id("welcome").text
time.sleep(2)
driver.close()
