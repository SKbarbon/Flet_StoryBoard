from .engines.viewer_engine import viewerEngine
from .tools.storyboard_class import StoryBoard
from .widgets.All import all_widgets
import json
import flet


class LoadStoryBoard:
    def __init__(self, target_function, storyboard_file_path: str):
        # set up the important props
        self.current_page_name = "main"
        self.file_path = storyboard_file_path
        self.development_mode = False
        self.all_widgets = all_widgets
        self.dict_content = json.loads(open(self.file_path, encoding="utf-8").read())
        self.target_function = target_function

        # copy of things
        self.viewerEngine = viewerEngine
        # Run the app.
        flet.app(target=self.run)

    def run(self, page: flet.Page):
        self.storyboard_class = StoryBoard(page=page, main_class=self)
        page.vertical_alignment = page.vertical_alignment = flet.MainAxisAlignment.CENTER
        self.page = page
        ve = viewerEngine(self, self.dict_content, self.current_page_name, page, page, self.development_mode)
        self.target_function(self.storyboard_class)
        page.update()

    def setup_storyboard_class(self):
        pass
