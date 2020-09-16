import pytest
import allure
@allure.feature("这是个加法计算器，加数{0}与加数{1}相加功能")
def add_caculator(num1,num2):
    sum = num1+num2
    return sum

@allure.description("加法的计算器测试")
@allure.severity("critical")
@allure.story("正确的测试用例")
@allure.testcase("http://www.imomoe.in/","这是加法测试用例")
@allure.issue('http://www.imomoe.in/search.asp',"曾经的bug")
@pytest.mark.parametrize("num1,num2,result",[[1,2,3],[3,12,15],[6,-2,4],[1.8,2,3.8]],ids=["10以内","10以外","负数","小数"])


def test_add_caculator(num1,num2,result):
    with allure.step("第一步：调用加法方法"):
        sum = add_caculator(num1,num2)
    with allure.step("第二步：断言加法"):
        assert  sum == result


@allure.description("加法的计算器测试")
@allure.severity("normal")
@allure.story("这是无效的测试用例")
@allure.testcase("http://www.imomoe.in/""这是加法测试用例")
@pytest.mark.parametrize("num1,num2,result",[[1,'2',3],[3,'',15],[6,'*-*-',4],[1.8,'ahj',3.8]],ids=["字符串","空格","特殊字符","字母"])

def test_add_error(num1,num2,result):
    with allure.step("若果错误截图"):
        allure.attach.file("1.png",attachment_type=allure.attachment_type.PNG)
        allure.attach("加数1+加数2=","{0}+{1}={2}")
        sum = add_caculator(num1,num2)
        allure.attach("<html><body>这是我们要测试的加法<body><html>")
        assert  sum == result


