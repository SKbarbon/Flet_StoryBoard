from fletsb.tools.create_new_storyboard_file import CreateStoryBoardFile
import os

p = "DemoProj.fletsb"

if not os.path.isfile(p):
    CreateStoryBoardFile(file_path=p)

from fletsb.application import Application


Application(storyboard_file_path=p)