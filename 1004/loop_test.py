# loop_test.py
from builtins import enumerate

v1=(1,2,3,4)
v2=["컴","퓨","터","구","입","ㄱ"]
v3="홍길동"

print("v1 자료형",type(v1),", v2자료형",type(v2),", v3자료형",type(v3))
print("=============")
for i in v1:
    print(i)
print("=============")
for i in v2:
    print(i)
print("=============")
for i in v3:
    print(i)
print("=============")

# range() TEST
# -range(start, stop, step size) 함수는 숫자 범위에 대하여 반복을 하거나 특정
# 한 범위의 숫자를 나열하도록 해주는 특별한 함수
# - range 함수를 사용하는 형식은 선택사항인 시작 값(start), 종료 값(stop), 그리고
# 선택사항인 증감 분(step size)이다.
# Ex) range(0,20,4) -------- 0,4,8,12,16
# 0에서 시 작하여 4의 갂격으로 20에 이르기 전까지의 정수

# range() 함수는 list와 함께 선언할 수 있다.

# print(range()) 에러 : 전달인지 필요
print(range(10))
print(range(3,10))
print(range(3,10,2))
print(type(range(10)))

for i in range(5): # i=0~4
    print(i)
print("=============")
for i in range(1,5): # i=1~4
    print(i,end="")
print()
print("=============")
for i in range(1,10,2): # i=1~10 (2step)
    print(i,end="")
print()
print("=============")
print()

# 반복문과 함께 사용하는 함수 _ enumerate()함수
# - enumerate()함수는 인덱스 값과 그 value 값을 동시에 저장 할 수 있는
# 특징을 가진 for문을 좀더 효율적으로 사용하기 위한 파이썬 함수이다.
# - enumerate([시퀀스 타입 객체], [시작 값=0])의 형식을 가지며 시퀸스타입
# 객체는 이터레이션이 가능한 객체가 입력되고 시작 값은 입력 시 해당 수부터
# 증가하며, 입력하지 않았을 때 기본값으로 0을 지정하게 된다

fruit=["사과","딸기","복숭아","포토"]
for t in enumerate(fruit):
    print(t)
print("=============")
print()

# zip() : 목록을 묶어서 리턴
# 반복문과 함께 사용하는 함수 _ zip()함수 : 매개 인자로 여러 목록을 받아
# 각 목록의 요소를 튜플에 담아 목록에 저장하고 반환

for x,y in zip([1,2,3],[4,5,6]):
    print(x+y,end=" ")
print()
print("=============")
# 목록을 묶어서 set으로 리턴
print(set(zip(['a','b','c'],[1,2,3])))

# 목록을 묶어서 dict으로 리턴
keys=["cat","dog","duck"]
values=["야옹","멍멍","꽥꽥"]
print(dict(zip(keys,values)))
print()

#items(): 목록을 key,value로 리턴
# 반복문과 함께 사용하는 함수 _ items()함수 : dict 의 내장함수로 키와 값을 동시에 검색

dic = {'one':1, 'two':2, 'three':3}
for key,value in dic.items():
    print(key,value)
print("=============")

# 흐름 제어 문이란 ?
# -프로그램의 흐름을 순차적으로 수행하다가 다른 곳으로 조건에 의해 또는
# 어떤 이유에서 흐름을 이동하는 구문을 말한다.
# -조건 문이나 반복 문 또는 프로그램의 명령을 수행하는 중에 Block를 빠져
# 나가거나 특정 위치로 이동할 필요가 있을 때 사용하는 문장으로 break, continue등이 있다

for i in range(1,10):
    if i>5: break
    print("%5d"%i,end=" ") #오른쪽 정렬
    #print("%-5d"%i,end=" ") #왼쪽 정렬
print()
print("=============")
# 중첩 for루프와 if
# - 파이썬의 구문은 구문 안에 또 다른 파이썬 구문을 이너(inner)형식으로 선언할 수
# 있으며 중첩 구조 형태를 가진다.
# - 중첩 if문은 if조건 식의 명령구문에 또 다른 if구문을 선언하는 것을 말하며 for문이 또
# 다른 for문을 가진 다면 다중 for라고 말한다.
# - 그 외에도 다중 while구문을 사용할 수 있으며 여러 가지 형태의 구문들을 이너(inner)
# 형태로 두기도 한다. 예를 들면 for 안에 while, if등을 선언할 수 있다
# - 다중 혹은 중첩구문의 조건 문에 따라 흐름 제어를 할 수 있어 구문에 따라 continue,
# break를 적절하게 사용한다

#2단 부터 5단까지 출력
for dan in range(2,6): #2~5
    for i in range(1,10): #1~9
        print("%d*%d="%(dan,i),dan*i) # %d : C언어와 같다

# 코드	    설명
# %s	    문자열 (String)
# %c	    문자 1개(character)
# %d	    정수 (Integer)
# %f	    부동소수 (floating-point)
# %o	    8진수
# %x	    16진수
# %%	    Literal % (문자 % 자체)
print()
print("=============")
