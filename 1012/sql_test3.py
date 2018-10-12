#sql_test3.py
#DB수정

import sqlite3
db = sqlite3.connect("book.db")
cursor = db.cursor()

#전달인자가 없다면 execute(), 전달인자 있다면 executemany( , [튜플])
cursor.execute("update book set title='Python3' where no=1")
print("커서 카운트 >>>", cursor.rowcount)

cursor.execute("select * from book")
#조회된 결과 모두를 리스트형태로 반환
print(cursor.fetchall())

cursor.close()
db.commit()
db.close()