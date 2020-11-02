from selenium.webdriver.common.by import By

from pythoncode.setupbroser import Base


class TestFram(Base):
    def test_fram(self):
        self.driver.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
        # 切换到fram
        self.driver.switch_to.frame('iframeResult')
        # 切换到fram，也可以这么写，但用的少
        # self.driver.switch_to_frame('iframeResult')
        print(self.driver.find_element(By.ID, 'draggable').text)
        # 切换回fram的父节点
        self.driver.switch_to.parent_frame()
        # 切换回默认的节点
        # self.driver.switch_to.default_content()
        print(self.driver.find_element(By.ID, 'submitBTN').text)
