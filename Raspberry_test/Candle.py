import RPi.GPIO as GPIO
import time

def candle(port,on,off):
    for i in range(0,30):
        GPIO.output(port,True)
        time.sleep(on)

        GPIO.output(port,False)
        time.sleep(off)

LED23=23
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED23,GPIO.OUT)

for i in range(0.40):
    sub=i*0.0005
    candle(LED23, 0.02-sub, 0.01)