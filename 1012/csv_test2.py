

#csv_test2.py  (입력데이터를 통한 CSV파일생성)

import csv
f = open('result.csv','wt',newline='') #출력파일 생성 (쓰기 --> 콤마 구분 데이터)
try:
  writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC ) # 쓰기 객체 생성
  writer.writerow( ('No','Alpha','Date')  ) #쓰기 실행(행단위 출력)
  for i in range(6): # 0~5
      writer.writerow( (i+1,  chr(ord('a')+i ),   '2018/%2d/12'%(i+1)  )     )
                         #ord('a') : 97 ,     chr(97+1) : 'b'
finally:
    f.close()

print ( open ( "result.csv" , 'rt' ) . read ())

