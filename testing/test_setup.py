def setup_module():
    print("资源准备：setup module")


def teardown_module():
    print("资源销毁：teardown module")


def test_case1():
    print("case")


def setup_function():
    print("资源准备：setup function")


def teardown_function():
    print("资源销毁：teardown function")


class TestDemo:
    def setup_class(self):
        print("资源准备：setup_class")

    def teardown_class(self):
        print("资源销毁：teardown_class")

    def setup(self):
        print("资源准备：setup")

    def teardown(self):
        print("资源销毁：teardown")

    def test_demo1(self):
        print("test demo1")

    def test_demo2(self):
        print("test demo2")
