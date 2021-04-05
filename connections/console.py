#!/usr/bin/python3
import cmd
from logs.environment import get_cookie
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
    html = ""

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
        self.dic_projects = {"217":"https://intranet.hbtn.io/projects/217"}
        for project in self.project_list:
            tokens = project.split("\"")
            self.dic_projects[tokens[0][1:]] = self.web + "projects" + tokens[0]

    def do_get_projects(self, line):
        """ Show projects running at the moment """
        print("\n".join(self.project_list).
              replace("\"", " | ").
              replace("<", "").
              replace(">", "").
              replace("/", ""))

    def do_use(self, line):
        """Set a project to work with. Syntax: use <id>"""
        if line not in self.dic_projects:
            print("This ID doesn't correspond of a running project")
            return
        self.current = line
        self.html = self.connection.get(self.dic_projects[self.current])

    def do_create_files(self, line):
        """Create all the mains, all the needed files with prototypes, README
        and more... """
        if (self.current == 0):
            print("You need to set a project first, syntax: use <id>")
            return
        # From here search for the no-mains files
        files_no_mains = re.findall(r"<li>File: <code>.*</code></li>", self.html.text)
        tokenized_files = [elm[16:-12] for elm in files_no_mains]
        for files in tokenized_files:
            open(files, 'a').close()
        # Until here are the tasks files (not mains).
        # From here, search for the main files
        main_count = re.findall(r"cat \d*-main.c", self.html.text)
        for element in main_count:
            main_n = element[4:].split("-")
            if int(main_n[0]) <= 50:
                main_regex = re.findall(r"{}.*gcc.* {}".
                                        format(element, element[4:]),
                                        self.html.text,
                                        flags=re.DOTALL)
                file_content = str(main_regex)
                file_content = file_content.replace("&quot;", "\"").\
                               replace("&lt;", "<").\
                               replace("&gt;", ">").\
                               replace("\\\\n", "--.n").\
                               replace("\\n", "\n").\
                               replace("--.n", "\\n").\
                               replace("\\\\", "\\")
                file_content = file_content + '\n'
                token_text = file_content.split("\n")
                tokenized_bracket = '\n'.join(token_text[1:]).split("}")
                file_content = '\n'.join(tokenized_bracket[:-1]) + '}\n'
                f = open(element[4:], "w")
                f.write(file_content)
                f.close()
            else:
                pass
        # Until here are the main files.

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


console_loop = Console()
console_loop.cmdloop()
del (console_loop.connection)
