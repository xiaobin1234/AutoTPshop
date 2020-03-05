import json
import random
import time

from selenium import webdriver

# 定义工具类名：
from selenium.webdriver.common.by import By


class UtilsDriver:
    _driver = None
    # 判断是否退出浏览器驱动对象
    is_quit = True
    # 定义获取浏览器驱动对象的方法
    @classmethod
    def get_driver(cls):
        if cls._driver is None:
            cls._driver = webdriver.Chrome()
            cls._driver.maximize_window()
            cls._driver.implicitly_wait(10)
        return cls._driver

    @classmethod
    def quit_driver(cls):
        if cls.is_quit and cls._driver is not None:
            cls.get_driver().quit()
            cls._driver = None

def get_tip_msg():
    time.sleep(3)
    msg = UtilsDriver.get_driver().find_element(By.CSS_SELECTOR, ".layui-layer-content").text
    return msg

def get_case_data(filename):
    with open(filename, encoding="utf-8") as f:
        case_data = json.load(f)
    list_case = []
    for data in case_data.values():
        list_case.append(tuple(data.values()))
    return list_case

def get_mobile():
    mobiles = ['134','135','136','137']
    m_str = str(int(time.time()))[2:]
    mobile = random.choice(mobiles)+m_str
    return mobile
