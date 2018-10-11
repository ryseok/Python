

#os_test.py

import os

res = os.access('.', os.W_OK | os.X_OK | os.R_OK)
print(res)

currDir = os.getcwd()#현재 디렉토리를 리턴
print('현재경로: ', currDir)

#os.chdir('c:\\test\\gildong')# 디렉토리 위치를 변경   에러발생: 존재하지 않는 경로 때문.
os.chdir('c:/test/gildong')
print('변경된 현재경로: ', os.getcwd())

for path,dirs, files in os.walk('c:/test/gildong'): #디렉토리 내의 경로, 파일정보얻기
    #c:/test/gildong/
    #c:/test/a.txt
    print(path,dirs,files)

try:
 os.mkdir('c:/test2')#디렉토리 생성

except OSError as e : #try내에서 예외가 발생했다면
    print("예외발생: ",e)
    os.rmdir('c:/test2')#디렉토리 삭제
    print('디렉토리삭제 성공!!')

else:  #try내에서 예외가 발생하지 않았다면
   print('디렉토리생성 성공!!')

file='c:/test/gildong/a.txt'

if os.path.isfile(file): #명시된 경로가 파일이라면
    a = os.path.basename(file)
    b = os.path.split(file)
    c = os.path.normpath(file)

    print('basename: ',a)
    print('split: ',b)
    print('normpath: ',c)

import time

print('파일생성시간1: ',os.path.getctime(file))
print('파일생성시간2: ', time.ctime(os.path.getctime(file)))
print('파일엑세스시간: ', time.ctime(os.path.getatime(file)))
print('파일변경시간: ', time.ctime(os.path.getmtime(file)))
print('파일사이즈: ', os.path.getsize(file))
print('파일명과 확장자 분리: ', os.path.splitext(file))

import  sys
print('시스템 버전: ', sys.version_info)
print('시스템 플랫폼: ', sys.platform)
