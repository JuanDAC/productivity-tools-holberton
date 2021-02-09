from bs4 import BeautifulSoup
from getpass import getpass
import requests
import urllib
from os import path, makedirs

if path.exists("/home/ubuntu/.hbtn_utils/cookie.txt") is False:
    print("Please enter your username: ", end='')
    user = input()
    password = getpass()
    makedirs("/home/ubuntu/.hbtn_utils", exist_ok=True)
    """ WE NEED TO DO THE REQUEST TO LOGIN """
    with open("/home/ubuntu/.hbtn_utils/cookie.txt", "w") as user_cookie:
        user_cookie.write("Here should be the cookie")

with open('/home/ubuntu/.hbtn_utils/cookie.txt', 'r') as user_cookie:
    print(user_cookie.read())
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
