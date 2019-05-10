import socket

s = socket.socket()
print("Socket Successfully Created")

port = 12345

s.bind(('', port))
print('socket binded to {0}'.format(port))

s.listen(5)
print('Socket is Listening')

while True:
	c, adr = s.accept()
	print('Got Connection from {0}'.format(adr))
	
	c.sendall(b'Thank You for Connecting')
	
	c.close()
