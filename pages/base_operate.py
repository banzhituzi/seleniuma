class BasePage(object):
    #初始化打开浏览器
    def __init__(self,driver):
        self.driver=driver
    def save_picture(self,file_path):
        self.driver.save_screenshot(file_path)

