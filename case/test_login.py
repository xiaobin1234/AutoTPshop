#导包
import logging
import unittest
#定义测试类
import time

from parameterized import parameterized

from config import BASE_DIR
from page.index_page import IndexProxy
from page.login_page import LoginProxy
from utils import UtilsDriver, get_case_data, get_tip_msg

case_data = get_case_data(BASE_DIR+"/data/login_case.json")
class TestLogin(unittest.TestCase):
    # 定义类级别的Fixture实现
    @classmethod
    def setUpClass(cls):
        cls.driver = UtilsDriver.get_driver()
        cls.index_proxy=IndexProxy()
        cls.login_proxy=LoginProxy()


    def setUp(self):
        self.driver.get("http://127.0.0.1/")
        self.index_proxy.go_login_link()

    @classmethod
    def tearDownClass(cls):
        UtilsDriver.quit_driver()

    #定义测试方法
    @parameterized.expand(case_data)
    def test_login_01(self, username, password, code, expect, is_success):
        try:
            self.login_proxy.login(username, password, code)
            if is_success:
                time.sleep(5)
                msg = self.driver.title
            else:
                msg = get_tip_msg()
            self.assertIn(expect, msg)
        except Exception as e:
            filename = (BASE_DIR + '/img/error_img_{}.png'.format(time.strftime("%Y%m%d%H%M%S")))
            self.driver.get_screenshot_as_file(filename)
            raise e
