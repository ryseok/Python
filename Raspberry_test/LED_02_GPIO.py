import RPi.GPIO as GPIO

import time

GPIO.setmode(GPIO.BCM)

LED18 = 18
LED23 = 23
LED24 = 24
LED25 = 25

dc = [0,1,2,3,4,5,6,7,8,9,10,12,13,14,15,16,17,18,20,30,50,70,100]

GPIO.setup(LED18, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(LED23, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(LED24, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(LED25, GPIO.OUT, initial=GPIO.LOW)

p18 = GPIO.PWM(LED18, 100)
p23 = GPIO.PWM(LED23, 100)
p24 = GPIO.PWM(LED24, 100)
p25 = GPIO.PWM(LED25, 100)

p18.start(0)
p23.start(0)
p24.start(0)
p25.start(0)

try :
    while 1:
        for val in dc:
            p18.ChangeDutyCycle(val)
            p23.ChangeDutyCycle(val)
            p24.ChangeDutyCycle(val)
            p25.ChangeDutyCycle(val)
            time.sleep(0.1)
        dc.reverse()
        time.sleep(0.1)
except KeyboardInterrupt:
    pass

p18.stop()
p23.stop()
p24.stop()
p25.stop()

GPIO.cleanup()



