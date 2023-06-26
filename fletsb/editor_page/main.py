from .appbar import AppBar
from .preview import Preview
from ..tools.manage_keyboard_commands import keyboard_commands
import flet
import os, time, json


class MainPage:
    """Main page of the editor"""
    def __init__(self, file_path:str) -> None:
        if not os.path.isfile(file_path):
            raise FileExistsError(f"There is no Flet StoryBoard on path '{file_path}' .")
        

        # UI props
        self.follow_page_bounds = [] # List of flet controls that will follow the page width and height.

        # save props
        self.current_page_name = "main"
        self.file_path = file_path
        self.dict_content = json.loads(open(file_path, encoding="utf-8").read())

        # storyboard template data
        self.storyboard_template = {}

        flet.app(target=self.UI)
        
    
    def UI (self, page:flet.Page):
        self.page = page
        # set page props
        page.on_keyboard_event = self.keyboard_commands_manager
        page.on_resize = self.on_page_resize
        page.vertical_alignment = flet.MainAxisAlignment.CENTER
        page.title = f"Flet_StoryBoard | {self.file_path}"
        page.bgcolor = "black"

        # main stack of the page.
        self.main_stack = flet.Stack()
        page.add(self.main_stack) 

        # main view
        self.main_view = flet.Column()
        self.push_on_stack(self.main_view)

        # row of mainview
        self.row_of_mainview = flet.Row(alignment=flet.MainAxisAlignment.CENTER)
        self.main_view.controls.append(self.row_of_mainview)

        # custom page's appbar.
        self.appbar = AppBar(main_class=self)
        self.main_view.controls.append(flet.Row([self.appbar.main_bar], alignment="center"))

        # add the preview place manager
        self.preview = Preview(main_class=self)

        # update page as if it was resized
        self.on_page_resize()
        self.page.update()
        self.page.window_center()
    

    def on_page_resize (self, e=None):
        self.main_stack.width = self.page.width
        self.main_stack.height = self.page.height

        self.appbar.main_bar.width = self.page.width - 25
        self.appbar.refresh()

        for con in self.follow_page_bounds: con.width = self.page.width; con.height = self.page.height

        self.page.update()


    def keyboard_commands_manager (self, e):
        keyboard_commands(event=e)


    def save_all (self, e=None):
        pass

    def push_on_stack (self, container:flet.Container, with_bg_cover:bool=False):
        def remove ():
            self.main_stack.controls.remove(animated_control)
            if with_bg_cover:
                self.main_stack.controls.remove(cover)
                self.follow_page_bounds.remove(cover)
            
            self.main_stack.update()
        
        animated_control = flet.AnimatedSwitcher(
            content=flet.Text(""),
            transition=flet.AnimatedSwitcherTransition.FADE,
            duration=300,
            reverse_duration=100,
            switch_in_curve=flet.AnimationCurve.BOUNCE_IN_OUT,
            switch_out_curve=flet.AnimationCurve.BOUNCE_IN_OUT
        )
        if with_bg_cover:
            cover = flet.Container(
                bgcolor="black", 
                width=self.page.width, 
                height=self.page.height,
                opacity=0.8
            )
            self.main_stack.controls.append(cover)
            self.follow_page_bounds.append(cover)
        self.main_stack.controls.append(animated_control)
        self.main_stack.update()

        time.sleep(0.1)

        animated_control.content = container
        animated_control.update()

        return remove