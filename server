服务端:
====================
import socket
def main():
    s=socket.socket()#导入socket模块
    host=socket.gethostname()#获取ip地址
    port=4444
    s.bind((host,port))#邦定ip地址和端口
    s.listen(5)#最多可以连接五个人
    c,addr=s.accept()#建立和对方的连接，c=套节字，addr=对方的ip地址
    print("对方的ip地址是",addr)
    c.send('welcome'.encode("utf-8"))#发送一个welcome给客户端，使用Utf-8编码
    print(c.recv(1024).decode("utf-8"))#接受客户端的信息并进行utf-8解码
    c.close()#关闭
    pass
if __name__ == '__main__':
    main()
