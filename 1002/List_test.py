#List_test.py

list1=[1,2,3]
print(type(list1),"리스트 내용=",list1)

list2=[1,2,3]
list3=[4,5,6]
print("list3 최대값:",max(list3))
print("list3 최소값:",min(list3))
print("list3 요소갯수:",len(list3))

#list데이터 조작(변경)
list3.append(77)
list3.append(88)
list3.append([99])


#list.extend(99):에러발생===>열거데이터를 추가해야함
list3.extend([101,102,101])
list3.insert(2,13);
list3.pop() #마지막 요소 삭제
list3.pop(6) #명시된 인덱스의 요소 삭제
list3.remove(88) #명시된 데이터를 삭제

print("====================")
print("list3 '101'의 갯수",list3.count(101))
print("list3요소 출력:",list3)

list3.reverse()
print("list3 리버스 후 요소출력",list3)

list3.sort()
print("list3 정렬:",list3)

list4=[11,22,11]
list4.remove(11);
print("list4에서 '11' 삭제후 결과",list4)

tuple1=(11,22,33)
print("tuple1 데이터:",tuple1)
print("tuple1[0]",tuple1[0])
#tuple1[0]=44 변경불가

list5=[11,22,33]
print("list5데이터:",list5)
print("list5[0]:",list5[0])
list5[0]=44
print("변경후 list5데이터:",list5)