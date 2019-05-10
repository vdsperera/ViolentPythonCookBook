import socket
import sys

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket is Successfully Created")
except socket.error as er:
    print("Socket Creation Failed with Error {0}".format(er))

port = 80

try:
    host_ip = socket.gethostbyname('www.google.com')
except socket.gaierror:
    print("there was an error resolving the host")
    sys.exit()

s.connect((host_ip, port))
print("the socket has successfully connected to google.com on port {0}".format(host_ip))
