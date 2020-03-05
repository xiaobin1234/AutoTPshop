# 订单支付页面PO封装
# 对象层
import time
from selenium.webdriver.common.by import By

from base.basepage import BasePage, BaseHandle, BaseProxy


class OrderPayPage(BasePage):
    def __init__(self):
        super().__init__()
        # 获取订单提交成功信息
        self.submit_order_msg = (By.CSS_SELECTOR, ".erhuh h3")
        # 货到付款
        self.pay_type_cod = (By.CSS_SELECTOR, "[value='pay_code=cod']")
        # 确认支付方式
        self.submit_pay_btn = (By.CSS_SELECTOR, ".button-style-5")

    # 定位提交成功信息元素
    def find_submit_order_msg(self):
        return self.find_element(self.submit_order_msg)

    # 定位货到付款
    def find_pay_type_cod(self):
        return self.find_element(self.pay_type_cod)
    # 定位确认支付方式
    def find_submit_pay_btn(self):
        return self.find_element(self.submit_pay_btn)

# 操作层
class OrderPayHandle(BaseHandle):
    def __init__(self):
        self.order_pay_page = OrderPayPage()
    # 获取提交成功信息
    def get_submit_order_msg(self):
        return self.order_pay_page.find_submit_order_msg().text

    # 点击货到付款
    def click_pay_type_cod(self):
        self.order_pay_page.find_pay_type_cod().click()
    # 点击确认支付方式
    def click_submit_pay_btn(self):
        self.order_pay_page.find_submit_pay_btn().click()

# 业务层
class OrderPayProxy(BaseProxy):
    def __init__(self):
        super().__init__()
        self.order_pay_handle = OrderPayHandle()
    # 业务:获取提交成功信息
    def get_pay_msg(self):
        msg = self.order_pay_handle.get_submit_order_msg()
        return msg

    # 业务:点击货到付款,点击确认支付方式,获取订单提交成功信息
    def go_pay_success(self):
        # 获取句柄
        self.switch_window()
        # 点击货到付款
        time.sleep(5)
        self.order_pay_handle.click_pay_type_cod()
        # 点击确认支付方式
        time.sleep(5)
        self.order_pay_handle.click_submit_pay_btn()
        # 获取订单提交成功信息
        time.sleep(5)
        msg = self.order_pay_handle.get_submit_order_msg()
        return msg