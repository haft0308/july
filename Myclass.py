class Person:
    # 생성자.
    def __init__(self, name, age, addr):#생성자는 1개만 정의해야함.직접적으로 함수오버로딩을 지원하지 않음.
        self.name = name
        self.age = age
        self.addr = addr

    def content_show(self):
        print("{}{}{}".format(self.name, self.age, self.addr))
        print(f"{self.name} {self.age} {self.addr}")



user = Person("고길동", 20, '노원구')
user.content_show()

class Animal:
    def __init__(self):
        print("Animal의 생성자__init__")
    def info(self):
        print("info()메소드")

animal = Animal()
animal.info()
print(animal.__dict__)

class Dog(Animal):#Animal을 상속받은 Dog
    name = '삼식'
    age = 3
    breed="골든 리트리버"

    def __init__(self):
        print("Dog클래스의 생성자__init__")
    def bark(self):
        print(self.name + '가 멍멍하고 짖는다')

    def info(self):#오버라이드된 메소드.
        print("info() Dog클래스의")
        super().info()#부모가 가지고 있는 info()를 자손클래스에서 호출함.

dog = Dog()
dog.bark()
dog.info()


class Cat(Animal):
    def __init__(self, name, age, breed, secret):#__는 특별하게 취급하는 메소드, 매직메소드 라고함.
        self.name = name
        self.age = age
        self.breed = breed
        self.__secret = secret #비공개 멤버변수
        print("cat의 __init__")

    def grooming(self, name):
        print(name+'가 그루밍하고 있다')

    def set_name(self, name):
        self.name = name
    def get_name(self):
        return self.name
    def get_secret(self):
        return self.__secret

    def set_secret(self, secret):
        self.__secret= secret
    def __str__(self):  #toString()과 같은 동작을 함. 객체의 값을 모두 확인하고 싶을때 사용함.
        return self.name + str(self.age) + self.breed#, str(self.__secret)
cat = Cat('고동이', 2, '코숏', 2024)
cat.secret = 2025
cat.set_secret(2025)
print()
cat.grooming('고동삼')
print(cat)

print(cat.__dict__)#객체가 가지고 있는 인스턴스 변수들을 저장한느 딕셔너리.
                    #객체 내부에 어떤 속성들이 있고 그 값이 무엇인지 알려줌..
                    # (객체 내부에 있음, 객체 생성될때 자동으로 메모리 공간에 할당함.
                    # 객체마다 자동생성, 별도로 뭐 할 것없이 바로 접근가능.
print(dog.__dict__)
print(animal.__dict__)

class ParkJungJa:
    def __init__(self):
        self.str = "박정자 생성자"
        print(self.str)

class KoKilDong:
    def __init__(self):
        self.str = "고길동 생성자"
        print(self.str)


class KoChulSoo(ParkJungJa, KoKilDong):#다중상속가능.
    def __init__(self):

        ParkJungJa.__init__(self)

        KoKilDong.__init__(self)
        print(self.str)
        print("고철수 생성자")
        super().__init__()


kcs = KoChulSoo()
print(kcs.str)
print(kcs.__dict__)