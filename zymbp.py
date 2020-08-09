import socket
import threading
import requests
import re
import queue


def zid(wenjian):
		
	words = queue.Queue()
	
	with open(wenjian,encoding='gbk') as zd:
		for i in zd:
			words.put(i)
			
	return words

def xxx(host):
	url = "http://"+host
	try:
		qingqiu = requests.get(url,timeout=2)
	except:
		print(host+" -- 端口开放但连接错误")
	try:
		qingqiu.encoding = qingqiu.apparent_encoding
		wangye = qingqiu.text
		title = re.findall("<title>.*?</title>",wangye)
	except:
		pass
	try:
		w = qingqiu.headers
	except:
		pass
	xinxi = ""
	try:
		if w['server']:
			xinxi += "服务器："+w['server']
	except:
		pass
	try:
		if w['X-Powered-By']:
			xinxi += "\n信息："+w['X-Powered-By']
	except:
		pass
	try:
		if title:
			biaoti = title[0]
			biaotis = biaoti.replace("<title>","") 
			biaotiss = biaotis.replace("</title>","")
			xinxi += "\n标题:"+biaotiss
	except:
		pass
	xinxi += "\n==========================================="
	print("[+]"+"http://"+host+"\t+开启+"+"\n"+xinxi)



	
def saomiao(host,port):
	try:
		socket.setdefaulttimeout(1)
		lianjie = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		lianjie.connect((host,port))
		host_port=host+":"+str(port)
		lianjie.close()		
		xxx(host_port)
	except:
		return

def zhuym(xinxi):
	lb = xinxi.split(".")
	yuming = lb[-2]+"."+lb[-1]
	return yuming

def zymbp_main(yuming):
	global list_ip
	threads = []
	print("==进入子域名爆破项==\n")
	pd = input("请输入要爆破的域名(当前域名请直接回车):")
	if pd:
		yumings = zhuym(pd)
	else:
		yumings = zhuym(yuming)
	xc = input("请输入线程: ")
	zym = zid("./zd/zymbp/zym.txt")
	for i in range(int(xc)):
		t = threading.Thread(target=main_a,args=(zym,yumings,))
		threads.append(t)
		t.start()
	
	for t in threads:
		t.join()
	print("==扫描完成==\n")
	

def main_a(zym,yuming):
	dk=80
	while True:
		if zym.empty():
			return
		else:
			i = zym.get()
			i = i.strip()
			url = i+"."+yuming
			saomiao(url,dk)
		
		
		
		


