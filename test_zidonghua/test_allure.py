import allure
import pytest

@allure.feature('给模块加备注')
class Test_Demo():
    @allure.story('给用例加备注')
    def test_demo1(self):
        with allure.step('给用例里面的步骤加备注'):
            print('哈哈哈')

if __name__ == '__main__':
    pytest.main(['-s'])