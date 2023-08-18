#coding:utf-8


import socket
ip='192.168.1.3'
port=5000

#1.创建socket对象
sk=socket.socket(socket.AF_INET,socket.SOCK_STREAM)  #流式协议（tcp协议）

#2.建立连接
sk.connect((ip,port ))

#3.传输数据
while True:
    #sk.send('hello'.encode('utf-8'))
    msg=input('请输入>>>>').strip()
    sk.send(msg.encode('utf-8'))
    if not msg:
        continue
    if msg == 'q':
        break

    data=sk.recv(1024)
    print(data.decode('utf-8'))

#4.关闭连接
sk.close()