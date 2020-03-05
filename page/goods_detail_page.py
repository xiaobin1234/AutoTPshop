# 商品详情页面
import time
from selenium.webdriver.common.by import By

from base.basepage import BasePage, BaseHandle


# 定义对象库层
class GoodsDetailPage(BasePage):
    def __init__(self):
        super().__init__()
        # 加入购物车按钮
        self.add_car = (By.CSS_SELECTOR, ".addcar")

        # 弹窗的iframe元素
        self.content_iframe = (By.CSS_SELECTOR, "#layui-layer-iframe1")

        # 添加成功之后的弹窗信息
        self.content_title = (By.CSS_SELECTOR, ".conect-title>span")

        # 进入到购物车
        self.go_add_car= (By.CSS_SELECTOR, ".ui-button-122")

    # 定位加入购物车按钮
    def find_add_car(self):
        return self.find_element(self.add_car)

    # 定位iframe
    def find_content_frame(self):
        return self.find_element(self.content_iframe)

    # 定位弹窗信息框
    def find_content_title(self):
        return self.find_element(self.content_title)

    # 定位进入到购物车按钮
    def find_go_add_car(self):
        return self.find_element(self.go_add_car)

# 定义操作层
class GoodsDetailHandle(BaseHandle):
    def __init__(self):
        self.goods_detail_page = GoodsDetailPage()

    # 点击加入购物车按钮
    def click_add_car(self):
        self.goods_detail_page.find_add_car().click()

    # 切换iframe
    def change_iframe(self):
        self.goods_detail_page.driver.switch_to.frame(self.goods_detail_page.find_content_frame())

    # 获取弹出框的信息
    def get_content_title(self):
        return self.goods_detail_page.find_content_title().text

    # 点击去购物车结算按钮
    def click_go_add_car(self):
        self.goods_detail_page.find_go_add_car().click()

# 定义业务层
class GoodsDetailProxy:
    def __init__(self):
        self.goods_detail_handle = GoodsDetailHandle()

    # 添加商品到购物车
    def add_car(self):
        # 点击加入购物车按钮
        self.goods_detail_handle.click_add_car()
        # 切换iframe
        self.goods_detail_handle.change_iframe()
        time.sleep(3)
        # 获取弹出框信息
        msg = self.goods_detail_handle.get_content_title()
        # 点击去购物车结算按钮
        self.goods_detail_handle.click_go_add_car()
        # self.goods_detail_handle.goods_detail_page.driver.switch_to.default_content()
        return msg