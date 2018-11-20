from selenium.webdriver.common.by import By

# 点击短信
add_sms_btn_byid = (By.ID, "com.android.mms:id/action_compose_new")
# 输入电话号码
send_phone_btn_byid = (By.ID, "com.android.mms:id/recipients_editor")
# 输入短信内容
send_sms_btn_byid = (By.ID, "com.android.mms:id/embedded_text_editor")
# 点击发送按钮
send_btn_byid = (By.ID, "com.android.mms:id/send_button_sms")
# 获取文本内容
text_byids = (By.ID, "com.android.mms:id/text_view")

'''设置界面'''
#点击更多
more_btn_xpath =(By.XPATH,"//*[contains(@text,'更多')]")
'''更多界面'''
#点击移动网络
network_btn_xpath = (By.XPATH,"//*[contains(@text,'移动网络')]")
'''移动网络设置界面'''
#点击首选网络类型
network_type_btn_xpath = (By.XPATH,"//*[contains(@text,'首选网络类型')]")
# 3G网络按钮
select_3G_btn_xpath = (By.XPATH, "//*[contains(@text,'3G')]")
#定位3G列表
select_3G_btn_by_ids = (By.ID, "android:id/summary")

