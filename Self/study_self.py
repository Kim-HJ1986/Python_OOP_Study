# self는 인스턴스 객체이다.
# 클래스 안에 있는 self의 주소와 만들어진 인스턴스의 주소는 같다.
# 즉, self는 인스턴스 그 자체이다.


class SelfTest:

    # 클래스 변수
    name = "class_attr"

    def __init__(self, x):
        self.x = x

    # 클래스 메서드
    @classmethod
    def class_method(cls):
        print(f"cls: {cls}")
        print("class_method")

    # 인스턴스 메서드
    def instance_method(self):
        print(f"self: {self}")
        print("class안의 self 주소: ", id(self))
        print("instance_method")


test_obj = SelfTest(11)

test_obj.instance_method()
test_obj.class_method()
print("인스턴스의 주소: ", id(test_obj))

"""
self: <__main__.SelfTest object at 0x000001A726CA9D60>
class안의 self 주소:  1817421978976
instance_method
cls: <class '__main__.SelfTest'>
class_method
인스턴스의 주소:  1817421978976

self와 instance의 주소가 같다!
인스턴스도 클래스 메서드를 사용할 수 있다. 즉, 인스턴스를 통해 해당 클래스 메서드를 사용할 수 있다.
단, 클래스는 인스턴스 메서드를 사용할 수 없다.
"""
