# 登陆页面对象
from selenium.webdriver.common.by import By

from base.basepage import BasePage, BaseHandle
# 定义对象库层
class LoginPage(BasePage):
    def __init__(self):
        super().__init__()
        # 用户名
        self.username = (By.CSS_SELECTOR, "#username")
        # 密码
        self.password=(By.CSS_SELECTOR, "#password")
        # 验证码
        self.code = (By.CSS_SELECTOR, "#verify_code")
        # 登陆按钮
        self.login_btn = (By.CSS_SELECTOR, ".J-login-submit")

    # 定位用户名输入框
    def find_username(self):
        return self.find_element(self.username)

    # 定位密码输入框
    def find_password(self):
        return self.find_element(self.password)

    # 定位验证码输入框
    def find_code(self):
        return self.find_element(self.code)

    # 定位登陆按钮
    def find_login_btn(self):
        return self.find_element(self.login_btn)

# 定义操作层
class LoginHandle(BaseHandle):
    def __init__(self):
        self.login_page = LoginPage()

    # 输入用户名
    def input_username(self, username):
        self.input_text(self.login_page.find_username(), username)
    # 输入密码
    def input_password(self, password):
        self.input_text(self.login_page.find_password(), password)
    # 输入验证码
    def input_code(self, code):
        self.input_text(self.login_page.find_code(), code)
    # 点击登陆按钮
    def click_login_btn(self):
        self.login_page.find_login_btn().click()
# 定义业务层
class LoginProxy:
    def __init__(self):
        self.login_handle = LoginHandle()

    # 业务操作：组合四个元素的操作业务形成登陆功能。
    def login(self, username, password, code):
        # 输入用户名
        self.login_handle.input_username(username)
        # 输入密码
        self.login_handle.input_password(password)
        # 输入验证码
        self.login_handle.input_code(code)
        # 点击登陆按钮
        self.login_handle.click_login_btn()