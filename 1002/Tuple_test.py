mytuple=()
print(type(mytuple))

mytuple=(11,"튜플",34.5)
print(mytuple)

mytuple=("파이썬",(1,2,3),(4,5,7))
print(mytuple)
print("mytuple크기=", len(mytuple))
print(mytuple[1][0])

mytuple2=("홍","길","동","번","쩍")
#           0    1    2   3    4
#"번쩍" 출력하기

print(mytuple2[3:])
print(mytuple2[3:5])
print(mytuple2[3:len(mytuple2)])

print((11,22,33)+(44,55))
print((11,22,33),(44,55))
print((11,22,33)*3) #3번 반복
print("안녕"*3) #3번 반복

mytuple2=("홍","길","동","번","쩍")
search="동"
print("["+search,"]의 위치는 ",mytuple2.index("동")+1, "입니다")






