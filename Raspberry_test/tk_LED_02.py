import RPi.GPIO as GPIO
import tkinter

import time

GPIO.setmode(GPIO.BOARD)

LED = 11

dc = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,15,20,30,50,70,100]

GPIO.setup(LED, GPIO.OUT, initial=GPIO.LOW)

p = GPIO.PWM(LED, 100)

root = tkinter.Tk()

led_val = tkinter.DoubleVar()

led_val.set(0)

p.start(0)

def change_duty(dc):
    p.ChangeDutyCycle(led_val.get())

s = tkinter.Scale(root, label = 'LED', orient='h',\
                  from_ = 0, to = 100, variable = led_val, command = change_duty)

s.pack()

root.mainloop()

p.stop()

GPIO.cleanup()


