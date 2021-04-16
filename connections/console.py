#!/usr/bin/python3
import cmd
from logs.environment import get_cookie
import requests
import re
import os
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
    cookie = get_cookie()  # Cooke for the session.
    web = "https://intranet.hbtn.io/"  # Intranet URL.
    current = 0  # This varable will be used when you select a project.
    html = ""  # html of the project when do_use activated.
    dir_name = ""  # Name of the project for the directory.

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
        self.dic_projects = {"217": "https://intranet.hbtn.io/projects/217"}
        for project in self.project_list:
            tokens = project.split("\"")
            self.dic_projects[tokens[0][1:]] = self.web + \
                "projects" + tokens[0]

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
        self.dir_name = re.search(
            r"<li>Directory: <code>.*</code></li>", self.html.text)
        self.dir_name = self.dir_name.group(0)[21:-12]
        print(self.dir_name)

    def do_create_files(self, line):
        """Create all the mains, all the needed files with prototypes, README
        and more... """

        if (self.current == 0):
            print("You need to set a project first, syntax: use <id>")
            return

        # Create the directory if not exists
        if not os.path.exists(self.dir_name):
            os.makedirs(self.dir_name)

        # Search for the project type.
        project_type = re.search(
            r"Foundations - Low-level programming|Foundations - Higher-level programming ― Python", self.html.text)
        project_type = project_type.group(0)

        if "Low-level programming" in project_type:
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
                        replace("\\\\", "\\").\
                        replace("&#39;", "\'").\
                        replace("&amp;", "&")
                    file_content = file_content + '\n'
                    token_text = file_content.split("\n")
                    tokenized_bracket = '\n'.join(
                        token_text[1:]).split("julien@ubuntu")[0:-1]
                    file_content = '\n'.join(tokenized_bracket[:])

                    with open(self.dir_name + "/" + element[4:], mode="w+") as f:
                        f.write(file_content)
                else:
                    pass
                # Until here are the main files.

                # Create a README with the project title
                with open(self.dir_name + "/" + "README.md", mode="w+") as f:
                    f.write("# {}\n".format(self.dir_name))
                    # Until here is the README

                # From here, will create the header FILE for C projects
                header_name = re.search(r"[a-z]*\.h[^A-Za-z]", self.html.text)
                header_name = header_name.group(0)[:-1]
                header_content = re.findall(r"Prototype: .*", self.html.text)
                prototypes = []

                for prototype in header_content:
                    header_tokenize = prototype.split(">")
                    prototypes.append(header_tokenize[1].split("<")[0] + "\n")

                with open(self.dir_name + "/" + header_name, mode="w+") as f:
                    f.write("#ifndef " + header_name.upper() + "\n" +
                            "#define " + header_name.upper() + "\n\n" +
                            "".join(prototypes) + "\n" +
                            "#endif /* " + header_name.upper() + " */\n"
                            )
                # Until here the header is created with all prototypes.

                # From here search for the no-mains files and assign them the prototype
                files_no_mains = re.findall(r"<li>File: <code>.*</code></li>",
                                            self.html.text)
                tokenized_files = [elm[16:-12] for elm in files_no_mains]

                for file_num in range(len(tokenized_files) - 1):
                    with open(self.dir_name + "/" + tokenized_files[file_num], mode='w+') as f:
                        f.write("#include \"" + header_name + "\"\n\n"
                                + "/**\n *\n *\n *\n *\n */\n\n" + prototypes[file_num] +
                                "{\n\n}\n")
                # Until here are the tasks files (not mains).
        # if the project is a python project:
#        if "Higher-level programming" in project_type:

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
