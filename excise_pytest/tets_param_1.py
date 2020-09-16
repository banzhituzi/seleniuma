import pytest
# @pytest.mark.parametrize("num1,num2,result",[[1,2,3],
#                                          [3,1,15],
#                                         [6,2,13],
#                                          [3,1,3]])
# def test_coculator(num1,num2,result):
#     assert num1+num2 == result

@pytest.mark.parametrize("num1,num2,result",[[1,2,3],[3,12,15],[6,-2,4],[1.8,2,3.8]],ids=["10以内","10以外","负数","小数"])
def test_coculator2(num1,num2,result):
    assert num1+num2 == result
