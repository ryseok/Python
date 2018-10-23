import RPi.GPIO as GPIO
import time

GPIO.setWarings(False)


# 라즈베리파이 보드핀 넘버를 사용
GPIO.setmode(GPIO.BCM)


LED18 = 18
LED23 = 23
LED24 = 24
LED25 = 25


# 12번 핀을 출력모드로 설정한다.
GPIO.setup(LED18, GPIO.OUT)
GPIO.setup(LED23, GPIO.OUT)
GPIO.setup(LED24, GPIO.OUT)
GPIO.setup(LED25, GPIO.OUT)

i = 0
while i < 10:
    GPIO.output(LED18, True)
    GPIO.output(LED23, True)
    GPIO.output(LED24, True)
    GPIO.output(LED25, True)
    time.sleep(0.5)

    GPIO.output(LED18, False)
    GPIO.output(LED23, False)
    GPIO.output(LED24, False)
    GPIO.output(LED25, False)
    time.sleep(0.5)

    i += 1

GPIO.cleanup()

