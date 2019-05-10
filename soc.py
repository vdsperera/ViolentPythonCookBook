import socket

socket.setdefaulttimeout(20)
##s = socket.socket()
##s.connect(("www.cricbuzz.com",443))
#ans = s.recv(1024)
#print(ans)

##ip = socket.gethostbyname("www.google.com")
##print(ip)
s = socket.socket()
s.connect(("192.168.95.148",21))
ans = s.recv(1024)
if ("FreeFloat Ftp Server (Version 1.00)" in ans):
    print("[+] FreeFloat FTP Server is vulnerable.")
elif ("3Com 3CDaemon FTP Server Version 2.0" in ans):
    print("[+] 3CDaemon FTP Server is vulnerable.")
elif("Ability Server 2.34" in ans):
    print("[+] Ability FTP Server is vulnerable.")
elif("Sami FTP Server 2.0.2" in ans):
    print("[+] Sami FTP Server is vulnerable.")
else:
    print("Sami FTP Server 2.0.2")

