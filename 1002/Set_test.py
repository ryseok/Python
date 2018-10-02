#Set_test.py

str1="abcabcabc"
str2="abcdefgij"
print("str1의 자료형:",type(str1))

set1=set(str1)
set2=set(str2)

print("set1의 자료형:", type(set1))
print("set1 출력:",set1)

print("set1과 set2의 합집합:", set1.union(set2))
print("set1과 set2의 교집합:",set1.intersection(set2))
print("set1-set2 차집합:",set1.difference(set2))
print("set2-set1 차집합:",set2.difference(set1))
print("set1과 set2의 배타 집합:",set1.symmetric_difference(set2))