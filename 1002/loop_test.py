#loop_test.py

#while True: ===> 무한 루프
#    print("안녕")

#1부터 10까지 더하기
i=1
sum=0
while i<=10:
    print(i)
    sum+=i
    i+=1
print("sum의 값: ",sum)

print("==========================")
fruit=["사과","딸기","바나나","수박"] #리스트 데이터
for fvalue in fruit: #for (리스트내 각각의 값을 받을)변수명 in [리스트]
    print(fvalue)

num=[1,2,3]
sum=0

for v in num:
    sum+=v
print("1+2+3= ", sum)

m_dict={"x":11, "y":22, "z":33} #딕셔너리 데이터
for key in m_dict:
    print(key, "=", m_dict[key])

t = [(11,22), (33,44), (55,66)] #리스트내에 튜플데이터
for (aa,bb) in t:
     print(aa, bb)