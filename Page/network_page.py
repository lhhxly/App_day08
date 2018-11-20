from Base.Base import Base
import Page

class Network_page(Base):
    def __init__(self,driver):
        Base.__init__(self,driver)

    #点击首选网络
    def select_first(self):
        self.click_element(Page.network_type_btn_xpath)
        self.click_element(Page.select_3G_btn_xpath)
    def get_res(self):

        res = self.search_elements(Page.select_3G_btn_by_ids)

        return [i.text for i in res]
