from .pages.create_new_file import CreateNewFile
from .pages.main_page import mainPage
import sys
import os
import flet


cmd_args = sys.argv


class manage_edit:
    def __init__(self) -> None:
        self.cmd_args = sys.argv
        self.file_name = None
        flet.app(target=self.CNF)
        if self.file_name == None: sys.exit("Exit.")
        if not str(self.file_name).endswith(".fletsb"):
            self.file_name = str(self.file_name) + ".fletsb"
        mainPage(self.file_name)
    
    def CNF (self, page):
        CreateNewFile(page, manage_class=self)


if len(cmd_args) == 1:
    #? To create a new file.
    manage_edit()
else:
    #? To edit a exist File.
    full_path = ""
    for i in range(1, len(cmd_args)):
        if full_path == "":
            full_path = full_path + cmd_args[i]
        else:
            full_path = full_path + " " + cmd_args[i]
    
    if os.path.isfile(full_path):
        mainPage(full_path)
    else:
        print(f"Warning: File not found '{full_path}', so create a new one.")
        manage_edit()