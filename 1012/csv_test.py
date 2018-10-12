#csv_test.py
import csv
f = open("book.csv","rt")

try:
    reader =  csv.reader(f)
    for row in reader:
        print(row) #row ===> list형태
    print("=============================")
    f.seek(0) #읽기 포인트를 파일의 맨앞으로 이동
    reader2 =  csv.DictReader(f)
    for row in reader2:
        #print(row) #row ===> list형태
        print( dict(row))
    print("=============================")

finally:
    f.close()