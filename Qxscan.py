import dksm
import cdsm
import webbp
import whois
import ipjx
import zymcx
import zymbp
import options
import dzcx

def xiugai():
	#修改ip与端口
	global host
	global port
	host = input("请输入目标ip或域名： ")
	port = input("请输入目标端口: ")
	if "http://" in host:
		host = host.replace("http://","")
	if "https://" in host:
		host = host.replace("https://","")
	if "/" in host:
		host = host.replace("/","")
		

def biaoti():
	print("""  ___                            
 / _ \ __  _____  ___ __ _ _ __  
| | | |\ \/ / __|/ __/ _` | '_ \ 
| |_| | >  <\__ \ (_| (_| | | | |
 \__\_\/_/\_\___/\___\__,_|_| |_|
                                 """)
	xinxi = "Qxscan: v1.2\n"
	xinxi += "======== BY:F_Dao||QQ:166014073========\n\n"

	print(xinxi)

def kaitou(host,port):
	dizhi = dzcx.dzcx_main(host)
	#打印绑定ip与端口以及选项
	xinxi = "HOST： "+host+" PORT: "+port+"\n"
	xinxi +="物理地址： "+dizhi+"\n"
	xinxi += "选项： \n"
	xinxi += "[0]-更改ip与端口-\n"
	xinxi += "[1]-端口扫描-\n"
	xinxi += "[2]-c段扫描-\n"
	xinxi += "[3]-web爆破-\n"
	xinxi += "[4]-whois查询-\n"
	xinxi += "[5]-ip解析-\n"
	xinxi += "[6]-子域名查询-\n"
	xinxi += "[7]-子域名爆破-\n"
	xinxi += "[8]-http方法查询-\n"
	xinxi += "\n[exit]-退出-"
	
	print(xinxi)
	global xuanxiang
	xuanxiang = input("\n请输入操作编号：")
	
def main():
	#程序入口
	biaoti()
	xiugai()
	while True:
		print("=======================================")
		kaitou(host,port)
		global xuanxiang
		if xuanxiang == "1":
			dksm.dksm_main()
		if xuanxiang == "exit":
			exit(0)
		if xuanxiang == "0":
			xiugai()
		if xuanxiang == "2":
			cdsm.cdsm_main(host)
		if xuanxiang == "3":
			webbp.webbp_main(host,port)
		if xuanxiang == "4":
			whois.whois_main(host)
		if xuanxiang == "5":
			ipjx.ipjx_main(host)
		if xuanxiang == "6":
			zymcx.zymcx_main(host)
		if xuanxiang == "7":
			zymbp.zymbp_main(host)
		if xuanxiang == "8":
			options.options_main(host)
		

if __name__ == "__main__":
	main()
