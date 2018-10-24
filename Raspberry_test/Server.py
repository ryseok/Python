# Server.py

import socket
import RPi.GPIO as IoPort

IoPort.setwarnings(False)
IoPort.setmode(IoPort.BCM)

LED1, LED2, LED3, LED4 = 18, 23, 24, 25
F1, F2, F3, F4 = 0, 0, 0, 0  # False,False,False,False

IoPort.setup(LED1, IoPort.OUT)
IoPort.setup(LED2, IoPort.OUT)
IoPort.setup(LED3, IoPort.OUT)
IoPort.setup(LED4, IoPort.OUT)

s = socket.socket()  # s : Socket객체
s.bind(('192.168.0.24', 20000))  # bind(서버ip,port넘버)
s.listen(10)
print('Server Start.....')
conn, addr = s.accept()  # 클라이언트 접속 대기
print('클라이언트 접속!!>>>', addr)
while True:
    receive_data = conn.recv(4096).decode('UTF-8')  # 클라이언트가 보낸 byte를 문자로 변환
    print("from Client>>>", receive_data)
    if receive_data == '1':
        # IoPort.output(LED1, True)
        F1 = not F1
        IoPort.output(LED1, F1)

    elif receive_data == '2':
        F2 = not F2
        IoPort.output(LED2, F2)
    elif receive_data == '3':
        F3 = not F3
        IoPort.output(LED3, F3)
    elif receive_data == '4':
        F4 = not F4
        IoPort.output(LED4, F4)

    # send_data = input("응답: ")
    # conn.send(bytes(send_data+'\n','UTF-8'));  #콘솔통해 입력받은 문자열을 클라이언트에게 byte로 보냄