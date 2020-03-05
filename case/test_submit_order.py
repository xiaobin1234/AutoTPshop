import unittest
# 定义测试类
import time

from config import BASE_DIR
from page.index_page import IndexProxy
from page.order_pay_page import OrderPayProxy
from page.shop_card_page import ShopCardProxy
from page.submit_order_page import SubmitOrderProxy
from proxy_utils import ProxyUtils
from utils import UtilsDriver


class TestSunbmitOrder(unittest.TestCase):
    # 定义类级别的Fixture初始化
    @classmethod
    def setUpClass(cls):
        cls.driver = UtilsDriver.get_driver()
        cls.index_proxy = IndexProxy()
        cls.shop_card_proxy = ShopCardProxy()
        cls.submit_order_proxy = SubmitOrderProxy()
        cls.order_pay_proxy = OrderPayProxy()
        cls.proxy_utils = ProxyUtils()
        cls.driver.get("http://127.0.0.1/")
        cls.proxy_utils.proxy_login()

    # 定义方法级别的Fixture初始化
    def setUp(self):
        self.driver.get("http://127.0.0.1/")

    @classmethod
    def tearDownClass(cls):
        UtilsDriver.quit_driver()
    # 定义测试方法
    def test_submit_order(self):
        try:
            self.index_proxy.go_my_card()
            time.sleep(3)
            self.shop_card_proxy.click_all()
            time.sleep(3)
            self.submit_order_proxy.go_to_submit()
            time.sleep(3)
            msg = self.order_pay_proxy.get_pay_msg()
            self.assertIn("订单提交成功", msg)
        except Exception as f:
            filename = (BASE_DIR + '/img/error_img_{}.png'.format(time.strftime("%Y%m%d%H%M%S")))
            self.driver.get_screenshot_as_file(filename)
            raise f