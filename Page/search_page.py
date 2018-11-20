from Base.Base import Base
from selenium.webdriver.common.by import By
import pytest

class Search_Page(Base):
    def __init__(self,driver):
        Base.__init__(self,driver)

        #定位搜索按钮
        self.search_btn_by_id = (By.ID,"com.android.settings:id/search")
        #定位搜索框
        self.search_input_by_id = (By.ID,"android:id/search_src_text")
        #获取列表
        self.search_res_by_ids = (By.ID,"com.android.settings:id/title")

    #点击搜索按钮
    def Search_btn(self):
        self.click_element(self.search_btn_by_id)

    #定位搜索框，输入内容
    def Input(self,name,value):
        self.send_element(self.search_input_by_id).send_keys(name,value)

    #获取文本列表
    def get_res(self):
        res_list = self.search_elements(self.search_res_by_ids)
        return [i.text for i in res_list]
