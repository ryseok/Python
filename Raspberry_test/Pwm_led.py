import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

LED23=23
LED25=25

GPIO.setup(LED23, GPIO.OUT)
GPIO.setup(LED25, GPIO.OUT)

pwm = GPIO.PWM(LED23, 100)  # 100hz


pwm.start(0)

for i in range(0, 3):

    for dc in range(0, 101, 5):
        pwm.ChangeDutyCycle(dc)
        time.sleep(0.1)
    for dc in range(100, -1, -5):
        pwm.ChangeDutyCycle(dc)
        time.sleep(0.1)

pwm.stop()
GPIO.cleanup()