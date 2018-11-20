from Page.more_page import More_Page
from Page.setting_page import Setting_page
from Page.network_page import Network_page

class Page:
    def __init__(self,driver):
        self.driver = driver

    def get_setting_page(self):
        #返回设置页面类实例化对象
        return Setting_page(self.driver)

    def get_more_page(self):
        #返回更多页面实例化对象
        return More_Page(self.driver)

    def get_mobile_network(self):
        #返回移动网络页面对象
        return Network_page(self.driver)