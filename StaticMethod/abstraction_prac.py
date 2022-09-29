# static method : 유틸리티성 정적 메서드.


class Robot:

    # 클래스 변수 : 인스턴스들이 공유하는 변수
    population = 0

    # 생성자 함수 : 인스턴스가 생성될 때 초기화가 되는 함수
    def __init__(self, name, code):
        self.name = name  # 인스턴스 변수
        self.code = code  # 인스턴스 변수
        Robot.population += 1

    # ... 생략

    @staticmethod
    def is_this_Robot():
        return "Yes!, this is Robot!!"


siri = Robot("siri", 123123132)
print(siri.is_this_Robot())
print(Robot.is_this_Robot())
