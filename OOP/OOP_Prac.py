class Calculator:
    # 생성자 : 메모리에 올라오는 즉시 실행된다.
    def __init__(self, a, b):
        self.a = a
        self.b = b

    # 인스턴스 메서드
    def plus(self):
        return self.a + self.b

    def minus(self):
        return self.a - self.b

    def multiple(self):
        return self.a * self.b

    def divide(self):
        return self.a / self.b


# 아래와 같이 생성하며, 생성 시 self는 instance인 calculator1로,
# a는 1, b는 2로 할당된다.
# 또한 생성자에서 정의한 self.a 는 인스턴스 변수가 되며,
# 이때 파라미터로 받은 a를 할당하는 것이다.
calculator1 = Calculator(1, 2)
calculator2 = Calculator(3, 4)

print(calculator1.a)
print(calculator1.b)
print(calculator1.plus())
print(calculator1.multiple())

print(calculator2.a)
print(calculator2.b)
print(calculator2.plus())
print(calculator2.multiple())

# 아래와 같이 할당된 인스턴스 변수여도 재할당이 가능하다.
calculator2.a = 9
