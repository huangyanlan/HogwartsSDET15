import pytest


@pytest.fixture()
def conn_db():
    print("完成数据库连接aaaaaa")
    yield "database"
    print("关闭数据库连接aaaaa")
