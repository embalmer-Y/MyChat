"""
This file holds the handler after the connection has been established
"""
import time

from Tools.Encryption import decrypt
from Tools.UserMsg import ChatParty


def tcp_link(sock, add):
    print('Accept new connection from %s:%s...' % add)
    sock.send(b'Welcome!Connect successful')
    key = sock.recv(1024)
    msg_dict = eval(key.decode('utf-8'))
    name = msg_dict["name"]
    chat = ChatParty()
    g = chat.send_msg(name=name)
    while True:
        data = sock.recv(1024)
        time.sleep(2)
        data_dict = eval(data.decode('utf-8'))
        if not data or decrypt(data_dict["msg"], key=data_dict["key"]) == 'exit':
            break
        else:
            chat.user_msg_init(msg=data_dict)
        try:
            un_encode_msg = next(g)
            sock.send(un_encode_msg.encode('utf-8'))
        except StopIteration as e:
            print('Generator return value:', e.value)
        finally:
            pass
    print('Connection from %s:%s closed.' % add)
