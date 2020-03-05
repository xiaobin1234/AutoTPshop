# 购物车页面对象
import time
from selenium.webdriver.common.by import By

from base.basepage import BasePage, BaseHandle


# 定义对象库层
class ShopCardPage(BasePage):
    def __init__(self):
        super().__init__()
        # 获取购物车第一个商品信息
        self.one_goods_name =(By.XPATH, "//p[@class='gwc-ys-pp'][1]/a")
        # 获取全选按钮
        self.check_all = (By.CSS_SELECTOR, ".checkCartAll")
        # 去结算按钮
        self.go_submit = (By.CSS_SELECTOR, ".gwc-qjs")

    # 获取购物车商品第一个元素
    def find_one_goods_name(self):
        return self.find_element(self.one_goods_name)
    # 获取全选按钮
    def find_check_all(self):
        return self.find_element(self.check_all)
    # 获取去结算按钮
    def find_go_submit(self):
        return self.find_element(self.go_submit)

# 定义操作层
class ShopCardHandle(BaseHandle):
    def __init__(self):
        self.shop_card_page = ShopCardPage()
    # 获取购物车第一个商品信息
    def get_one_goods_name(self):
        return self.shop_card_page.find_one_goods_name().text

    # 点击全选按钮
    def click_check_all(self):
        self.shop_card_page.find_check_all().click()
        self.shop_card_page.find_check_all().click()
    # 点击去结算按钮
    def click_go_submit(self):
        self.shop_card_page.find_go_submit().click()

# 定义业务层
class ShopCardProxy:
    def __init__(self):
        self.shop_card_handle = ShopCardHandle()
    # 业务操作:获取购物车第一个商品信息
    def get_one_goods_info(self):
        return self.shop_card_handle.get_one_goods_name()

    # 业务操作:点击全选按钮,点击去结算按钮
    def click_all(self):
        # 点击全选按钮
        self.shop_card_handle.click_check_all()
        # 点击去结算按钮
        self.shop_card_handle.click_go_submit()
        time.sleep(5)