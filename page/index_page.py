# 首页页面对象
import time
from selenium.webdriver.common.by import By

from base.basepage import BasePage, BaseHandle

# 定义对象库层
class IndexPage(BasePage):
    # 通过调用super重写初始化方法，便于调用基类中的相关方法
    def __init__(self):
        super().__init__()
        # 登陆按钮
        self.go_login_btn =(By.CSS_SELECTOR, '.red')
        # 搜索框
        self.search_k = (By.CSS_SELECTOR, ".ecsc-search-input")
        # 搜索按钮
        self.search_btn = (By.CSS_SELECTOR, ".ecsc-search-button")
        # 搜索出来的第一个商品图片链接
        self.search_one_img = (By.XPATH, "//*[@class='s_xsall']/div/a")
        # 我的购物车
        self.my_card = (By.CSS_SELECTOR, ".share-shopcar-index")
        # 我的订单
        self.my_order = (By.XPATH, "//*[@class='top-ri-header fr clearfix' ]/li/a")

    # 定位首页中的登陆按钮
    def find_login_link(self):
        return self.find_element(self.go_login_btn)
    # 定位搜索框
    def find_search_k(self):
        return self.find_element(self.search_k)
    # 定位搜索按钮
    def find_search_btn(self):
        return self.find_element(self.search_btn)
    # 定位搜索出来的第一个商品图片
    def find_search_one_img(self):
        return self.find_element(self.search_one_img)

    # 定位我的购物车
    def find_my_card(self):
        return self.find_element(self.my_card)

    # 定位我的订单
    def find_my_order(self):
        return self.find_element(self.my_order)

# 定义操作层
class IndexHandle(BaseHandle):
    def __init__(self):
        self.index_page = IndexPage()
    # 针对登陆按钮进行点击操作
    def click_login_link(self):
        self.index_page.find_login_link().click()
    # 针对搜索框进行输入操作
    def input_search_k(self, text):
        self.input_text(self.index_page.find_search_k(), text)
    # 针对搜索按钮进行点击操作
    def click_search_btn(self):
        self.index_page.find_search_btn().click()
    # 针对第一个搜索出来的图片进行点击操作
    def click_one_img(self):
        self.index_page.find_search_one_img().click()

    # 点击我的购物车
    def click_my_card(self):
        self.index_page.find_my_card().click()

    # 点击我的订单
    def click_my_order(self):
        self.index_page.find_my_order().click()

# 定义业务层
class IndexProxy:
    def __init__(self):
        self.index_handle = IndexHandle()

    # 业务操作：点击登陆按钮跳转到登陆页面
    def go_login_link(self):
        self.index_handle.click_login_link()

    # 业务操作：输入搜索内容进行搜索
    def search_goods(self, text):
        # 输入要搜索的商品
        self.index_handle.input_search_k(text)
        # 点击搜索按钮
        self.index_handle.click_search_btn()
        # 点击搜索的第一个商品图片进入到商品详情页
        self.index_handle.click_one_img()
        time.sleep(5)

    # 业务操作:点击我的购物车
    def go_my_card(self):
        self.index_handle.click_my_card()

    # 业务:点击我的订单跳转页面
    def go_my_order(self):
        self.index_handle.click_my_order()