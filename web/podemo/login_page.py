from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class LoginPage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    # 扫码
    def scan(self):
        pass

    # 进入到注册页面
    def goto_register(self):
        self.driver.find_element(By.CSS_SELECTOR, ".login_registerBar_link")
        return
