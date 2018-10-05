

#assert_test.py
#assert: 특정 조건을 만족했을때 예외 발생
#형식: assert 조건식 메시지

def check_assert():
    a=3
    b=6
    assert a<b , "a가 b보다 작습니다!!" #조건식결과가 false일때 Exception발생
    print('a=',a,',b=',b)

try:
 check_assert()
except Exception as e:
    print('Exception: check_Assert',e)
    
#UnitTest테스트(단위테스트)
import unittest
class MyTest(unittest.TestCase):
    def test(self):
        print('테스트1')

    def test2(self):
        print('테스트2')

ts = unittest.TestSuite()
ts.addTest(MyTest("test"))
ts.addTest(MyTest("test2"))

#unittest.main()

import sys
print(sys.path)


    



