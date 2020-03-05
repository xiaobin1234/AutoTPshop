from selenium.webdriver import ActionChains

from utils import UtilsDriver

# 定义对像库层的基类
class BasePage:
    def __init__(self):
        self.driver = UtilsDriver.get_driver()

    # 定义一个定位元素的方法
    def find_element(self, location):
        return self.driver.find_element(location[0], location[1])

# 定义操作层基类
class BaseHandle:
    # 针对元素的输入操作
    def input_text(self, element, text):
        element.clear()
        element.send_keys(text)

    # 针对元素的右击操作
    def context_click(self, driver, element):
        action = ActionChains(driver)
        action.context_click(element)
        action.perform()
# 定义业务层基类
class BaseProxy:
    def __init__(self):
        self.driver = UtilsDriver.get_driver()

    # 切换窗口
    def switch_window(self):
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])
