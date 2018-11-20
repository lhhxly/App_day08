import sys,os
sys.path.append(os.getcwd())
from Base.page import Page
from Base.get_driver import get_driver


class Test_setting():
    def setup_class(self):
        self.page_obj = Page(get_driver("com.android.settings", ".Settings"))
        # self.page_obj = Page(get_driver("com.android.settings", ".Settings"))


    def teardown_class(self):
        self.page_obj.driver.quit()


    def test_change(self):
        #点击更多
        self.page_obj.get_setting_page().More()
        #点击移动网络
        self.page_obj.get_more_page().network_btn()
        #点击首选网络类型
        self.page_obj.get_mobile_network().select_first()

        #断言
        # print(self.page_obj.get_mobile_network().get_res())
        assert "3G" in self.page_obj.get_mobile_network().get_res()




