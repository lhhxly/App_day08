import pytest
import time
from appium import webdriver
from Page.search_page import Search_Page
from selenium.webdriver.common.by import By
from Base.get_driver import get_driver
from appium import webdriver
import pytest
'''
1.点击搜索  只点击一次--class
2.输入内容  点击多次--function
     输入 1   休眠存在
     输入 m   MAC地址存在
     输入 ip  IP地址是否存在
'''



class Test_Prc():


    def setup_class(self):
        self.driver = get_driver("com.android.settings", ".Settings")
        self.search_obj = Search_Page(self.driver)

    def teardown_class(self):
        self.driver.quit()

    @pytest.fixture(scope="class",autouse=True)
    def find_btn(self):
        self.search_obj.Search_btn()

    @pytest.mark.parametrize("name,value",[("1","休眠"),("m","MAC地址"),("ip","IP地址")])
    def test_search_text(self,name,value):
        #定位search文本框  传值

        self.search_obj.Input(name,value)
        time.sleep(1)
        #断言
        # if data == 1:
        #     assert "休眠" in [i.text for i in search_list]
        # if data == "m":
        #     assert "MAC地址" in [i.text for i in search_list]
        # if data == "ip":
        #     assert "IP地址" in [i.text for i in search_list]
        # assert data.get("value") in [i.text for i in search_list]
        assert value in self.search_obj.get_res()
if __name__ == '__main__':
    pytest.main("test_search.py")
