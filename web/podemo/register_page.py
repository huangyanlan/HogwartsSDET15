from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


class RegisterPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    # 注册信息

    def register(self):
        self.driver.find_element(By.ID, "corp_name").send_keys("lalalla")
        self.driver.find_element(By.ID, "manager_name").send_keys("haohaoha")
        self.driver.find_element(By.ID, "register_tel").send_keys("13457656009")
        self.driver.find_element(By.ID, "submit_btn").click()
        return True

    def register_fail(self):
        self.driver.find_element(By.ID, "corp_name").send_keys("lalalla")
        self.driver.find_element(By.ID, "manager_name").send_keys("haohaoha")
        self.driver.find_element(By.ID, "register_tel").send_keys("13457656009")
        self.driver.find_element(By.ID, "submit_btn").click()
        return True
