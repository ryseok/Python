# function_test.py

def Hello():
    print("hello")


def Hello2(name):
    "함수에 대한 주석 : 전달받은 이름 안녕을 출력"
    return "안녕," + name + "~!!"


print("=======================")
print("function TEST")
Hello()
# Hello2() 에러 : 전달데이터 필요
data = Hello2("길동")
print(data)
print("Hello() return값 확인>>>", Hello())
print("=======================")


def hello3():
    return "아이폰", "iphoneXS"


s1, s2 = hello3()
print(s1, s2)
print("=======================")


def add_sub(x, y):
    return x + y, x - y


a, b = add_sub(10, 5)
print("더하기>>>%s" % a)
print("빼기>>>", b)
print("=======================")

def repeat_msg(msg):
    print(msg)


def repeat_msg2(msg, rep=3):
    print("반복횟수>>>", rep)
    for i in range(rep):
        print(msg)

repeat_msg("안녕,목요일")

#rep=반복횟수 : 내 마음대로 변경 가능하다 <=== def repeat_msg2(msg, rep=3): 정의 되어 있지만
repeat_msg2("내일 불금???",rep=10)
print("=======================")
def varargs(*su):#(su1,su2):
    print("가변인자",su)
varargs()
varargs(1,2)
varargs(11,22,33)

# def varargs2(*su,su2): ===> 에러 발생 : 가변인자는 반드시 맨 마지막에 한번 정의!!!
def varargs2(su2,*su):
    print("su>>>",su)
    print("su2>>>",su2)
varargs2(90,100,101,102)


# 파라미터에 ( **변수) 인자
# 변수는 딕셔너리 형태로 키워드 읶자들 중에서 일반 인자가 아닌 것들을 넘겨 받는다.
# 만약 가변 개수 인자 (*변수)와 혼용하는 경우에는 반드시 가변 변수 뒤에 와야 한다.
def varargs3(su, *su2, **su3): #일반인자, 가변인자, 딕셔너리인자의 순서를 반드시 가져야 함
    print("su의값>>>",su)
    print("su2의값>>>",su2)
    print("su3의값>>>",su3)
varargs3(100,200,300,400,id="gildong",pwd="123")