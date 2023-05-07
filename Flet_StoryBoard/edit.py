from .pages.create_new_file import CreateNewFile
from .pages.main_page import mainPage
import sys
import os
import flet

cmd_args = sys.argv
debug_mode = False
if "--debug" in cmd_args:
    debug_mode = True


class manage_edit:
    def __init__(self) -> None:
        self.cmd_args = sys.argv
        self.file_name = None
        flet.app(target=self.CNF)

        if self.file_name is None and debug_mode:
            print("Debug alert: Unexpected exit, no errors.")
            sys.exit("Exit.")
            return
        
        if self.file_name is None:
            sys.exit("Exit.")
            return

        if not str(self.file_name).endswith(".fletsb"):
            self.file_name = str(self.file_name) + ".fletsb"

        if debug_mode:
            print("Debug alert: About to run the editor.")

        mainPage(self.file_name)

    def CNF(self, page):
        CreateNewFile(page, manage_class=self)


if len(cmd_args) == 1:
    # To create a new file.
    if debug_mode:
        print("Debug alert: About to show the 'CreateNewFile' window.")
    manage_edit()
else:
    # To edit an existing File.
    full_path = ""
    for i in range(1, len(cmd_args)):
        if full_path == "":
            full_path = full_path + cmd_args[i]
        else:
            full_path = full_path + " " + cmd_args[i]

    full_path = full_path.replace(" --debug", "")
    full_path = full_path.replace("--debug", "")

    if os.path.isfile(full_path):
        if debug_mode:
            print("Debug alert: About to run the editor.")
        mainPage(full_path)
    else:
        print(f"Warning: File not found '{full_path}', so create a new one.")
        if debug_mode:
            print("Debug alert: About to show the 'CreateNewFile' window.")
        manage_edit()
