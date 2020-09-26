import socket
import re
import queue

def zwzd():
	zwlb = []
	with open('./zd/zwsb/cms.txt',encoding='utf-8') as txt:
		for i in txt:
			i.strip()
			i.strip('\n')
			i.strip('\r')
			q = re.findall('.*?\|',i)
			zwlb.append(q)
	return zwlb

def guol(i):
	i = i.replace("%0a","")
	i = i.replace("%0A","")
	i = i.replace("%0d","")
	i = i.replace("%0D","")
	i = i.replace("\n","")
	i = i.replace("\r","")
	i.strip()
	return i


def zid(lb):
		
	words = queue.Queue()
	
	for i in lb:
		words.put(i)
			
	return words


zwzds = zwzd()

zwzdqueu = zid(zwzds)


while not zwzdqueu.empty():
	i = zwzdqueu.get()
	w = i[0]
	e = i[1]
	w = w.replace("|","")
	e = e.replace("|","")
	w = guol(w)
	print(w)