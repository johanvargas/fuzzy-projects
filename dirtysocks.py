# basic socket usage
import socket

socket.setdefaulttimeout(2)

s = socket.socket()

try:
	s.connect(("127.0.0.1", 8000))
	ans = s.recv(1024)
except Exception, e:
	print('Error {}'.format(e))
