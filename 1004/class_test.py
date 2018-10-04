# class_test.py

# -OOP(Object Oriented Programming) 이란 객체 지향프로그램을 말하며 데이터 처리를 하
# 는 메서드들을 하나의 프로그램으로 설계해서 연동하는 객체(Object)를 중심으로 프로그램을
# 짜는 언어를 말한다.
# -Python은대화적이고(interactive), 읶터프리팅(interpreted)되는 객체 지향(objectoriented)
# 프로그래밍 언어이다.
# - 파이썬은 자바, 닷넷 등의 객체지향 언어와는 다르게 클래스를 포함해서 사용하는 모든 것
# 을 객체로 다룬다.

# 객체와 클래스는 다음과 같이 분류 될수 있다
# 객체 = 속성(Attributes) + 행위(Behaviors)
# 클래스 = 변수(Variable) + 메소드(Methods)



class Test:
    def empty(self): #self : 현재 클래스 객체 레퍼런스
        print("empty() Method>>>", self)
        self.data=[]

    def add(self,x):
        print("add() Method>>>",self)
        self.data.append(x)

print("클래스 객체 테스트")

#객체생성
my01=Test() #새로운 객체 생성(메모리 할당)
my02=my01 #my01의 주소를 복사해서 my02 할당(my01과 my02는 같은 메모리 주소를 갖음)
my03=Test() #새로운 객체생성

my01.empty()
my02.empty()
my03.empty()

my01.add(11)
my01.add(22)
my01.add(33)

print("my01의 데이터",my01.data)
print("my02의 데이터",my02.data) #my02는 my01과 같은 메모리를 참조하기 때문에 결과값도 동일
print("my03의 데이터",my03.data)

class Address:
    name="길동홍"
    addr="남터"
    tel="010-1234-5678"

Address.addr="고속터미널" #남터에서 고터로 변경됨

print("이름>>>", Address.name, ",주소>>>", Address.addr, ",전화번호>>>", Address.tel)

#private 멤버 TEST
class Test2():
    a=100
    __b=200 #더블 언더바 ===> private : 현재 클래스의 멤버끼리만 사용가능

    def __m(self):
        return "안녕"

    def k(self):
        print("__b의 값 출력>>>",self.__b,", __m()호출>>>",self.__m())
t2 = Test2() #객체 생성
print("Test2클래스 a속성값>>>",t2.a)
#print("Test2클래스 b속성값>>>",t2.b) #AttributeError: 'Test2' object has no attribute 'b'
#print("Test2클래스 b속성값>>>",t2.__b) #AttributeError: 'Test2' object has no attribute '__b'
#t2.__m() #AttributeError: 'Test2' object has no attribute '__m'

t2.k()