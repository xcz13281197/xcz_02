import allure
import pytest


class Test(object):
    @allure.step(title = "这是第一个测试")
    def test01(self):
        print("我是许朝卓")

        # 错误级别    BLOCKER：有防碍的
    @pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
    @allure.step(title="这是第二个测试")
    def test02(self):
        print("我是许卓")
        assert False


    def test03(self):
        with open("./image/image.png","rb") as f:
            allure.attach("失败原因",f.read(),allure.attach_type.PNG)
