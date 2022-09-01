def copyright(func):
    def new_func():
        print("@Copyright")
        func()
        return "end!"

    return new_func


# 함수 바로 위에 어노테이션과 함수 이름을 넣기만 해도 재정의가 된다!!
# 함수의 내부를 수정하지 않고 기능에 변화를 주고 싶을 때 사용한다.
# 일반적으로 함수의 전처리나 후처리에 대한 필요가 있을때 사용을 한다.
# 또한 데코레이터를 이용해, 반복을 줄이고 메소드나 함수의 책임을 확장한다.
# 기능을 추가할 함수를 인자로 넘긴다.
# 이를 decorator라고 한다.
@copyright
def smile():
    print("😊")


@copyright
def sunglass():
    print("😎")


@copyright
def angry():
    print("🤬")


@copyright
def doggy():
    print("🐶")


@copyright
def madness():
    print("👹")


@copyright
def scary():
    print("😫")


@copyright
def hmm():
    print("🤔")


@copyright
def surprise():
    print("😨")


smile()
sunglass()
angry()
doggy()
madness()
scary()
hmm()
surprise()
