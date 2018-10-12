 # sqlite3 란?
	# SQLite3(http://www.sqlite.org/)는 오프라인에서 응용 프로그램에 넣어 사용하는 경량의 임베디드 데이터베이스이다.
	# MSSQL, MySQL과 같은 데이터베이스 관리 시스템과는 다르게 API는 단순히 라이브러리를 호출하는 것만 있으며,
	# 데이터를저장하는데 하나의 파일만을사용하는 것이 특징이다.	
	# 경량이기 때문에 안드로이드 SDK에도 내장되어 사용된다. 

# SQLite의 장점은 다음과 같다
# 	작은 크기와 간결함으로 로컬에서의 간단한 DB 구성에 사용된다.
# 	크로스 플랫폼이며 트랜잭션을 지원한다
# 	오픈소스 프로젝트로 개발 비용이 절감된다.
# 	서버를 포함한 네트워크 구성이 필요 없다

# SqLite는 경량으로 빠른 데이터의 처리를 가장 큰장정으로 가지나 DB 엔진자체가 호스트 프
# 로그램에 임베딩되는 스타일이므로 호스트 프로그램이 DB 처리에 대한 모든 부하를 안을 수
# 있다는 단점을 가진다. 

#  sqlite3의 구문
# sqlite3에서 사용되는 간단한 구문을 정리하면 다음과 같다.
# - 테이블 생성
# CREATE TABLE 테이블명
# (column1 type primary key, column2 type, ...);
# - 질의
# SELECT (column1, column2,column3, ...)
# FROM 테이블명
# WHERE 조건 ;

# Cursor클래스
# 파일을 다루는 파일 핸들(file handle)처럼 데이터베이스에 저장된 파일에 연산을 수행하기 위해서 커서(cursor)를
# 사용한다.
# Cursor클래스는 실질적으로 데이터베이스에 SQL문장을 수행하고, 조회된 결과를 가지고 오는 역할을
# 한다. execute(), executemany(), executescript()는Connection 클래스와 동일하다



#coding : utf-8

#sql_test.py
import sqlite3
import os

db_fileName = "Book.db" #데이터베이스명(저장소명 = 파일)

db_is_new = not os.path.exists(db_fileName) #DB파일이 있는지 확인, not 생성시 True
print("db_is_new : ",db_is_new)

conn = sqlite3.connect(db_fileName) #없는 DB에 대한 생성, 연결
print(conn) #connection 객체

if db_is_new:
    print(db_fileName,"DB생성 합니다.")
else:
    print("이미 DB가 생성되었습니다.")

conn.close()