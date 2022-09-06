# abstraction : 추상화
# 불필요한 정보는 숨기고, 중요한(필요한) 정보만을 표현함으로써
# 공통의 속성 값이나 행위(methods)를 하나로 묶어 이름을 붙이는 것이다.


class Robot:

    # 클래스 변수 : 인스턴스들이 공유하는 변수
    population = 0

    # 생성자 함수 : 인스턴스가 생성될 때 초기화가 되는 함수
    def __init__(self, name, code):
        self.name = name  # 인스턴스 변수
        self.code = code  # 인스턴스 변수

        # 모든 인스턴스들이 공유하는 클래스 변수의 값을, 생성될 때 마다 + 1 씩 해준다.
        Robot.population += 1

    # 인스턴스 메서드
    def say_hi(self):
        # code..
        print(f"Greetings, my masters call me {self.name}.")

    # 인스턴스 메서드
    def calc_add(self, a, b):
        return a + b

    # 인스턴스 메서드
    def die(self):
        print(f"{self.name} is being destroyed!")

        # 죽었을 경우 클래스 변수인 population 1 감소
        Robot.population -= 1

        if Robot.population == 0:
            print(f"{self.name} was the last one.")
        else:
            print(f"There are still {Robot.population} robots working.")

    # 인스턴스 메서드
    def fixed(self):
        print(f"{self.name} is fixed now!")

        # 고쳤을 경우 클래스 변수인 population 1 증가
        Robot.population += 1
        print(f"There are {Robot.population} robots working now.")

    # 클래스 메서드
    @classmethod
    def how_many(cls):  # cls는 인스턴스인 self 대신 클래스를 받는 것 (class를 의미).
        print(f"We have {cls.population} robots.")


print(Robot.population)  # 0

siri = Robot("siri", 120392491)
jarvis = Robot("jarvis", 1232349729)
bixby = Robot("bixby", 3452234134435)

print(Robot.population)  # 3

print(siri.name)
print(siri.code)
siri.calc_add(2, 3)
siri.die()

Robot.how_many()

siri.fixed()
Robot.how_many()
