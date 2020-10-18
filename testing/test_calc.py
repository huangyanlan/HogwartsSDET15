import pytest

from pythoncode.calculator import Calculator


class TestCalc:

    def setup_class(self):
        print("开始计算")
        self.calc = Calculator()

    def teardown_class(self):
        print("结束计算")
        self.calc = Calculator()

    @pytest.mark.parametrize('a,b,expect', [
        [1, 1, 2], [-1, -2, -3], [0.1, 0.1, 0.2]
    ], ids=['int_case', 'fu_case', 'float_case'])
    def test_add(self, a, b, expect):
        # calc = Calculator()
        result = self.calc.add(a, b)
        assert result == expect
