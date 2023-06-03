import requests
import re
import bs4 as bs

def isFlag(url):
        rgx = re.compile(r'(([a-z]|[0-9])+)')
        match = rgx.match(requests.get(url).text)
        if match and match.group(1):
                print("~~~FLAG~~~")
                print("Path: %s" % url)
                return match.group(1)
        return None

def scrapper(url):
	getRes = requests.get(url)
	page = bs.BeautifulSoup(getRes.text, 'html.parser')
	if (page is not None):
		links = page.find_all("a")
		for link in links:
			readme = link.get('href')
			if (readme == "README"):
				getRes = requests.get(url + readme)
				if (isFlag(url + readme)):
					print(getRes.text)
					quit()
			elif (readme != "../"):
				scrapper(url + readme)

scrapper("http://[VM_IP]/.hidden/") # Change to yor VM IP address
