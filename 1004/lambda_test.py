#lambda_test.py

# - 람다 대수학(lambda calculus)에서 유래된 이름으로 익명함수라고 지칭
# - 함수의 이름이 없는 함수로 파이썬 에서는 lambda 라는 키워드로 익명 함수를 정의
# - 간단한 기능의 함수가 컨테이너의 요소로 들어가는 경우 혹은 다른 함수의 인자로
# 함수를 넘겨줄 필요가 있을 때 사용되며 한 줄로 표시되는 함수로 정의
# - 람다 함수는 filter(), map() ,reduce() 등의 함수와 함께 유용하게 사용된다.
#lambda 인자1, 인자2,인자3 : 표현식

add=lambda x,y:x+y
print("람다함수 TEST")
print("add람다 결과값>>>",add(5,3))
print((lambda x,y,z:x*y*z)(2,3,4))
print("===================================")
def even(x): #사용자 정의 함수 even
    return (x%2 ==0) #전달되는 데이터가 짝수일때 True 리턴

myList=range(10)
print(list(filter(even,myList))) #filter고차함수는 True값만(결과값 전달받는) 취하는 함수

print(list(filter(lambda x:x%2==0,myList)))
print(list(filter(lambda x:x%2==0,range(10))))

print(list(map(lambda a:a*2,[11,22,33,44])))

from functools import reduce
print("0~10합>>>",reduce(lambda x,y:x+y, range(11)))
print("0~100합>>>",reduce(lambda x,y:x+y, range(101)))

def sum_n(n):
    if n==0:
        return 0
    else:
        return n+sum_n(n-1)
print("5부터 0까지의 합>>>",sum_n(5))

# 5*4*3*2*1의 값을 구하시오
def num_n(n2):
    if n2==1:
        return 1
    else:
        return n2*num_n(n2-1)
print("5부터 1까지 곱>>>",num_n(5))