#io_test.py

print(192,168,0,85);
print(192,168,0,85,sep=".");
print("new line하지 않겠어",end="\t")
print("hello")

#콘솔 출력 대신 txt 파일에 출력!!!
print("hello","hi","good","추가된 문자열",file=open("a.txt",'w'))

#su=input()
#print("su:",su)

a = input("a값 입력: ")
b = input("b값 입력: ")
print("입력 받은 a의 자료형:",type(a))
print("a와 b를 더한 합(문자열)=",a+b)

print("a와 b를 더한 합(숫자 변환)=",int(a)+int(b))

    #print() #들여쓰기 에러
