from selenium import webdriver
import time
#进入浏览器
driver =webdriver.Chrome("C:\\Users\Administrator\PycharmProjects\seleniuma\driver\chromedriver.exe")
#输入要测试的网址
driver.get("http://59.110.232.6/orangehrm/symfony/web/index.php/admin/viewJobTitleList")
#登录密码
driver.find_element_by_id("txtUsername").send_keys("root")
#输入密码
driver.find_element_by_id("txtPassword").send_keys("password1")

driver.find_element_by_id("btnLogin").click()
driver.find_element_by_id ( "btnAdd" ).click ()
driver.find_element_by_id ( "jobTitle_jobTitle" ).click ()
driver.find_element_by_id ( "jobTitle_jobTitle" ).clear ()
driver.find_element_by_id ( "jobTitle_jobTitle" ).send_keys ( "gaojj" )
driver.find_element_by_id ( "btnSave" ).click ()

time.sleep(2)
assert  "Welcome dxc" == driver.find_element_by_id("welcome").text
assert "gaojj" == driver.find_element_by_id("gaojj").text
driver.close()
time.sleep(2)