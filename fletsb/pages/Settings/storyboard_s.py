import flet



class StoryBoardSection:
    """Its the section of edit the storyboard settings"""
    def __init__(self, settings_page_class) -> None:
        self.settings_page_class = settings_page_class
        self.view = flet.Column([flet.Text("StoryBoard section", color=flet.colors.WHITE)])