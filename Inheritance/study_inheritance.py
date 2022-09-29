"""
클래스 상속

1. 부모 클래스가 갖는 모든 메서드와 속성이 자식 클래스에 그대로 상속된다.

2. 자식 클래스에서 별도의 메서드나 속성을 추가할 수 있다.

3. 메서드 오버라이딩

4. super()

5. Python의 모든 클래스는 object 클래스를 상속한다. -> 모든 것은 객체이다.

* MyClass.mro() -> 상속 관계를 보여준다.
"""


class Robot:
    def __init__(self, name: str) -> None:
        self.name = name

    def say_hello(self):
        print(f"hello, my name is {self.name}")


class Siri(Robot):
    def __init__(self, name: str, age: int) -> None:
        super().__init__(name)
        self.age = age

    def say_hello(self):
        super().say_hello()
        print("this is Method Overriding")


siri = Siri("siri", 28)
siri.say_hello()
print(siri.age)
