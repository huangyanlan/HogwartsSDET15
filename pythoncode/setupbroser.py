from selenium import webdriver
import os


class Base:
    def setup(self):
        # 要将broser设置为环境变量，然后通过os.getenv来获取
        browser = os.getenv('browser')
        if browser == 'Chrome':
            self.driver = webdriver.Chrome()
        elif browser == 'Firefox':
            self.driver = webdriver.Firefox()

        self.driver.maximize_window()
        self.driver.implicitly_wait(60)

    def teardown(self):
        self.driver.quit()
