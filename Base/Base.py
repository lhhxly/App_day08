from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class Base:

    def __init__(self,driver):

        self.driver = driver

    #定位点击元素
    def search_element(self, loc, timeout=10, poll_frequency=1):
        """
        定位单个元素
        :param loc_type: 远元祖定位类型 (By.ID,ID属性值) (By.XPATH,XPATH属性值) (By.CLASS_NAME,CLASS_NAME属性值)
        :param timeout: 超时时间
        :param poll_frequency: 搜索元素间隔
        :return: 定位对象
        """
        return WebDriverWait(self.driver, timeout, poll_frequency).until(lambda x: x.find_element(*loc))

    def search_elements(self, loc, timeout=10, poll_frequency=1):
        """
        定位单个元素
        :param loc_type: 远元祖定位类型 (By.ID,ID属性值) (By.XPATH,XPATH属性值) (By.CLASS_NAME,CLASS_NAME属性值)
        :param timeout: 超时时间
        :param poll_frequency: 搜索元素间隔
        :return: 定位对象
        """
        return WebDriverWait(self.driver, timeout, poll_frequency).until(lambda x: x.find_elements(*loc))
    def click_element(self, loc, timeout=10, poll_frequency=1):
        """
        点击元素
        :param loc_type: 祖定位类型 (By.ID,ID属性值) (By.XPATH,XPATH属性值) (By.CLASS_NAME,CLASS_NAME属性值)
        :param timeout: 超时时间
        :param poll_frequency: 搜索元素间隔
        :return:
        """
        self.search_element(loc, timeout, poll_frequency).click()

    def send_element(self, loc, text, timeout=10, poll_frequency=1):
        """
        输入元素
        :param loc: 祖定位类型 (By.ID,ID属性值) (By.XPATH,XPATH属性值) (By.CLASS_NAME,CLASS_NAME属性值)
        :param text: 发送文本
        :param timeout: 超时时间
        :param poll_frequency: 搜索元素间隔
        :return:
        """
        input_data = self.search_element(loc, timeout, poll_frequency)
        # 清空输入框
        input_data.clear()
        # 输入
        input_data.send_keys(text)