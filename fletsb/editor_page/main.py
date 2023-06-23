from .appbar import AppBar
import flet
import os, time


class MainPage:
    """Main page of the editor"""
    def __init__(self, file_path:str) -> None:
        if not os.path.isfile(file_path):
            raise FileExistsError(f"There is no Flet StoryBoard on path '{file_path}' .")
        
        # save props
        self.file_path = file_path

        flet.app(target=self.UI)
        
    
    def UI (self, page:flet.Page):
        self.page = page
        page.window_width = 450
        # set page props
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

        # custom page's appbar.
        self.appbar = AppBar(main_class=self)
        self.main_view.controls.append(flet.Row([self.appbar.main_bar], alignment="center"))

        self.main_view.controls.append(flet.Text("gr", color="white"))

        # update page as if it was resized
        self.on_page_resize()
        self.page.update()
        self.page.window_center()
    

    def on_page_resize (self, e=None):
        self.main_stack.width = self.page.width
        self.main_stack.height = self.page.height

        self.appbar.main_bar.width = self.page.width - 25
        self.appbar.refresh()

        self.page.update()


    def save_all (self, e=None):
        pass


    def push_on_stack (self, container:flet.Container):
        def remove ():
            animated_control.content = flet.Text("")
            animated_control.update()
            time.sleep(0.5)
            self.main_stack.controls.remove(animated_control)
            self.main_stack.update()
        
        animated_control = flet.AnimatedSwitcher(
            content=flet.Text(""),
            transition=flet.AnimatedSwitcherTransition.FADE,
            duration=300,
            reverse_duration=100,
            switch_in_curve=flet.AnimationCurve.BOUNCE_IN_OUT,
            switch_out_curve=flet.AnimationCurve.BOUNCE_IN_OUT
        )
        self.main_stack.controls.append(animated_control)
        self.main_stack.update()

        time.sleep(0.1)

        animated_control.content = container
        animated_control.update()

        return remove