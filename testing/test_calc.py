import pytest
import yaml

from pythoncode.calculator import Calculator


# 解析测试数据
def get_datas():
    with open("./datas/calc.yml", encoding='utf-8') as f:
        datas = yaml.safe_load(f)
    add_datas = datas['add']['datas']
    add_ids = datas['add']['ids']
    print(add_datas)
    print(add_ids)
    return [add_datas, add_ids]


# 解析测试步骤
def steps(addstepsfile, calc, a, b, expect):
    with open(addstepsfile) as f:
        steps = yaml.safe_load(f)

        for step in steps:
            if 'add' == step:
                result = calc.add(a, b)
            elif 'add1' == step:
                result = calc.add1(a, b)
        assert result == expect


class TestCalc:

    def setup_class(self):
        print("开始计算")
        self.calc = Calculator()

    def teardown_class(self):
        print("结束计算")
        self.calc = Calculator()

    @pytest.mark.parametrize('a,b,expect', get_datas()[0], ids=get_datas()[1])
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

    # @pytest.mark.parametrize('a,b', [
    #     [0.1, 0.2], [0.2, 0.3]
    # ])
    def test_add_steps(self):
        # assert 2==self.calc.add(1,1)
        # assert 3 == self.calc.add1(1, 2)
        # assert 0 == self.calc.add(-1, 1)
        a = 1
        b = 1
        expect = 2
        steps("./steps/add_steps.yml", self.calc, a, b, expect)
