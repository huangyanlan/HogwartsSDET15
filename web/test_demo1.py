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
        # self.driver.implicitly_wait(3)

    def teardown_method(self, method):
        self.driver.quit()

    def test_testdemo(self):
        self.driver.get("https://www.baidu.com/")

    def test_weixin(self):
        self.driver.find_element(By.ID, "menu_contacts").click()

        sleep(3)

    def test_cookie(self):
        # get_cookies()可以获得当前打开的页面的cookie
        # cookies = self.driver.get_cookies()
        cookies = [
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'Hm_lpvt_eaa57ca47dacb4ad4f5a257001a3457c',
             'path': '/', 'secure': False, 'value': '1604408177'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False,
             'value': '1688853097024424'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False,
             'value': '3zBULMCGGcZIVXXuIxv01X0LqWScvfxM_gJ03CQm7yvxq3EGezfNiLAxhwWSylRQMi48dwqXCwHicts0jpsG4Wp4dgLBrYADHjzh5wFeFuniMjKwLjRfircZsSYGYhsuR98YX0k1po0YFfUWVISGwpB6t-zhQvktfPEjaijEJasVOXTDYaoYly4NKmnAbs52O8_0jl_m9e3fJM-8CSWxkZzSvYKjvR1H3Pd1B22ojg0bRuWf_ILKcJ_rovywXFlyzBMy9wrvLabcZ0AlGsi_cQ'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False,
             'value': '1688853097024424'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False,
             'value': '1970325031172040'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False,
             'value': 'kfCYjTrXONVB8hL1jJuKf5Moq2CBpVkWDIEBtGLxVt41bDwizwOx5lA9vT0eaBnc'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False,
             'value': 'a6039789'}, {'domain': '.work.weixin.qq.com', 'expiry': 1635944176, 'httpOnly': False,
                                    'name': 'Hm_lvt_eaa57ca47dacb4ad4f5a257001a3457c', 'path': '/', 'secure': False,
                                    'value': '1604406551,1604407521,1604407991,1604408164'},
            {'domain': 'work.weixin.qq.com', 'expiry': 1604438078, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/',
             'secure': False, 'value': '5ppi58h'},
            {'domain': '.qq.com', 'expiry': 1604494571, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False,
             'value': 'GA1.2.2065155519.1604321625'},
            {'domain': '.qq.com', 'expiry': 1667480171, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False,
             'value': 'GA1.2.1094890820.1604321625'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1635857619, 'httpOnly': False, 'name': 'wwrtx.c_gdpr',
             'path': '/', 'secure': False, 'value': '0'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1607000243, 'httpOnly': False, 'name': 'wwrtx.i18n_lan',
             'path': '/', 'secure': False, 'value': 'zh'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False,
             'value': '1'}, {'domain': '.work.weixin.qq.com', 'expiry': 1635944156, 'httpOnly': False,
                             'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False,
                             'value': '1604407514,1604407984,1604408130,1604408157'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False,
             'value': 'direct'},
            {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/',
             'secure': False, 'value': '944084030'},
            {'domain': '.qq.com', 'expiry': 2147483649, 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'secure': False,
             'value': 'd2f7fb5dbe0547cfbc5b80e08758935fe7003368dfba5dd4d7e0eefa047cce46'},
            {'domain': '.qq.com', 'expiry': 2147483649, 'httpOnly': False, 'name': 'RK', 'path': '/', 'secure': False,
             'value': '4rZoVzB8OS'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d',
             'path': '/', 'secure': False, 'value': '1604408157'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False,
             'value': '2971283227335579'},
            {'domain': '.qq.com', 'expiry': 1604408290, 'httpOnly': False, 'name': '_gat', 'path': '/', 'secure': False,
             'value': '1'},
            {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvi', 'path': '/',
             'secure': False, 'value': '1242882048'}]

        # shelve python 的内置模块，专门用来对对数据持久化存储的库，相当于小型的数据库
        # 可以通过键值来key，value 来把数据存储到shelve
        # db = shelve.open(cookies)
        # db['cookie'] = cookies
        # db.close()
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")

        for cookie in cookies:
            self.driver.add_cookie(cookie)

        self.driver.refresh()
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")

        print(cookies)

    def test_shelve(self):
        # cookies = [{'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'Hm_lpvt_eaa57ca47dacb4ad4f5a257001a3457c', 'path': '/', 'secure': False, 'value': '1604408177'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False, 'value': '1688853097024424'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False, 'value': '3zBULMCGGcZIVXXuIxv01X0LqWScvfxM_gJ03CQm7yvxq3EGezfNiLAxhwWSylRQMi48dwqXCwHicts0jpsG4Wp4dgLBrYADHjzh5wFeFuniMjKwLjRfircZsSYGYhsuR98YX0k1po0YFfUWVISGwpB6t-zhQvktfPEjaijEJasVOXTDYaoYly4NKmnAbs52O8_0jl_m9e3fJM-8CSWxkZzSvYKjvR1H3Pd1B22ojg0bRuWf_ILKcJ_rovywXFlyzBMy9wrvLabcZ0AlGsi_cQ'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False, 'value': '1688853097024424'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False, 'value': '1970325031172040'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False, 'value': 'kfCYjTrXONVB8hL1jJuKf5Moq2CBpVkWDIEBtGLxVt41bDwizwOx5lA9vT0eaBnc'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False, 'value': 'a6039789'}, {'domain': '.work.weixin.qq.com', 'expiry': 1635944176, 'httpOnly': False, 'name': 'Hm_lvt_eaa57ca47dacb4ad4f5a257001a3457c', 'path': '/', 'secure': False, 'value': '1604406551,1604407521,1604407991,1604408164'}, {'domain': 'work.weixin.qq.com', 'expiry': 1604438078, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/', 'secure': False, 'value': '5ppi58h'}, {'domain': '.qq.com', 'expiry': 1604494571, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False, 'value': 'GA1.2.2065155519.1604321625'}, {'domain': '.qq.com', 'expiry': 1667480171, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False, 'value': 'GA1.2.1094890820.1604321625'}, {'domain': '.work.weixin.qq.com', 'expiry': 1635857619, 'httpOnly': False, 'name': 'wwrtx.c_gdpr', 'path': '/', 'secure': False, 'value': '0'}, {'domain': '.work.weixin.qq.com', 'expiry': 1607000243, 'httpOnly': False, 'name': 'wwrtx.i18n_lan', 'path': '/', 'secure': False, 'value': 'zh'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.work.weixin.qq.com', 'expiry': 1635944156, 'httpOnly': False, 'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1604407514,1604407984,1604408130,1604408157'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False, 'value': 'direct'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/', 'secure': False, 'value': '944084030'}, {'domain': '.qq.com', 'expiry': 2147483649, 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'secure': False, 'value': 'd2f7fb5dbe0547cfbc5b80e08758935fe7003368dfba5dd4d7e0eefa047cce46'}, {'domain': '.qq.com', 'expiry': 2147483649, 'httpOnly': False, 'name': 'RK', 'path': '/', 'secure': False, 'value': '4rZoVzB8OS'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1604408157'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False, 'value': '2971283227335579'}, {'domain': '.qq.com', 'expiry': 1604408290, 'httpOnly': False, 'name': '_gat', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvi', 'path': '/', 'secure': False, 'value': '1242882048'}]
        db = shelve.open("cookies")
        cookies = db['cookie']

        db.close()

        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")

        for cookie in cookies:
            self.driver.add_cookie(cookie)

        self.driver.refresh()

        sleep(3)

        self.driver.find_element(By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(2)").click()

        self.driver.find_element(By.CSS_SELECTOR, ".ww_fileImporter_fileContainer_uploadInputMask").send_keys(
            "C:/Users/hyl/Documents/工作汇总表.xlsx")
        #
        filename = self.driver.find_element(By.CSS_SELECTOR, ".ww_fileImporter_fileContainer_fileNames").text
        #
        assert filename == "工作汇总表.xlsx"

        sleep(5)
