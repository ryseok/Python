#test.py

# 메소드에 지정하는 self 의 의미
# - 파이썬에서 매개인자 중 메소드를 정의핛 때 첫 번째 매개인자를 반드시 명시
# 하게 되는데 self인수라고 부른다.
# - Self 인수의 의미는 객체자식의 참조이다.
# - 모든 메소드는 최소한 self 인수는 가져야 핚다.
# - 객체를 통해서 불려지는 메소드의 첫 번째 읶수는 자동적으로 객체의 참조로
# 채워진다. 따라서 self 인수를 넘겨 줄 필요는 없다.
# - Self를 통해서 클래스 내의 멤버나 메소드를 자유롭게 호출할 수 있다.


class Address:
   name='홍길동'
   addr='남부터미널'

a1 = Address()
a2 = a1
a3 = Address()


print('Address.name1=', Address.name)

a1.name='길라임'
Address.name='김주원'
print('Address.name2=', Address.name)

print('a1.name=',a1.name)
print('a2.name=',a2.name)
print('a3.name=',a3.name)

# __class__ 키워드
# - 인스턴스객체가 자싞을 생성할 클래스 객체를 참조하기 위하여 파이 에서는 인스턴스 객체의 내장속성 '__class__‘를 제공할
# 다. 더블 언더스코어를 class라는 키워드의 앞뒤에 붙여서 사용되며 클래스 영역에 모든 읶스턴스 객체에 데이터를 참조하거나
# 수정할 때 사용된다.\

class Num:
  def __init__(self,num):
      print('생성자')
      self.no = num
  def __add__(self, num):
      print('__add__')
      self.no += num
  def __sub__(self, num):
      print('__sub__')
      self.no -= num

n = Num(100)
print('no=',n.no) #100
n+200
print('no=',n.no) #100+200 ---> 300
n-600
print('no=',n.no) #300-600 ---> -300