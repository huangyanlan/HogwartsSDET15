import pytest


#
# @pytest.fixture(autouse=True,scope="function")
# def login():
#     print("登录操作")
#     yield['tom','12345']
#     print("登出操作")
#
# @pytest.fixture(autouse=True,scope="function")
# def z():
#     print("完成数据库连接")

# @pytest.mark.usefixtures("login")
def test_case1(login):
    print(login)
    print("用例1")


def test_case2():
    print("用例2")


def test_case3(conn_db):
    print(conn_db)
    print("用例3")
