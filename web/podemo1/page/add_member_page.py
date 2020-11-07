from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from web.podemo1.page.base_page import BasePage


class AddMemberPage(BasePage):

    # def __init__(self,driver:WebDriver):
    #     self.driver = driver

    def add_member(self, username, acount, phone):

        # username="aaaaa"
        # acount = "aaaa_hyl"
        # phone = "12450090909"
        # sleep(6)

        self.find(By.ID, "username").send_keys(username)

        self.find(By.ID, "memberAdd_acctid").send_keys(acount)
        self.find(By.ID, "memberAdd_phone").send_keys(phone)
        self.find(By.CSS_SELECTOR, ".js_btn_save").click()
        checkbox = (By.CSS_SELECTOR, ".ww_checkbox")
        self.wait_for_click(checkbox)
        # sleep(3)
        return True

    def get_member(self, value):

        # contactlist = self.finds(By.CSS_SELECTOR,".member_colRight_memberTable_td:nth-child(2)")
        # titlelist=[element.get_attribute("title") for element in contactlist]

        total_list = []
        while True:
            contactlist = self.finds(By.CSS_SELECTOR, '.member_colRight_memberTable_td:nth-child(2)')
            titlelist = [element.get_attribute("title") for element in contactlist]
            print(titlelist)
            total_list = total_list + titlelist
            if value in total_list:
                return total_list
            result: str = self.find(By.CSS_SELECTOR, ".ww_pageNav_info_text").text
            num, total = result.split('/', 1)

            if int(num) == int(total):
                break
            else:
                self.find(By.CSS_SELECTOR, ".ww_commonImg_PageNavArrowRightNormal").click()

        return total_list
