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

#f=open("c:/test/c.txt") #mdoe w(write)없이 존재하지 않는 파일을 open하면 에러발생
f=open("c:/test2/c.txt","w") #존재하지 않는 디렉토리(폴더) 에러발생
linesTxt = ["first text\n","second text\n", "thrid\t text"]
f.writelines(linesTxt)
f.close()