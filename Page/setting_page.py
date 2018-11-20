from Base.Base import Base
import Page

class Setting_page(Base):
    def __init__(self,driver):
        Base.__init__(self,driver)

    def More(self):
        #点击更多
        self.click_element(Page.more_btn_xpath)