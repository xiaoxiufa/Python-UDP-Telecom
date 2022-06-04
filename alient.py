import socket
def main():
    s=socket.socket()
    host="192.168.203.149"#要连接的ip
    port=4444
    s.connect((host,port)) #连接服务器
    msf=input("发送的信息",)
    print(s.recv(1024).decode("utf-8"))
    s.send(msf.encode("utf-8"))
    #print(s.recv(1024).decode("utf-8"))
    s.close()
    pass
if __name__ == '__main__':
    main()
