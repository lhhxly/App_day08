import sys,os
sys.path.append(os.getcwd())

import pytest
import time
from appium import webdriver
from Base.Base import Base
from Page.sms_page import Sms_Page
from selenium.webdriver.common.by import By
from Base.get_driver import get_driver


class Test_Prc():

    def setup_class(self):
        self.driver = get_driver("com.android.mms",".ui.ConversationList")

        self.sms_obj = Sms_Page(self.driver)

    def teardown_class(self):
        self.driver.quit()

    #编写测试方法
    #1.输入手机号方法
    @pytest.fixture(scope="class",autouse="True")
    def test_mms(self):
        self.sms_obj.Input_phone("18766668888")

    #2.发送短信方法
    @pytest.mark.parametrize("value",["123","eee","gftg"])
    def test_send_mms(self,value):
        self.sms_obj.Send_sms(value)
        time.sleep(1)
        #3.获取结果方法
        #断言
        assert value in self.sms_obj.Get_res()

if __name__ == '__main__':
    pytest.main("test_mms.py")
