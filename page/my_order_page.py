# 我的订单页面
# 对象层
from selenium.webdriver.common.by import By

from base.basepage import BasePage, BaseHandle, BaseProxy


class MyOrderPage(BasePage):
    def __init__(self):
        super().__init__()
        # 待付款
        self.wait_pay = (By.CSS_SELECTOR, ".selected")
        # 立即支付
        self.right_pay = (By.CSS_SELECTOR, ".ps_lj")
    # 定位待付款
    def find_wait_pay(self):
        return self.find_element(self.wait_pay)
    # 定位立即支付
    def find_right_pay(self):
        return self.find_element(self.right_pay)

# 操作层
class MyOrderHadle(BaseHandle):
    def __init__(self):
        self.my_order_page = MyOrderPage()
    # 点击待付款
    def click_wait_pay(self):
        self.my_order_page.find_wait_pay().click()
    # 点击立即支付
    def click_right_pay(self):
        self.my_order_page.find_right_pay().click()

# 业务层
class MyOrderProxy(BaseProxy):
    def __init__(self):
        super().__init__()
        self.my_order_handle = MyOrderHadle()
    # 业务操作:点击待付款,点击立即支付
    def go_to_pay(self):
        # 获取句柄
        self.switch_window()
        # 点击待付款
        self.my_order_handle.click_wait_pay()
        # 点击立即支付
        self.my_order_handle.click_right_pay()