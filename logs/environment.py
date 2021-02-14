from os import path, makedirs, environ
from env import WORKING_DIRECTORY, COOKIE;
from ast import literal_eval

def exist_directory():
	return(path.exists(WORKING_DIRECTORY))

def create_directory()
	try:
		makedirs(WORKING_DIRECTORY, exist_ok=True)
	except OSError:
		print ("Creation of the directory %s failed" % WORKING_DIRECTORY)
		return(False);
	else:
		return(True)

def exist_cookie():
	return(path.isfile(COOKIE))

def create_cookie(hbtn_cookie):
	with open(COOKIE, "w") as file:
		file.write(str(hbtn_cookie))

# TODO add literal eval
def get_cookie():
	with open(COOKIE, 'r') as user_cookie:
		return(literal_eval(ser_cookie.read()))
