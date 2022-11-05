#!/usr/bin/python3
#/create by rozhbasxyz

import requests, socks, random, re, bs4, base64, os
from bs4 import BeautifulSoup as parser
from random import choice as rc
from random import randint as rr
pro = []


class Proxx:
	def __init__(self):
		self.ses =  requests.Session()
		print("sedang dump proxy mohon tunggu")
		self.dump1()
		self.dump2()
		self.dump3()
		self.dump4()
		self.dump5()
		self.dump6()
	
	def main(self,isi): # cek proxy
		global pro
		try:
			proxy = {"https": "socks4://%s"%isi, "http": "socks4://%s"%isi}
			data = self.ses.get("https://ipinfo.io/json",proxies=proxy, timeout=0.5).json()
			ip = data["ip"]
			kota = data["city"]
			print(f"proxy aktif\nkota : {kota}\nip   : {ip}\n")
			pro.append(isi)
		except Exception as e:
			try:
				data = self.ses.get("https://ipinfo.io/json",proxies=proxy, timeout=0.5).json()
				ip = data["ip"]
				kota = data["city"]
				print(f"proxy aktif\nkota : {kota}\nip   : {ip}\n")
				pro.append(isi)
			except:pass
	
	# proxydbnet / socks4 indonesia
	def dump1(self):
		try:
			head = {"Host": "proxydb.net", "Connection": "keep-alive", "Upgrade-Insecure-Requests": "1", "User-Agent": "Mozilla/5.0 (Linux; Android 10; Redmi 8A Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "Referer": "http://proxydb.net/?protocol=socks4&country=ID", "Accept-Encoding": "gzip, deflate", "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
			link = parser(self.ses.get("http://proxydb.net/?protocol=socks4&country=ID",headers=head).text, "html.parser")
			for x in link.find_all("a",href=True):
				if " " in str(x.text):pass
				else: self.main(x.text)
		except Exception as e:pass
	
	# hidemy.name / socks4 indonesia
	def dump2(self):
		try:
			link = parser(self.ses.get("https://hidemy.name/en/proxy-list/?country=ID&maxtime=1000&type=4#list",headers={"user-agent": "Mozilla/5.0 (Mobile; rv:48.0; A405DL) Gecko/48.0 Firefox/48.0 KAIOS/2.5"}).text, "html.parser")
			for x in re.findall("<tr><td>(.*?)</td><td>(.*?)</td><td>",str(link)):
				if 'IP' in str(x):pass
				else: self.main(x[0]+':'+x[1])
		except Exception as e:pass
	
	# proxyscrape / socks4 indonesia		
	def dump3(self):
		try:
			y = self.ses.get("https://api.proxyscrape.com/?request=displayproxies&protocol=socks4&timeout=1000&country=id&ssl=all&anonymity=all").text
			for x in y.splitlines(): self.main(x)
		except Exception as e:pass
	
	# proxydocker / socks4 indonesia		
	def dump4(self):
		try:
			token = re.search('name="_token" content= "(.*?)"',str(self.ses.get("https://www.proxydocker.com").text)).group(1)
			date = {"token": token, "country": "Indonesia", "city": "all", "state": "all", "port": "all", "type": "socks4", "anonymity": "all", "need": "all", "page": "1"}
			bz = self.ses.post("https://www.proxydocker.com/id/api/proxylist/",data=date).text
			for ip, hs in re.findall('"ip":"(.*?)","port":(\d+),',str(bz)):
				self.main(ip+":"+hs)
		except Exception as e:pass
	
	# free-proxy / socks4 indonesia
	def convert(b):
		return base64.b64decode(b).decode('utf-8')
	
	def dump5(self):
		try:
			link = parser(self.ses.get("http://free-proxy.cz/en/proxylist/country/ID/socks4/ping/all",headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win32; x86) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36"},
			cookies={"cookie":"__gads=ID=a46154120acc2b0f-2214b83dafd60084:T=1663949799:RT=1663949799:S=ALNI_MY6ZCKPnb75CGnvnnDTsNOd_afMTQ; fp=9cc77da02135fe1d597bb5e5d77197aa; __utmc=104525399; __gpi=UID=000009d951d88e7d:T=1663949799:RT=1664085736:S=ALNI_Ma3Zc894Q3Mue-joehr-DCyKGn-hg; __utmz=104525399.1664089425.5.5.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __utma=104525399.1797804672.1663949798.1664089425.1664093143.6; __utmt=1; __utmb=104525399.8.10.1664093143"}).text, "html.parser")
			for x in link.find_all("tr"):
				try:
					ip = convert(str(x).split('Base64.decode("')[1].split('"))</script>')[0])
					hs = re.findall('style="">(\d+)</',str(x))[0]
					self.main(ip+":"+hs)
				except:pass
		except Exception as s: pass
	
	def dump6(self):
		try:
			x = self.ses.get("https://www.proxy-list.download/api/v2/get?l=en&t=socks4").json()["LISTA"]
			for c in re.findall("'IP': '(.*?)', 'PORT': '(\d+)', 'ANON': '(.*?)', 'COUNTRY': '(.*?)',",str(x)):
				if "indonesia" in str(c[3].lower()): self.main(c[0]+":"+c[1])
				else:pass
		except Exception as e: pass
	

Proxx()	
os.system("clear")
input(pro)




