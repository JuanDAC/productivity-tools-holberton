from os import path, makedirs, environ
from logs.credentials import login
from logs.environment import *


def main():
    if exist_directory():
        create_directory()
    if exist_cookie():
        from connections.console import Console
    else:
        create_cookie(login())


if __name__ == '__main__':
    main()
