import socket
TCP_IP = 'localhost'
TCP_PORT = 9999
MESSAGE = "tangina mo"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send(MESSAGE)
s.close()