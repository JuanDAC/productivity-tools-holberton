from bs4 import BeautifulSoup
import requests
import urllib

cookie = {"_holberton_intranet_session": "COOKIE_HERE"}
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
