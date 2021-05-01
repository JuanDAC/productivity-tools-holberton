#!/usr/bin/python3
from os import path, makedirs, environ
from logs.env import WORKING_DIRECTORY, COOKIE
from ast import literal_eval


def exist_directory():
<<<<<<< HEAD
    return(path.exists(WORKING_DIRECTORY))


def create_directory():
    try:
        makedirs(WORKING_DIRECTORY, exist_ok=True)
    except OSError:
        print ("Creation of the directory %s failed" % WORKING_DIRECTORY)
        return(False)
    else:
        return(True)

=======
	print("Directory is %s " % WORKING_DIRECTORY)
	print(path.exists(WORKING_DIRECTORY))
	return(path.exists(WORKING_DIRECTORY))

def create_directory():
	try:
		print("Creating direction")
		makedirs(WORKING_DIRECTORY, exist_ok=True)
	except OSError:
		print("Creation of the directory %s failed" % WORKING_DIRECTORY)
		return(False);
	else:
		return(True)
>>>>>>> 5a8bc466965b9554f57d7810c6162969184a7d14

def exist_cookie():
    return(path.isfile(COOKIE))


def create_cookie(hbtn_cookie):
<<<<<<< HEAD
    with open(COOKIE, "w") as file:
        file.write(str(hbtn_cookie))

=======
	with open(COOKIE, "w") as file:
		file.write(str(hbtn_cookie))
def get_cookie():
	with open(COOKIE, 'r') as user_cookie:
		return(literal_eval(user_cookie.read()))
>>>>>>> 5a8bc466965b9554f57d7810c6162969184a7d14

def get_cookie():
    with open(COOKIE, 'r') as user_cookie:
        return(literal_eval(user_cookie.read()))
