# 提交订单页面
from selenium.webdriver.common.by import By

from base.basepage import BasePage, BaseHandle


# 定义对象层
class SubmitOrderPage(BasePage):
    def __init__(self):
        super().__init__()
        # 提交订单
        self.submit_order_btn = (By.CSS_SELECTOR, ".gwc-qjs")
    # 定位提交订单按钮
    def find_submit_order_btn(self):
        return self.find_element(self.submit_order_btn)

# 定义操作层
class SubmitOrderHandle(BaseHandle):
    def __init__(self):
        self.submit_order_page = SubmitOrderPage()
    # 点击提交按钮
    def click_submit_order_btn(self):
        self.submit_order_page.find_submit_order_btn().click()

# 定义业务层
class SubmitOrderProxy:
    def __init__(self):
        self.submit_order_handle = SubmitOrderHandle()
    # 业务:点击提交按钮
    def go_to_submit(self):
        self.submit_order_handle.click_submit_order_btn()