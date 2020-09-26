import optparse
import socket
import queue
import threading

duankou = {"20":"ftp-data","21":"ftp","22":"ssh","23":"telnet","25":"smtp",
			"53":"dns","80":"http","81":"hosts2-ns","135":"msrpc","8080":"http",
			"139":"netbios-ssn","443":"https","445":"smb","1723":"pptp",
			"3306":"mysql","3389":"rdp","1433":"mssql","888":"bt","8888":"bt"}

def qqq(zidian):
	words = queue.Queue()
	for i in zidian:
		words.put(i)
	return words

def dksm(host,port):
	try:
		socket.setdefaulttimeout(2)
		lianjie = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		lianjie.connect((host,int(port)))
		return "1"
		lianjie.close()
		
	except:
		return "0"
	
	
def duankous(port):
	ports = port.split("-")
	portss = [list(range(int(ports[0]),int(ports[1])+1))]
	return portss
	
def ipy(host):
	l = host.find("/")
	s = host[0:l]
	q = s.split(".")
	liebiao = []
	for i in range(0,256):
		f = q[0]+"."+q[1]+"."+q[2]+"."+str(i)
		liebiao.append(f)
		
	return liebiao





def csxinxi():
	global port
	global xiancheng
	global ports
	global host
	
	port = input("[-]请输入要扫描的端口： ")

	xiancheng = input("[-]请输入线程： ")
	
	host = input("[-]请输入域名或ip: ")
	if port:
		if "-" in port:
			ports = duankous(port)
		else:
			ports = False
	else:
		port = False
		ports = False





	

def dksm_main():
	print("==进入端口扫描项==\n")
	
	csxinxi()
	if "/" in host:
		hosts = ipy(host)
	else:
		hosts = False
	threads = []
	if hosts:
		if ports:
			for ip in hosts:
				t=threading.Thread(target=main_a,args=(ip,ports,))
				threads.append(t)
				t.start()
		if port and (not ports):
			for ip in hosts:
				t=threading.Thread(target=main_b,args=(ip,port,))
				threads.append(t)
				t.start()
		if (not port) and (not ports):
			for ip in hosts:
				t=threading.Thread(target=main_d,args=(ip,duankou,))
				threads.append(t)
				t.start()
	if host and (not hosts):
		if ports:
			for dks in ports:
				dkq = qqq(dks)
				if xiancheng:
					for i in range(0,int(xiancheng)):
						t=threading.Thread(target=main_c,args=(host,dkq,))
						threads.append(t)
						t.start()
				else:
					t=threading.Thread(target=main_c,args=(host,dkq,))
					threads.append(t)
					t.start()
		if port and (not ports):
			t=threading.Thread(target=main_b,args=(host,port,))
			threads.append(t)
			t.start()
		if (not port) and (not ports):
			dks = []
			for p,fuwu in duankou.items():
				dks.append(p)
			dkp = qqq(dks)
			if xiancheng:
				for i in range(0,int(xiancheng)):
					t=threading.Thread(target=main_e,args=(host,dkp,duankou,))
					threads.append(t)
					t.start()
			else:
				t=threading.Thread(target=main_e,args=(host,dkp,duankou,))
				threads.append(t)
				t.start()
	for t in threads:
		t.join()
	print("==扫描完成==\n")

		
		
def main_a(ip,dks):
	for dk in dks:
		for d in dk:
			panduan = dksm(ip,d)
			if panduan == "1":
				print("[+]"+ip+":"+str(d))
					
def main_b(ip,dk):
	panduan = dksm(ip,dk)
	if panduan == "1":
		print("[+]"+ip+":"+str(dk))

def main_c(ip,dkq):
	while not dkq.empty():
		dk = dkq.get()
		dk_list =[]
		dk_list.append(dk)
		for d in dk_list:
			panduan = dksm(ip,d)
			if panduan == "1":
				print("[+]"+ip+":"+str(d))
		
	
def main_d(ip,duankou):
	for port,fuwu in duankou.items():
		panduan = dksm(ip,port)
		if panduan == "1":
			print("[+]"+ip+":"+str(port)+"\t"+fuwu)

def main_e(ip,dkp,zidian):
	while not dkp.empty():
		dk = dkp.get()
		dk_list =[]
		dk_list.append(dk)
		for d in dk_list:
			panduan = dksm(ip,d)
			if panduan == "1":
				print("[+]"+ip+":"+str(d)+"\t"+zidian[str(d)])
		
if __name__ == '__main__':
	dksm_main()

