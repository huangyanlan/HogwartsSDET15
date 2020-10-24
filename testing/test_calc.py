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
        [1, 1, 2], [-1, -2, -3]
    ], ids=['int_case', 'fu_case'])
    def test_add(self, a, b, expect):
        # calc = Calculator()
        result = self.calc.add(a, b)
        assert result == expect

    @pytest.mark.parametrize('a,b,expect', [
        [0.1, 0.2, 0.3], [0.2, 0.3, 0.5]
    ])
    def test_float(self, a, b, expect):
        result = self.calc.add(a, b)
        assert round(result, 2) == expect

    @pytest.mark.parametrize('a,b,expect', [
        [0.1, 0, True], [0.2, 0, True]
    ])
    def test_div(self, a, b, expect):
        with pytest.raises(ZeroDivisionError):
            result = self.calc.div(a, b)
        # try:
        #    result=self.calc.div(1,0)
        # except ZeroDivisionError:
        #    print("除数为0")
