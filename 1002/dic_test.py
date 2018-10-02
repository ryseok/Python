#dic_test.py

dic1={}
print("dic1의 자료형:", type(dic1))

#dic2={"key":"안녕"}
dic2={"name":"홍길동","age":"12","job":"학생"}
print("dic1의 key:",dic2.keys())
print("dic2의 value:",dic2.values())
#print("모든 내용 삭제후 dic2:",dic2.clear()) #결과 : None

#dic2.clear()
#print("모든 내용 삭제후 dic2:",dic2) #결과 : {}

print("저장 이름:",dic2.get("name"))