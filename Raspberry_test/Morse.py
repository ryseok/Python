import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

LED23=23
LED25=25

#LED23를 출력포트로 사용하겠음.
GPIO.setup(LED23,GPIO.OUT)
GPIO.setup(LED25,GPIO.OUT)

#초기 OFF 설정
GPIO.output(LED23,False)
time.sleep(2.4)


GPIO.output(LED23, True)
time.sleep(0.4)
GPIO.output(LED23, False)
time.sleep(1.2)

#S 모스부호
GPIO.output(LED23,True)
time.sleep(0.4)
GPIO.output(LED23,False)
time.sleep(0.4)

GPIO.output(LED23,True)
time.sleep(0.4)
GPIO.output(LED23,False)
time.sleep(0.4)

GPIO.output(LED23,True)
time.sleep(0.4)
GPIO.output(LED23,False)
time.sleep(0.4)

GPIO.output(LED23, True)
time.sleep(0.4)
GPIO.output(LED23, False)
time.sleep(1.2)
#==========================

def LedOn(Port,Delay):
    GPIO.output(LED25, True)
    time.sleep(Delay)

def LedOff(Port,Delay):
    GPIO.output(LED25, False)
    time.sleep(Delay)

def Send_s():
    LedOn(LED25,0.4)
    LedOff(LED25,0.4)
    LedOn(LED25,0.4)
    LedOff(LED25,0.4)
    LedOn(LED25,0.4)
    LedOff(LED25,1.2)

def Send_o():
    LedOn(LED25, 1.2)
    LedOff(LED25, 0.4)
    LedOn(LED25, 1.2)
    LedOff(LED25, 0.4)
    LedOn(LED25, 1.2)
    LedOff(LED25, 1.2)

LedOff(LED25, 1.2)

while(1):
    Send_s()
    Send_o()
    Send_s()




