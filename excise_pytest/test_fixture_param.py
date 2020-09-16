import pytest

test_user_data = [{'name':'linda','password':'root1234'},
                  {'name':'gaoyongqaing','password':'root1244'},
                  {'name':'duxincheng','password':'root2123'}]

@pytest.fixture(scope="module")
def login(request):
    username = request.param['name']
    password = request.param['password']
    print(f"\n打开首页准备登陆，登陆用户：{username},密码是{password}")
    return  request.param

@pytest.mark.parametrize("login", test_user_data, indirect=True,ids=["老师","agl","dshqld"])
def test_login(login):
    name=login['name']
    print(f"本次登陆的:{name}")
    assert name !=""