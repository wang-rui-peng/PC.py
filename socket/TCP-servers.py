#coding:utf-8


import socket,socketserver
from multiprocessing import Process    #进程
from threading import Thread           #线程
ip='192.168.1.3'
port=5000


def task(conn):
    # 5.数据传输
    while True:
        try:  # windows上的解决办法
            data = conn.recv(1024)
        except:
            break
        if not data:  # linux和mac报错处理
            break
        data = data.decode('utf-8')
        print('客户端发过来的数据为：', data)

        conn.send(data.upper().encode('utf-8'))

    # 6.结束服务
    conn.close()

def run(ip,port):
    # 1.创建socket对象
    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 流式协议（tcp协议）

    # 2.绑定地址
    sk.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # 重用端口
    sk.bind((ip,port ))

    # 3.监听连接请求（开始营业）
    sk.listen(5)  # 5为半连接池大小
    print('服务端已启动成功，在5000这个端口等待客户连接')

    # 4.取出连接请求，开始服务
    # 持续提供服务，并发提供服务
    while True:
        conn, addr = sk.accept()
        print('连接对象：', conn)
        print('客户端ip+端口：', addr)

        # 进程实现并发
        # p = Process(target=task, args=(conn,))
        # p.start()

        # 线程实现并发
        Thread(target=task, args=(conn,)).start()


if __name__=='__main__':
    run(ip,port)