

#sql_test2.py (DB연결, 테이블생성, 데이터추가, 데이터조회)

import sqlite3

db = sqlite3.connect("Book.db")  #DB연결
cur = db.cursor() #커서객체 생성

cur.execute('drop table if exists Book')
a=cur.execute('create table Book (no integer, title text)') #테이블생성
b=cur.executemany('insert into Book values (?,?)', [(1,'파이썬')])
print('입력한 데이터 갯수: ', cur.rowcount)

#cur.executemany('insert into Book values (2,"JAVA")',[])
#cur.execute('sql문')
#cur.executemany('sql문',열거가능한 데이터)
cur.execute('insert into Book (no,title) values (2,"JAVA")')
print('입력한 데이터 갯수: ', cur.rowcount) #실행된 행의 갯수 

cur.executemany('insert into Book (no,title) values (?,?)', [(3,'HTML'),(4,'JSP'),(5,'자바스크립트')])
print('입력한 데이터 갯수: ', cur.rowcount) #실행된 행의 갯수


print("타입체크 >>>", type((1,2,3)))
#title없는 no만 6~10까지 입력
for i in range(6,11):
    cur.executemany("insert into book (no) values (?)", [(i,)])


print('a=',a)
print('b=',b)

#데이터 조회
cur.execute('select no,title from book')
for row in cur:
    print(row)  #튜플 리턴

print("[데이터 조회2]")
cur.execute("select * from Book")
for row2 in cur:
    print(row[0], row2[1]) #컬럼 인덱스를 명시

db.commit()
db.close()







