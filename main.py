from bs4 import BeautifulSoup
from getpass import getpass
import requests
import urllib
from os import path, makedirs, environ


Home = environ['HOME'] + '/.hbtn_utils/cookie.txt'
pat = Home[:-11]
if path.exists(pat) is False:
    print("Please enter your username: ", end='')
    user = input()
    password = getpass()
    with requests.Session() as log:
        payload={
            "user[login]": user,
            "user[password]": password,
            "commit": "Log in"
        }
        r = log.get("https://intranet.hbtn.io/auth/sign_in")
        soup = BeautifulSoup(r.content, 'html5lib')
        payload['authenticity_token'] = soup.find('input', attrs={'name': 'authenticity_token'})['value']
        pos = log.post("https://intranet.hbtn.io/auth/sign_in", data=payload)

        if "Invalid Email or password." in pos.text:
            print("Your credentials are wrong. Please try again.")
            exit() # Or do a loop.
        hbtn_cookie=pos.cookies.get_dict()
        makedirs(pat, exist_ok=True)
        with open(Home, "w") as file:
            file.write(str(hbtn_cookie))

with open(Home, 'r') as user_cookie:
    cookie=user_cookie.read()
print(cookie)
exit()

"""
We need then to login and save the cookie in a file
If the file with cookie content doesn't exist, ask for credentials
If credentials sucessful, then we need to get the cookie
"""

cookie = {"_holberton_intranet_session": user_cookie}
url = "https://intranet.hbtn.io/projects/228"

print("\nWorking...\n")

sexsion = requests.session()
requests.utils.add_dict_to_cookiejar(sexsion.cookies, cookie)
tmp = sexsion.get(url, cookies=cookie)
content = tmp.content
web = BeautifulSoup(content, 'html.parser')

# Search for data-confirm
hml = web.find_all("a", {"data-confirm": True})
if hml:
    opt = sexsion.get(url + '/unlock_optionals', cookies=cookie)
print(hml)

del sexsion
