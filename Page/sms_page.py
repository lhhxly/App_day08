import Page
from Base.Base import Base


class Sms_Page(Base):
    def __init__(self,driver):
        Base.__init__(self,driver)
        # self.base_obj = Base(driver)

    def Input_phone(self,text):
        #点击短信
        self.click_element(Page.add_sms_btn_byid)
        #输入电话号码
        self.send_element(Page.send_phone_btn_byid,text)

    def Send_sms(self,text):
        #输入短信内容
        self.send_element(Page.send_sms_btn_byid,text)
        #点击发送
        self.click_element(Page.send_btn_byid)

    def Get_res(self):
        #获取文本列表
        res = self.search_elements(Page.text_byids)

        return [i.text for i in res]

