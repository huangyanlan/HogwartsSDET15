import pytest


# 笛卡尔积参数化
@pytest.mark.parametrize('b', [4, 5, 6])
@pytest.mark.parametrize('a', [1, 2, 3])
def test_param(a, b):
    print(a, b)
