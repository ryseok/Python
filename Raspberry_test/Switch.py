import  RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

LED23=23
SW=8

GPIO.setup(LED23,GPIO.OUT)
GPIO.setup(SW,GPIO.IN)

while True:
    flag=GPIO.input(SW)
    GPIO.output(LED23,flag)