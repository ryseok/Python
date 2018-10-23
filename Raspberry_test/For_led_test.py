import RPi.GPIO as GPIO
import time
GPIO.setWarings(False)

# 라즈베리파이 보드핀 넘버를 사용
#GPIO.setmode(GPIO.BOARD)

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

for i in range(0, 100):
    if i == 1:
        GPIO.output(LED18, GPIO.HIGH)
        time.sleep(0.5)
    elif i == 2:
        GPIO.output(LED23, GPIO.LOW)
        time.sleep(0.5)
    elif i == 3:
        GPIO.output(LED24, GPIO.LOW)
        time.sleep(0.5)
    elif i == 4:
        GPIO.output(LED25, GPIO.HIGH)
        time.sleep(0.5)


GPIO.cleanup()

