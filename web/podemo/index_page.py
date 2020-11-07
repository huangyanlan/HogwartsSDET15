from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

from web.podemo.login_page import LoginPage
from web.podemo.register_page import RegisterPage


class IndexPage:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://work.weixin.qq.com/")

    # 进入登录页
    def goto_login(self):
        # click loing
        self.driver.find_element(By.CSS_SELECTOR, ".index_top_operation_loginBtn").click()
        # return loginPage
        return LoginPage(self.driver)

    # 进入到注册页
    def goto_register(self):
        # click loing
        self.driver.find_element(By.CSS_SELECTOR, ".index_head_info_pCDownloadBtn").click()
        # return registerPage
        return RegisterPage(self.driver)
