#inheritance_test.py

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def personInfo(self):
        return self.name+" : (나이:"+ str(self.age) +")" #ex: "홍길동 : (나이:13)"

    def xx(self):
        print('xx()함수!!')

# '나'+'너' ---> '나너'
# 11+33     ---> 44
# '11'+33 --->  에러     해결) int('11') + 33
# '우리'+ 55 ---> 에러   해결) '우리' + str(55)

class Student(Person):
    def __init__(self,name,age,grade):
        Person.__init__(self,name,age)
        self.grade = grade

    def studentInfo(self):
        return self.personInfo()+",등급:"+ str(self.grade)

    def yy(self):
        print('yy()함수!!')

print('상속테스트!!')
p = Person('홍길동',13)
print("Person정보>>>"+ p.personInfo())
p.xx()
#p.yy() #에러: 부모레퍼런스 통해 자식호출X

print('---------------------------------')
s = Student('길라임',15,2)
print("Student정보>>>"+ s.studentInfo())
s.yy()
s.xx()

class Dog:
 def sound(self):
  print ("멍멍~~" )

class Cat:
 def sound(self):
  print ("야옹야옹~~")

class Chimera (Cat,Dog):#(Dog, Cat):
 pass

Chimera().sound()

print("===========================================================================================")
#추상클래스 정의
from abc import abstractmethod, ABCMeta
class Base(metaclass=ABCMeta):

    @abstractmethod
    def start(self):
        print("Base 시작")

    def stop(self):
        print("Base 정지")

class Duck(Base):
    def hello(self):
        print("오리 안녕")

    def start(self):
        print("오리 냠냠")

d = Duck()
d.hello()
d.start()
d.stop()