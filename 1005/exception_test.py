#exception_test.py

su1=int(input("첫번쨰 수 입력>>>"))
su2=int(input("두번째 수 입력>>>"))

try:
    result = su1 / su2 #예외가 발생할 가능성이 있는 문장
except ZeroDivisionError as e:#Exception as e===>어떤 에러 인지 모를때 사용하자 #except:
    print("0으로 나눌 수 없습니다.",e)
else:
    print("굿굿 bbbbbb")
    print("결과값>>>",result)
finally:
    print("finally는 무조건 실행")

#사용자 정의 예외 Exception
class MyException (Exception):
    def __init__(self,msg):
        self.msg=msg #MyException클래스에 msg속성 정의

    def __str__(self):
        return self.msg

def raise_test(su): #사용자 정의 함수
    if su%2==0:
        raise MyException("사용자 정의 에러 메시지>>>짝수 에러") #사용자 정의 예외를 명시적 호출
    else:
        print("su>>>",su)
try:
    raise_test(33) #예외 발생 가능성 문장
except Exception as e:
    print(e)
else:
    print("SUCCESS")
