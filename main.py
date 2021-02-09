from bs4 import BeautifulSoup
from getpass import getpass
import requests
import urllib

print("Please enter your username: ", end='')
user = input()
password = getpass()
print("You entered a password!")

""" We need then to login and save the cookie in a file
If the file with cookie content doesn't exist, ask for credentials
If credentials sucessful, then we need to get the cookie
"""

cookie = {"_holberton_intranet_session": "COOKIE_HERE"}
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
