#condition_test.py

my_id=input("아이디 입력: ") #my_id의 자료형 : String

#파이썬은 indent(들여쓰기)를 사용하여 블럭을 표현
if (my_id=="gildong123"):
    #조건식 결과가 참일때 실행할 문장은 반드시 들여쓰기를 해야함!!(한칸 이상 ㅇㅋ?)
    print("해킹 완료")

    #첫번째 라인과 같은 열을 유지해야 함
    print("로그인 성공")
print("if 조건식과 상관 없는 문장 실행")

print("=================================")

num = 1
if (num<=10 and num>=1):
    print("Great")
else:
    print("Worng")
print("if~else와 상관없는 문장")

print("=================================")

num=-13

if num > 0:
    print("num은 양수 입니다")
elif num == 0:
    print("num은 0입니다")
else:
    print("num은 음수 입니다")
