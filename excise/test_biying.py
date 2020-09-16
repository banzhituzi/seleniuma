from selenium import webdriver
import time
driver=webdriver.Chrome("C:\\Users\\Administrator\\PycharmProjects\\seleniuma\\driver\\chromedriver.exe")
driver.get("https://cn.bing.com/search?q=python&qs=n&form=QBLH&sp=-1&pq=python&sc=9-6&sk=&cvid=61BD59A1ACA04A0CA84C91EF80023273")
driver.find_element_by_id("sb_form_q").send_keys("python")
driver.find_element_by_id("sb_form_go").click()
assert 'python' in driver.page_source
time.sleep(2)
driver.close()