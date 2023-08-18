import socketserver,sys


ip = '192.168.1.3'
port = 5000


class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        #self.request,self.client,self.server
        conn=self.request
        #conn.sendall(bytes('hello'),encoding=('utf-8'))
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
        pass


if __name__=='__main__':
    try:
        server=socketserver.ThreadingTCPServer((ip,port),MyServer)
        server.serve_forever()          #while循环
    except KeyboardInterrupt:
        sys.exit()