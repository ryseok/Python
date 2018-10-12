

#sql_test4.py

#정렬된 조회, dump파일만들기

import  sqlite3

con = sqlite3.connect('book.db')
cur = con.cursor()

#정렬 조건을 표현하는 함수정의
def myFunc(str1,str2):
    s1 = str1.upper() #전체 대문자 변환
    s2 = str2.upper()
    #return (s1>s2) - (s1<s2)   #오름차순정렬
    return (s1<s2) - (s1>s2)   #내림차순정렬

#  s1='python'   s2='abc'     :     true-false    1-0 : 1 (true)
#  s1='abc'   s2='abc'       :      false-true    0-1 : -1

con.create_collation('myordering',myFunc) #명시적인 별칭과 핸들러(myFunc) 대입
cur.execute('select title  from book order by title COLLATE myordering')
for r in cur:
    print(r[0])


for l in con.iterdump(): #실행된 쿼리구문을 덤프로 만들어 출력.
    print(l)

with open('dump.sql','w',encoding='utf-8') as f:#실행된 쿼리구문을 덤프파일로 출력.
 for l2 in con.iterdump():
    #f.write(l2+'\n')
    f.write('{0}\n'.format(l2))


