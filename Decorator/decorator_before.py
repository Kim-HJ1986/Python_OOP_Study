def copyright(func):
    def new_func():
        print("@Copyright")
        func()
        return "end!"

    return new_func


def smile():
    print("😊")


def sunglass():
    print("😎")


def angry():
    print("🤬")


def doggy():
    print("🐶")


def madness():
    print("👹")


def scary():
    print("😫")


def hmm():
    print("🤔")


def surprise():
    print("😨")


# 새로운 함수로 재정의 해준다. 이 때, 각 object는 새로운 함수로 재정의 된다.
# 예를 들어, smile의 경우 copyright()로 재정의 된다.
# 이때 smile은 재정의된 함수이며,
# 소괄호 ()를 붙일 경우 실행하라는 뜻이 되어,
# smile()의 return 값인 None이 인자로 넘어가 not callable 오류가 발생한다.
smile = copyright(smile)
sunglass = copyright(sunglass)
angry = copyright(angry)
doggy = copyright(doggy)
madness = copyright(madness)
scary = copyright(scary)
hmm = copyright(hmm)
surprise = copyright(surprise)

# smile()
# sunglass()
# angry()
# doggy()
# madness()
# scary()
# hmm()
# surprise()

print(smile)
# 함수 자체를 print하면 smile이 먼저 실행되고 -> copyright(smile)
# 해당 함수의 return 값을 print한다. 여기에선 copyright의 return 값이 없으므로 None 이 찍힌다.
# 현재는 return 값을 end! 로 지정하여, end! 가 찍힌다.
print(smile())
