from fletsb import uikit
from fletsb import utils
import flet, time

from fletsb.pages import Editor


class Application:
    def __init__(self, storyboard_file:str=None) -> None:

        # Experience data
        self.user_on_edit_state = False # Apply when a project is opened for being edited.

        # start flet app cycle.
        flet.app(target=self.app)

    def app (self, page:flet.Page):
        self.page : flet.Page = page
        # Page properties
        page.theme_mode = flet.ThemeMode.DARK
        page.padding = 0
        page.spacing = 0
        page.bgcolor = flet.colors.TRANSPARENT

        # Page events
        page.on_resize = self.on_page_resize
        page.on_keyboard_event = self.on_keyboard_shortcut

        # Page main stack controls
        self.main_stack = flet.Stack(expand=True)
        page.add(self.main_stack)

        # Page background customisation
        bg_container = flet.Container(
            bgcolor="#151515"
        )
        self.main_stack.controls.append(bg_container)


        # Holders
        self.main_scene_holder = flet.AnimatedSwitcher(
            content=flet.Text(""),
            duration=1,
            switch_in_curve=flet.AnimationCurve.BOUNCE_IN
        )
        self.main_stack.controls.append(self.main_scene_holder)

        self.sheet_container = flet.Container(
            bgcolor="white",
            border_radius=18,
            visible=False
        )
        self.main_stack.controls.append(flet.Column([
            flet.Row([self.sheet_container], alignment=flet.MainAxisAlignment.CENTER)
        ], alignment=flet.MainAxisAlignment.CENTER))


        # Set specific page appearance for desktop
        if utils.is_phone_platform() == False and page.web == False:
            page.window_frameless = True
            page.window_min_height = 550
            page.window_min_width = 700
            bg_container.border_radius = 18
            bg_container.opacity = 0.9

        
        page.update()
        page.window_center()

        # testing scene
        e = Editor("Proj Name", page=self.page, application_class=self)
        self.editor_scene = e
        self.show_a_scene(scene=e)

        self.page.update()
        e.testing_content()
    

    def show_a_scene (self, scene):
        safe_area = flet.SafeArea(content=scene)

        self.main_scene_holder.content = safe_area
        self.main_scene_holder.update()
    

    def on_page_resize (self, e):
        # print(e.__dict__)
        if self.page.width > 450:
            #! if big screen size
            self.sheet_container.width = self.page.width / 1.5
        else:
            self.sheet_container.width = self.page.width - 50
        
        self.sheet_container.height = self.page.height - 150

        if hasattr(self, 'editor_scene') and self.user_on_edit_state:
            self.editor_scene.editor_canvas_engine.main_col.width = self.page.width / 1.5
            self.editor_scene.editor_canvas_engine.main_col.height = self.page.height - 150
            self.editor_scene.right_section.width = self.page.width - (self.page.width / 1.5) - 50
            self.editor_scene.right_section.height = self.editor_scene.editor_canvas_engine.main_col.height
        
        self.page.update()

    def on_keyboard_shortcut (self, e):
        if str(e.key).lower() == "escape":
            if self.sheet_container.visible == True: self.show_the_sheet = False
    

    @property
    def show_the_sheet (self): return self.sheet_container.visible

    @show_the_sheet.setter
    def show_the_sheet(self, value:bool):
        if value == True:
            self.sheet_container.visible = True
            self.main_scene_holder.opacity = 0.5
            self.main_scene_holder.disabled = True
        else:
            self.sheet_container.visible = False
            self.main_scene_holder.opacity = 1.0
            self.main_scene_holder.disabled = False
        
        self.main_scene_holder.update()
        self.sheet_container.update()