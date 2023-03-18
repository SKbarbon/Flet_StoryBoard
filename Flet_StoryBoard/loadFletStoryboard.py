from .Engines.preview_engine import previewEngine




class load_flet_storyboard:
    """
    This will run a window of a storyboard.
    """
    def __init__(self, storyboard_path, functions={}) -> None:
        self.functions = functions
        if str(storyboard_path).endswith(".fletsb"):
            self.storyboard_path = storyboard_path
        else:
            self.storyboard_path = storyboard_path + ".fletsb"

    def run (self):
        previewEngine("", None, development=False, file_path=self.storyboard_path, functions=self.functions)