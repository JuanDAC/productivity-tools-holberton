from bs4 import BeautifulSoup
from getpass import getpass
import requests
import urllib
from os import path, makedirs, environ
from ast import literal_eval


Home = environ['HOME'] + '/.hbtn_utils/cookie.txt'
pat = Home[:-11]
if path.exists(pat) is False:
    print("Please enter your username: ", end='')
    user = input()
    password = getpass()
    makedirs(pat, exist_ok=True)
    with requests.Session() as log:
        payload={
            "user[login]": user,
            "user[password]": password,
            "commit": "Log in"
        }
        r = log.get("https://intranet.hbtn.io/auth
        soup = BeautifulSoup(r.content, 'html5lib'
        payload['authenticity_token'] = soup.find(nticity_token'})['value']
        pos = log.post("https://intranet.hbtn.io/a

        if "Invalid Email or password." in pos.tex
            print("Your credentials are wrong. Ple
            exit() # Or do a loop.
        hbtn_cookie=pos.cookies.get_dict()
        with open(Home, "w") as file:
            file.write(str(hbtn_cookie))

with open(Home, 'r') as user_cookie:
    cookie=user_cookie.read()
cookie = literal_eval(cookie)

# WE HAVE IT UNTIL HERE

url = "https://intranet.hbtn.io/projects/228"

print("\nWorking...\n")

sexsion = requests.session()
requests.utils.add_dict_to_cookiejar(sexsion.cooki
tmp = sexsion.get(url, cookies=cookie)
content = tmp.content
web = BeautifulSoup(content, 'html.parser')

# Search for data-confirm
hml = web.find_all("a", {"data-confirm": True})
if hml:
    opt = sexsion.get(url + '/unlock_optionals', c
print(hml)

del sexsion
