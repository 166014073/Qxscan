import socket

def cx(host):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect(('183.84.10.201', 43))
	hosts = host+" \r\n"
	s.send(hosts.encode("utf-8"))
	response =b''
	while True:
	    data = s.recv(4096)
	    response += data
	    if not data :
	        break
	s.close()
	print (response.decode())

def whois_main(host):
	print("==进入whois查询项==\n")
	yuming = input("==>请输入要查询的域名(若当前域名则直接输入[y])： ")
	if yuming == "y":
		cx(host)
	else:
		cx(yuming)
	
	print("==查询完成==\n")
