#!/usr/bin/python3
import cmd
from logs.environment import get_cookie
from bs4 import BeautifulSoup
import requests
import re
""" Interactive console to get projects, review, files, and more. """

if __name__ == "__main__":
    print("Use main.py instead of console.py")
    exit()


class Console(cmd.Cmd):
    """
    Interactive console
    prompt = Console prompt waiting for input

    =====================================================
    |     In case to add or edit a help description     |
    |  Modify the comment below function of instruction |
    =====================================================

    """
    prompt = "Console-> "
    cookie = get_cookie()
    web = "https://intranet.hbtn.io/"
    current = 0 # This varable will be used when you select a project

    def __init__(self):
        """ Stablish the connection to persistent """
        cmd.Cmd.__init__(self)
        self.connection = requests.Session()
        """
        The next request is because self.connection save the session, so
        we don't need to specify the cookie again in all this file.
        This gets the current projects and save them in project_list-
        """
        print("This could take a bit... (Some seconds)")
        html = self.connection.get(
            "https://intranet.hbtn.io/dashboards/my_current_projects",
            cookies=self.cookie)
        projects_block_html = re.findall(
            r"<ul class=\"list-group gap\">.*<span class=\"bpi-status\">",
            html.text, flags=re.DOTALL)
        self.project_list = re.findall(r"/[0-9]{1,3}\".*<",
                                  "\n".join(projects_block_html))
        self.dic_projects = {}
        for project in self.project_list:
            tokens = project.split("\"")
            self.dic_projects[tokens[0][1:]] = self.web + "projects" + tokens[0]

    def emptyline(self):
        """ User enters an empty line >> pass """
        pass

    def do_EOF(self, line):
        """ User send EOF (End of file | CTRL + D) >> exit """
        print()
        return True

    def do_quit(self, line):
        """ User types quit >> exit """
        return True

    def do_get_projects(self, line):
        """ Show projects running at the moment """
        print("\n".join(self.project_list).
              replace("\"", " | ").
              replace("<", "").
              replace(">", "").
              replace("/", ""))

    # def do_use(self, line):
    #     """ User must use a project in order to get all the files """


console_loop = Console()
console_loop.cmdloop()
del (console_loop.connection)
