import shelve
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


class TestTestdemo():
    def setup_method(self, method):
        # options = Options()
        # options.debugger_address = "127.0.0.1:9222"
        # self.driver = webdriver.Chrome(options=options)
        options = Options()
        options.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome()  # options=options
        self.driver.implicitly_wait(3)

    def teardown_method(self, method):
        self.driver.quit()

    def test_testdemo(self):
        self.driver.get("https://www.baidu.com/")

    def test_weixin(self):
        self.driver.find_element(By.ID, "menu_contacts").click()

    def test_cookie(self):
        # get_cookies()可以获得当前打开的页面的cookie
        # cookies = self.driver.get_cookies()
        cookies = [
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'Hm_lpvt_eaa57ca47dacb4ad4f5a257001a3457c',
             'path': '/', 'secure': False, 'value': '1604323877'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False,
             'value': '1688853097024424'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False,
             'value': 'wWw_95QTlmba-Ra4VkMKyieV7I1ioIMlKNPVzG9FAGAR34N5vWWrOrE6_XoSzug5Y7HLSgv4CPUe53ai_2iGDq464TJcTI4M__qqIyWozXmWGB3F-pYHkBcCgt0i5ZrIX47vbOdezVGMEgACawzvPmolNf6RloqOmieF5K105xQS50Y1PPDnUr1skhvCJOCWAEWAiK1t_icLGBHNlXbnNx7AWaS3RLErFi2c2dNzhrzEEe0aIilFbfhfBogN3BvFs93_oQ8QSkHhFp7JsK-ykw'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False,
             'value': '1688853097024424'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False,
             'value': '1970325031172040'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False,
             'value': 'kfCYjTrXONVB8hL1jJuKf2wu55gIP84KA7XJFw6waNj2bz5GCMJDasQT5zZBg6cT'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False,
             'value': 'a1135994'}, {'domain': '.work.weixin.qq.com', 'expiry': 1635859876, 'httpOnly': False,
                                    'name': 'Hm_lvt_eaa57ca47dacb4ad4f5a257001a3457c', 'path': '/', 'secure': False,
                                    'value': '1604321627,1604321798,1604321836,1604323384'},
            {'domain': 'work.weixin.qq.com', 'expiry': 1604353155, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/',
             'secure': False, 'value': '1hmup1s'},
            {'domain': '.qq.com', 'expiry': 1604410271, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False,
             'value': 'GA1.2.2065155519.1604321625'},
            {'domain': '.qq.com', 'expiry': 1667395871, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False,
             'value': 'GA1.2.1094890820.1604321625'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1635857619, 'httpOnly': False, 'name': 'wwrtx.c_gdpr',
             'path': '/', 'secure': False, 'value': '0'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1606915874, 'httpOnly': False, 'name': 'wwrtx.i18n_lan',
             'path': '/', 'secure': False, 'value': 'zh'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False,
             'value': '1'}, {'domain': '.work.weixin.qq.com', 'expiry': 1635859376, 'httpOnly': False,
                             'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False,
                             'value': '1604321637,1604322004,1604322358,1604323376'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False,
             'value': 'direct'},
            {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/',
             'secure': False, 'value': '944084030'},
            {'domain': '.qq.com', 'expiry': 2147483649, 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'secure': False,
             'value': 'd2f7fb5dbe0547cfbc5b80e08758935fe7003368dfba5dd4d7e0eefa047cce46'},
            {'domain': '.qq.com', 'expiry': 2147483649, 'httpOnly': False, 'name': 'RK', 'path': '/', 'secure': False,
             'value': '4rZoVzB8OS'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d',
             'path': '/', 'secure': False, 'value': '1604323376'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False,
             'value': '29712832271372959'},
            {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvi', 'path': '/',
             'secure': False, 'value': '1242882048'}]

        # shelve python 的内置模块，专门用来对对数据持久化存储的库，相当于小型的数据库
        # 可以通过键值来key，value 来把数据存储到shelve
        db = shelve.open(cookies)
        db['cookie'] = cookies
        db.close()
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")

        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")

        print(cookies)
