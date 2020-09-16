import pytest
import sys


def setup_module():
    print("这是一个文件在开始时执行一次")
def teardown_module():
    print("这是一个文件在结束时执行一次，不是按照现在所有位置顺序执行的")

def setup_function():
    print("这个方法里的在不在类的每个方法函前执行一次")

def test_function_01():
    print("不在类中的函数方法")

def test_function_02():
    print("不在类中的函数方法2")

def teardown_function():
    print("这个方法里的在不在类的每个方法函数后执行一次")

class TestClass():
    def setup_class(self):
        print("在类的开始时执行一次")

    def teardown_class(self):
        print("在类结束时执行一次")

    def set_up_method(self):
        print("在有类的每个地方前执行一次，有几个方法执行几次")

    def teardown_method(self):
        print("在有类的每个地方后执行一次，有几个方法执行几次")

    def test_method_01(self):
        print("这是类中的方法01")
        assert 3 == 2+1
        assert (3>2) ==True
        assert 'linda'in'lindafang'

    def test_method_02(self):
        print("这是类中方法02")
        assert {'name': 'linda' , 'age': 18} == {'name': 'linda' , 'age': 38}
    environment = 'android'
    @pytest.mark.skipif( environment=="android",reason='android平台没有这个功能')
    def test_cart_3(self):
        print ( ' 这是mac-apple的还环境所以不能执行' )
    @pytest.mark.skipif(sys.platform == 'win32',reason='不在windows下运行')
    @pytest.mark.skipif(sys.version_info <(3,6),reason='3.6版本以下不执行')
    def test_cart(login):
        print ( 'case3,登陆，点击苹果图标，3.6以下版本无法执行')
    @pytest.mark.skipif(reason="我不想执行了")
    def test_method_03(self):
        print("这是类中方法03")
        assert '*' * 10 == '*' * 5


if __name__ == '__main__':
           pytest.main()