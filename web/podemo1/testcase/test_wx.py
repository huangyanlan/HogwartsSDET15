import pytest
import yaml

from web.podemo1.page.main_page import MainPage


def get_datas():
    with open("./datas/calc.yml", encoding='utf-8') as f:
        datas = yaml.safe_load(f)
    add_datas = datas['add']['datas']
    add_ids = datas['add']['ids']
    print(add_datas)
    # print(add_ids)
    return add_datas


class TestWx:

    def setup(self):
        self.main = MainPage()

    @pytest.mark.parametrize('username,acount,phone', get_datas())
    def test_addmenber(self, username, acount, phone):
        # username="aaaaa12"
        # acount = "aaaa_hyl521"
        # phone = "12450090905"

        addmember = self.main.goto_addmember()

        addmember.add_member(username, acount, phone)
        username: str = username
        listtile = addmember.get_member(username)

        assert username in listtile
