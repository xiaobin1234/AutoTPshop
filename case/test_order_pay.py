import unittest
# 定义测试类
import time

from config import BASE_DIR
from page.index_page import IndexProxy
from page.my_order_page import MyOrderProxy
from page.order_pay_page import OrderPayProxy
from proxy_utils import ProxyUtils
from utils import UtilsDriver


class TestOrderPay(unittest.TestCase):
    # 定义类级别Fixture初始化
    @classmethod
    def setUpClass(cls):
        cls.driver = UtilsDriver.get_driver()
        cls.index_proxy = IndexProxy()
        cls.my_order_proxy = MyOrderProxy()
        cls.order_pay_proxy = OrderPayProxy()
        cls.proxy_utils = ProxyUtils()
        cls.driver.get("http://127.0.0.1/")
        cls.proxy_utils.proxy_login()

    # 定义方法级别Fixture初始化
    def setUp(self):
        self.driver.get("http://127.0.0.1/")
        time.sleep(3)
        self.index_proxy.go_my_order()

    @classmethod
    def tearDownClass(cls):
        UtilsDriver.quit_driver()
    # 定义测试方法
    def test_order_pay(self):
        try:
            self.my_order_proxy.go_to_pay()
            time.sleep(3)
            msg = self.order_pay_proxy.go_pay_success()
            self.assertIn("我们将在第一时间给你发货", msg)
        except Exception as f:
            filename = (BASE_DIR + '/img/error_img_{}.png'.format(time.strftime("%Y%m%d%H%M%S")))
            self.driver.get_screenshot_as_file(filename)
            raise f