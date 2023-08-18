#coding:utf-8


import socket

#1.创建socket对象
sk=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)  #数据报协议（UDP协议）

#2.绑定地址
sk.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)  #重用端口
sk.bind(('192.168.1.3',5000))

#4.取出连接请求，开始服务
#持续提供服务，并发提供服务

#5.数据传输
while True:
    data,addr=sk.recvfrom(1024)
    print('客户端发过来的数据为：',data)
    sk.sendto(data.upper(),addr)
