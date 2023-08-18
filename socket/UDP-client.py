#coding:utf-8


import socket

#1.创建socket对象
sk=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)  #流式协议（tcp协议）

#3.传输数据
while True:
    #sk.send('hellowwwwwwwwwwwwwwwwwww'.encode('utf-8'))
    msg=input('请输入>>>>').strip()
    if msg == 'q':
        break
    sk.sendto(msg.encode('utf-8'),('192.168.1.3',5000))

    data,addr=sk.recvfrom(1024)
    print(data)

#4.关闭连接
sk.close()