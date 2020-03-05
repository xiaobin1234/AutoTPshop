import time

from page.index_page import IndexProxy
from page.login_page import LoginProxy


class ProxyUtils:
    def __init__(self):
        self.index_proxy = IndexProxy()
        self.login_proxy = LoginProxy()

    def proxy_login(self):
        self.index_proxy.go_login_link()
        self.login_proxy.login("13838384388", "123456", "8888")
        time.sleep(5)