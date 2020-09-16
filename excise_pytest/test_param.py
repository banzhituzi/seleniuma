import pytest
#通过fixture自带的参数进行数据驱动，形参名字必须是request
@pytest.fixture(params=[1,2,3,'dqdq'])
def data_param(request):
    return request.param

#测试方法需要一些数据通过装饰器的方式加载数据
def test_fixture_param(data_param):
    print(data_param)

# @pytest.mark.usefixtures("data_param")
# def test_fixture_param1():
#     print(data_param)