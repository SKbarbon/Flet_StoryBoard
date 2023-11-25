import flet




class SettingsForum (flet.Column):
    def __init__ (self, storyboard_class, settings_section_name:str):
        self.storyboard_class = storyboard_class
        self.settings_section_name = settings_section_name

        self.refresh_forum()

    def refresh_forum(self):
        self.controls.clear()

        pass