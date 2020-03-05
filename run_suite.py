#导包
import os
import unittest
import time
from HTMLTestRunner_PY3 import HTMLTestRunner

from case.test_add_card import TestAddCard
from case.test_login import TestLogin
from case.test_order_pay import TestOrderPay
from case.test_submit_order import TestSunbmitOrder
from config import BASE_DIR

# 创建suite对象
# suite = unittest.TestLoader().discover(BASE_DIR + "/case", pattern="test*.py")
suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestLogin))
suite.addTest(unittest.makeSuite(TestAddCard))
suite.addTest(unittest.makeSuite(TestSunbmitOrder))
suite.addTest(unittest.makeSuite(TestOrderPay))

# 创建测试报告文件
# filename = './report/test_report_{}.html'.format(time.strftime("%Y%m%d%H%M%S"))
filename = os.path.dirname(os.path.abspath(__file__)) + './report/test_report.html'
# 打开测试报告文件
with open(filename, 'wb') as f:
    runner = HTMLTestRunner(stream=f, title="tpshop", description="win7- Chrome7.8")
    runner.run(suite)