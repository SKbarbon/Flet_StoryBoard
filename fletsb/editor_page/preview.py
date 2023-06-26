import flet



class Preview:
    def __init__(self, main_class) -> None:
        # settings of preview
        self.preview_mode = "full" #? full, iPad-portrait-, iPad-landscape-, iPhoneX-portrait- and iPhoneX-landscape-.
        # generate
        self.container = flet.Container(border=flet.border.all(0.2, color=flet.colors.WHITE))

        self.page : flet.Page = main_class.page
        self.main_view : flet.Column = main_class.main_view
    

    def reset_container (self):
        if self.preview_mode == "full":
            pass