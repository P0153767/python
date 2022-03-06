import pytest


#class Test_Demo():
#@pytest.mark.parametrize('a,b',((2,3),(3,3))) #后面的值格式的组合可以很随意，最外面是元祖还是列表，
# 里面是元祖还是列表还是字典都没有关心，只要与前面的参数数量对应就行
@pytest.mark.parametrize('a,b',(({1:2},{3:4}),({5:6},{7:8})))
def test_demo(a,b):
    print(a,b)
    #print('1')




if __name__ == '__main__':
    pytest.main(['-s'])  #'-s'参数的作用是输出print的内容，不加就输出不了




