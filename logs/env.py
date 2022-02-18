from os import path, makedirs, environ

WORKING_DIRECTORY = path.join(
    environ.get('HOMEPATH') or environ.get('HOME'),
    ".hbtn_utils"
)
COOKIE = path.join(WORKING_DIRECTORY, 'cookie')
