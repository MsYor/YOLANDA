import httpx

http_proxies = [
	"https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all",
	"https://www.proxy-list.download/api/v1/get?type=http&anon=elite",
	"https://www.proxy-list.download/api/v1/get?type=http&anon=anonymous"
]

file_name = "proxy.txt"
with open(file_name, 'w'):
	for proxies in http_proxies:
		if httpx.get(proxies).status_code == 200:
			print(f"[{httpx.get(proxies).status_code}] GET => {proxies}")
			with open(file_name, 'a') as p:
				p.write(httpx.get(proxies).text)
		else:
			print(f"[{httpx.get(proxies).status_code}] ERROR => {proxies}")
	with open(file_name, 'r') as count:
		print(f"[+] Total {file_name.replace('.txt', '')} Proxies: {len(count.readlines())}")
