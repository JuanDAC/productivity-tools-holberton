from bs4 import BeautifulSoup
import requests
import urllib

cookie = {"_holberton_intranet_session": "Njk2MHlXWDFZVDlaK3pxcFBvYXd5MHgxUUN4YmJzbUNGVGNkd2pTTmdTYlk0cEpmN1lRbnM5eTNHelVvSzYxRzRTN1hRaE5rcDFMbjFUSmVrbjVJSDZKeXA1cWlTWDd4Q04wZHAxMWVkMEZncmIreStUc0laR1czWC9PMjVpN2xXYUtXeUJ2ZDRYdDlIWHRIa2Y4L01STEdrajlsdUh0STZrMDl1TThWdDU2MElPMDRNNW9QYTlVclA5SlBDelc3RlF5TlBBU1UySTZOemJjM2NYNVRxUT09LS1ydUZ1WlVhcWtwdENxeE9xWFVkTUNBPT0%3D--5cd4cb5cbd102e1957e7f64bec7d034e7775367d"}
url = "https://intranet.hbtn.io/projects/228"

print("\nWorking...\n")

sexsion = requests.session()
requests.utils.add_dict_to_cookiejar(sexsion.cookies, cookie)
tmp = sexsion.get(url, cookies=cookie)
content = tmp.content
web = BeautifulSoup(content, 'html.parser')
hml = web.find_all("a", {"data-confirm": True})
if hml:
    opt = sexsion.get(url + '/unlock_optionals', cookies=cookie)
print(hml)
del sexsion
