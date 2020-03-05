#导包
import unittest
import time
from HTMLTestRunner_PY3 import HTMLTestRunner

from config import BASE_DIR

# 创建suite对象
suite = unittest.TestLoader().discover(BASE_DIR + "/case", pattern="test*.py")

# 创建测试报告文件
filename = './report/test_report_{}.html'.format(time.strftime("%Y%m%d%H%M%S"))
# 打开测试报告文件
with open(filename, 'wb') as f:
    runner = HTMLTestRunner(stream=f, title="tpshop", description="win7- Chrome7.8")
    runner.run(suite)