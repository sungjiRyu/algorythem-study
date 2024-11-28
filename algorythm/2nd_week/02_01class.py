class Person:
    def __init__(self, name_param):
        self.name = name_param
        print("hello", self.name)

    def talk(self):
        print("안녕하세요 저는", self.name, "입니다")


person_1 = Person("hi")
person_1.talk()

person_2 = Person("hello")
person_2.talk()
