import socket
import threading

from Tools.TcpLink import tcp_link


if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("0.0.0.0", 7840))
    s.listen(100)
    while True:
        # 接受一个新连接:
        sock, add = s.accept()
        # 创建新线程来处理TCP连接:
        t = threading.Thread(target=tcp_link, args=(sock, add))
        t.start()
