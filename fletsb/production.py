from .storyboard import StoryBoard
from .engines.canvas import Canvas
import flet, json, os




class Production:
    """This is the production engine. Its responsible of loading the fletsb application for production."""
    def __init__(self, file_path:str) -> None:
        self.file_path = file_path

        # Init data
        self.current_page_name = "main"
        self.storyboard_content = self.load_file()
        self.storyboard_controls = []

        # Experiance
        self.storyboard_class = StoryBoard(
            main_class=self,
            development_mode=False
        )
        self.preview_canvas = Canvas(main_class=self)

        # Update all
        self.preview_canvas.update_canvas()
        self.preview_canvas.update_page_properties()
    
    # Utils
    def change_canvas_page (self, page_name:str):
        if page_name in self.storyboard_content['pages']:
            self.current_page_name = page_name
            self.preview_canvas.update_canvas()
            self.preview_canvas.update_page_properties()
        else:
            print(f"Warning: There is no page with name '{page_name}'")
    
    # Production Essentials
    def load_file (self) -> dict:
        if not os.path.isfile(self.file_path):
            raise Exception("There is no such fletsb file in the specified path")
        
        try:
            return json.loads(open(self.file_path, encoding="utf-8").read())
        except:
            raise Exception("The file at the specified path is broken or can't read it as a fletsb file.")

    @property
    def view (self):
        return self.preview_canvas.view