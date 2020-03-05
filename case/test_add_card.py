#导包
import logging
import unittest
#定义测试类
import time
from parameterized import parameterized
from selenium.webdriver.common.by import By

from config import BASE_DIR
from page.goods_detail_page import GoodsDetailProxy

from page.index_page import IndexProxy
from page.shop_card_page import ShopCardProxy
from proxy_utils import ProxyUtils
from utils import UtilsDriver, get_case_data

add_card_data = get_case_data(BASE_DIR+'/data/addCard_case.json')
class TestAddCard(unittest.TestCase):
    # 类级别的Fixture实现
    @classmethod
    def setUpClass(cls):
        cls.driver = UtilsDriver.get_driver()
        cls.index_proxy = IndexProxy()
        cls.goods_detail_proxy = GoodsDetailProxy()
        cls.shop_card_proxy = ShopCardProxy()
        cls.proxy_utils = ProxyUtils()
        cls.driver.get("http://127.0.0.1/")
        cls.proxy_utils.proxy_login()

    def setUp(self):
        self.driver.get("http://127.0.0.1/")

    @classmethod
    def tearDownClass(cls):
        UtilsDriver.quit_driver()

    # 定义测试方法
    @parameterized.expand(add_card_data)
    def test_add_card(self, apple, expect):
        try:
            self.index_proxy.search_goods(apple)
            msg = self.goods_detail_proxy.add_car()
            self.assertIn(expect, msg)
            time.sleep(3)
            name = self.shop_card_proxy.get_one_goods_info()
            self.assertIn(apple.upper(), name.upper())
        except Exception as f:
            filename = (BASE_DIR + '/img/error_img_{}.png'.format(time.strftime("%Y%m%d%H%M%S")))
            self.driver.get_screenshot_as_file(filename)
            raise f


