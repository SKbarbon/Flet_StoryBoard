import sys
import os

from .editStoryBoard import EditStoryBoard

file_args = sys.argv

if len(file_args) == 1:
    EditStoryBoard("")
elif len(file_args) > 1:
    file_path = file_args[1]
    if str(file_path).endswith(".fletsb") == False:
        file_path = file_path + ".fletsb"
    if os.path.isfile(file_path) == False:
        print(f"There is no storyboard file with name '{file_path}', so it will be created a new one.")
    EditStoryBoard(file_path)