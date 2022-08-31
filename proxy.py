#!/usr/bin/python3
#/create by rozhbasxyz

###---[ GLOBAL ERROR ]---###
def erorr_nih(isi):
	error = str(isi).split("'")[1].split("'")[0]
	exit("[\033[91m!\033[00m] terdapat error : "+error)

###---[ IMPORT MODULE ]---###
try:
	import requests, re, bs4, sys, os
except Exception as e:
	erorr_nih(e)

###---[ GLOBAL NAME ]---###
parser = bs4.BeautifulSoup
H = "\033[92m"
P = "\033[00m"
M = "\033[91m"
url_ip = "https://ipinfo.io/json"

###---[ DUMP PROXY AKTIF ]--###
class Proxies:
	def __init__(self):
		self.r = requests.Session()
		self.no, self.prox = 0, []
		self.get_proxy()
	
	def get_proxy(self): # socks 4/5 server IRAN-USA-RUSIA
		try:
			link = parser(self.r.get("https://hidemy.name/en/proxy-list/?country=IRRUUS&type=5#list",headers={"user-agent": "Mozilla/5.0 (Mobile; rv:48.0; A405DL) Gecko/48.0 Firefox/48.0 KAIOS/2.5"}).text, "html.parser")
			for x in re.findall("<tr><td>(.*?)</td><td>(.*?)</td><td>",str(link)):
				if "IP" in str(x):pass
				else:self.prox.append(x[0]+':'+x[1])
		except Exception as e:
			error_nit(e)
		if len(self.prox)==0:
			exit(f"[{M}!{P}] gagal dump proxy")
		else:
			self.cek_proxy()
	
	def cek_proxy(self): # cek proxy yang aktif 
		try:
			ip_asli = self.r.get(url_ip).json()["ip"]
			for data in self.prox:
				self.no += 1
				proxy = {"https": "socks4://"+data}
				print(f"\r[{H}{self.no}{P}/{H}{len(self.prox)}{P}] mencoba : {data}",end="")
				sys.stdout.flush()
				try:
					ip_pro = self.r.get(url_ip,proxies=proxy).json()["ip"]
					print(f"\r[{H}*{P}] socks4   : {data}      \n[{H}*{P}] ip asli  : {ip_asli}\n[{H}*{P}] ip proxy : {ip_pro}\n[{H}*{P}] status   : aktif        \n")
				except:
					print(f"\r[{M}*{P}] socks4   : {data}      \n[{M}*{P}] status   : mati        \n")
		except Exception as e:
			error_nih(e)

if __name__=="__main__":
	dev = sys.platform.lower()
	if "linux" in dev:os.system("clear")
	elif "win" in dev:os.system("cls")
	else:os.system("clear")
	Proxies()
