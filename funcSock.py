import socket

def retBanner(ip, port):
    try:
        socket.setdefaulttimeout(5)
        s = socket.socket()
        s.connect((ip,port))
        print('Connected to {0}:{1}'.format(ip,port))
        banner =s.recv(1024)
        print('Received Banner: ', banner)
        return banner;
    except Exception as e:
        print('Error: ', e)
        return

def main():
	ip1 = '192.168.96.148'
	#ip1 = '74.125.68.105'
	ip2 = '192.168.96.149'
	ip3 = '192.168.96.150'
	port = 21

	banner1 = retBanner(ip1, port)
	if banner1:
		print('IP 1 Banner:', banner1)
		checkVulns(banner1)
	banner2 = retBanner(ip2, port)
	if banner2:
		print('IP 2 Banner:', banner2)
		checkVulns(banner2)
	banner3 = retBanner(ip3, port)
	if banner3:
		print('IP 2 Banner:', banner3)
		checkVulns(banner3)
		
	print('IP 1 Banner: {0} and IP 2 Banner: {1} and IP 3 Banner: {2}'.format(banner1, banner2, banner3))

def checkVulns(banner):
	if ("FreeFloat Ftp Server (Version 1.00)" in banner):
		print("[+] FreeFloat FTP Server is vulnerable.")
	elif ("3Com 3CDaemon FTP Server Version 2.0" in banner):
		print("[+] 3CDaemon FTP Server is vulnerable.")
	elif("Ability Server 2.34" in banner):
		print("[+] Ability FTP Server is vulnerable.")
	elif("Sami FTP Server 2.0.2" in banner):
		print("[+] Sami FTP Server is vulnerable.")
	else:
		print("Sami FTP Server 2.0.2")
		
if __name__ == '__main__':
    main()
