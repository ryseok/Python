


#sql_test5.py (Mydb생성, test테이블 생성, 데이터를 입력(인덱스, 콜론 통한))

import sqlite3

db = sqlite3.connect('Mydb.db')
cur = db.cursor()

cur.execute('drop table if exists test')
sql_cmd='create table test (id integer,name text)'
cur.execute(sql_cmd)

#execute 통한 입력
sql_cmd = 'insert into test values (?,?)'
cur.execute(sql_cmd, (1,'나영석'))
cur.execute(sql_cmd, (2,'홍길동'))

for row in cur.execute('select * from test'):
    print(row)

print("====================================")

#콜론을 통한 입력
sql_cmd2 = "insert into test values (:id, :name)"
cur.execute(sql_cmd2,{"id" : 3, "name" : "김주원"})
cur.execute(sql_cmd2,{"id" : 4, "name" : "김유신"})
for row in cur.execute('select * from test'):
    print(row)