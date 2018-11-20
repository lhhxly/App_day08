from Base.Base import Base
import Page

class More_Page(Base):
    def __init__(self,driver):
        Base.__init__(self,driver)

    def network_btn(self):
        self.click_element(Page.network_btn_xpath)



