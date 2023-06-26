from .pages.create_new_file import CreateNewFile
from .editor_page.main import MainPage
import sys
import os
import flet

cmd_args = sys.argv
# To edit an existing File.
full_path = ""
for i in range(1, len(cmd_args)):
    if full_path == "":
        full_path = full_path + cmd_args[i]
    else:
        full_path = full_path + " " + cmd_args[i]


class FileManager:
    def __init__(self) -> None:
        self.file_name = None
        if not os.path.isfile(full_path):
            # if file not exists
            print(f"Cannot find a file on {full_path}, so create a new one.")
            flet.app(target=self.file_creation_page)
            if self.file_name is None:
                sys.exit("Exit.")
            
            self.file_name = str(self.file_name) + ".fletsb"
            MainPage(file_path=self.file_name)
        else:
            # if file is exist
            MainPage(file_path=full_path)
    
    def file_creation_page (self, page:flet.Page):
        CreateNewFile(page=page, manage_class=self)


if __name__ == "__main__":
    FileManager()