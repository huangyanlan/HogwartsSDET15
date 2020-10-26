from typing import List

import pytest

from pythoncode.calculator import Calculator


@pytest.fixture(scope="function", params=['tom', 'jerry'])
def login(request):
    print("登录操作")
    username = request.param
    yield username
    print("登出操作")


@pytest.fixture(autouse=True, scope='session')
def conn_db():
    print("完成数据库连接")
    yield "database"
    print("关闭数据库连接")


@pytest.fixture(scope="class")
def get_calc():
    print("计算开始")
    calc = Calculator()
    yield calc
    print("计算结束")


def pytest_collection_modifyitems(session: "Session", config: "Config", items: List["Item"]) -> None:
    print(type(items))
    items.reverse()

    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')

    if 'add' in item.nodeid:
        item.add_marker(pytest.mark.add)
    elif 'div' in item.nodeid:
        item.add_marker.marker(pytest.mark.div)
