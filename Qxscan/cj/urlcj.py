import requests
import re
import threading

ljs = []


def shouji(text):
	global ljs
	headers = {
		'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
		'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
		'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
		'Accept-Encoding': 'gzip, deflate',
		'Referer':'https://www.baidu.com/baidu?tn=monline_3_dg&ie=utf-8&wd=inurl%3Aphp%3Fid%3D'
	}
	xinxi = re.findall('href="http://www.baidu.com/link(.*?)"',text)
	for i in xinxi:
		i = i.strip()
		urls = "http://www.baidu.com/link"+i
		try:
			s = requests.session()
			ymz = requests.get(urls,headers=headers)
			lj = ymz.url
			s.close()
			ljs.append(lj)
		except:
			pass


def paxing(payload):
	headers = {
		'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
		'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
		'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
		'Accept-Encoding': 'gzip, deflate',
		'Referer':'https://www.baidu.com/baidu?tn=monline_3_dg&ie=utf-8&wd=inurl%3Aphp%3Fid%3D'
	}

	ye = 0
	panduan = True
	threads = []
	while panduan:
		print("=正在爬取第 "+str(ye)+" 页=")
		url = "http://www.baidu.com/s?wd="+payload+"&pn="+str((int(ye)-1)*10)+"&oq="+payload+"&ie=utf-8&rsv_page=1&bs="+payload+"&_ss=1&hsug=&f4s=1&csor=13"
		s = requests.session()
		wangye = s.get(url,headers=headers)
		yemian = wangye.text
		if "下一页 &gt;</a>" not in yemian:
			panduan = False
		ye += 1
		s.close()

		t = threading.Thread(target=shouji,args=(yemian,))
		threads.append(t)
		t.start()
			
	for t in threads:
		t.join()
	print("[+]采集完成[+]")

def urlcj_main():
	global ljs
	print("==================进入url采集项==================\n")
	while True:
		zhi = input("请输入采集的值:")
		if zhi:
			break
	zhi = zhi.replace(" ","+")
	paxing(zhi)
	ljs=list(set(ljs))
	with open("lianjie.txt",'w') as txt:
		for i in ljs:
			i = i.strip()
			i += "\n"
			txt.write(i)
	print("[+]已将采集的链接输出到文件: ./lianjie.txt\n")
	print("==================url采集项结束==================\n")
		
