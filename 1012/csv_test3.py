




#csv_test3.py ( CSV파일을 읽어서 DB에 저장)

# book.csv의 no, title를 읽어 mycsv.db의 mybook테이블(id,name)에 저장
import  sqlite3
import  csv

conn = sqlite3.connect('mycsv.db')
cur = conn.cursor()

cur.execute('drop table if exists mybook')
cur.execute('''create table mybook (
                 id integer,
                 name text
            )''')
f = open('book.csv','r')
#reader = csv.reader(f)
reader = csv.DictReader(f)

for row in reader:
    #t = (row[0],row[1])
    t = (row['no'],row['title'])
    cur.execute("insert into mybook values (?,?)", t )
conn.commit()

#DB조회
for row in cur.execute("select * from mybook"):
    print(row)

cur.close()
