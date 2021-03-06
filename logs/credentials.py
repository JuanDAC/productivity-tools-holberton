from bs4 import BeautifulSoup
from getpass import getpass
import requests
import urllib

def login():
    user = input("Please enter your username: ")
    password = getpass()
    with requests.Session() as log:
        payload = {
            "user[login]": user,
            "user[password]": password,
            "commit": "Log in"
        }
        r = log.get("https://intranet.hbtn.io/auth/sign_in")
        soup = BeautifulSoup(r.content, 'html5lib')
        payload['authenticity_token'] = soup.find(
            'input', attrs={'name': 'authenticity_token'})['value']
        pos = log.post("https://intranet.hbtn.io/auth/sign_in", data=payload)

        if "Invalid Email or password." in pos.text:
            print("Your credentials are wrong. Please try again.")
            login()
        return(pos.cookies.get_dict())
