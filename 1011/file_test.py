#file_test.py

str="Hello"
f = open("c:/test/a.txt","w")
f.write(str)
f.close()
print("파일쓰기 성공")

str="""Hello,
        Python
            한글"""
f = open("c:/test/b.txt","w",encoding="utf-8") #존재하지 않는 파일은 새로 생성
f.write(str)
f.close()
print("파일쓰기 성공(b.txt)")