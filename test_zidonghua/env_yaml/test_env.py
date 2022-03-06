import pytest
import yaml

class Test_Demo():
    @pytest.mark.parametrize('env',yaml.safe_load(open('./env.yml')))
    def test_demo(self,env):
        #print(env)
        if 'test'in env:
            print('这是测试环境','ip地址是',env['test'])
        if 'dev'in env:
            print('这是开发环境','ip地址是',env['dev'])


if __name__ == '__main__':
    pytest.main(['-s'])