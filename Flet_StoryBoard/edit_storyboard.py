from flet import *
import flet
import json
import os

from .create_storyboard import create_flet_storyboard
from .pages.controls_widgets_page import Widgets_Page
from .pages.page_preview import Page_Preview_Page
from .pages.edit_controls_page import Edit_Controls_Page
from .ui_tools.built_in_widgets import BuiltIn_Widgets
from .pages.settings_page import push_settings

class edit_flet_storyboard:
    """
    Edit an exist storyboard using an easy ui.
    * if the storyboard file not exist, it will be created a new one.
    """
    def __init__(self, storyboard_file_name, functions={}, external_widgets=None, create_new_storyboard_if_not_exist=True):
        if str(storyboard_file_name).endswith(".fletsb"): pass
        else: storyboard_file_name = storyboard_file_name + ".fletsb"

        if os.path.isfile(storyboard_file_name) == False:
            if create_new_storyboard_if_not_exist:
                create_flet_storyboard(storyboard_file_name)
            else:
                raise OSError(f"there is not storyboard with name {storyboard_file_name}")
        
        self.storyboard_file_name = storyboard_file_name
        self.functions = functions
        self.built_in_widgets = BuiltIn_Widgets
        self.external_widgets = external_widgets

        self.storyboard_json = json.loads(open(storyboard_file_name, encoding="utf-8").read())
        self.preview_frame = None
        self.__edit_widget_page = None

        self.__show_the_gui()
    def __show_the_gui(self):
        def EDITOR_GUI(page:flet.Page):
            def on_keyboard_shortcut(me):
                if str(me.key) == "A" and me.meta or str(me.key) == "A" and me.ctrl:
                    pass
                elif str(me.key) == "S" and me.meta or str(me.key) == "S" and me.ctrl:
                    self.__save_file()
            
            def on_resize(me):
                page_pages_manager.width = page.width; page_pages_manager.height = page.height - 80
                widgets_page.width = page.width/5; widgets_page.height = page.height
                preview_page.width = page.width-float(page.width/5+page.width/4); preview_page.height = page.height
                edit_widget_page.width = page.width/4-40; edit_widget_page.height = page.height
                page_pages_manager.update()
            
            def show_settings(me):
                push_settings(page, self)
            
            #! UI START.
            self.page = page
            page.bgcolor = "white"
            page.on_keyboard_event = on_keyboard_shortcut
            page.window_min_width = 1090; page.window_width = 1090;
            page.window_min_height = 730; page.window_height = 730;
            page.window_center()
            page.on_resize = on_resize
            page.appbar = AppBar(
                bgcolor="white",
                leading=Row([
                    Text("    "),
                    Icon("DASHBOARD_CUSTOMIZE_ROUNDED", color="black"),
                    Text("Flet storyboard", color="black")
                ]),
                actions=[
                    TextButton(content=Text("settings", color="black", size=12), on_click=show_settings, tooltip="show settings sheet"),
                    Text("  "),
                    ElevatedButton(content=Text("save", size=12), bgcolor="black", color="white", width=70, on_click=self.__save_file,
                    tooltip="save the storyboard changes"),
                    Text("  ")
                ]
            )

            page_pages_manager = Row(width=page.width, height=page.height)
            widgets_page = Column(width=page.width/5, height=page.height, scroll=True)
            preview_page = Column(width=page.width-float(page.width/5+page.width/4-40), height=page.height, scroll=True, 
            horizontal_alignment=flet.CrossAxisAlignment.END, alignment=flet.MainAxisAlignment.CENTER)
            self.preview_page = preview_page
            edit_widget_page = Column(width=page.width/4-40, height=page.height, scroll=True)
            self.__edit_widget_page = edit_widget_page
            self.ewp = edit_widget_page

            page_pages_manager.controls.append(Container(widgets_page, bgcolor=page.bgcolor))
            page_pages_manager.controls.append(Container(preview_page, bgcolor="#EEEEEE"))
            page_pages_manager.controls.append(Container(edit_widget_page, bgcolor=page.bgcolor))

            #! generate pages index
            Widgets_Page(widgets_page, self.built_in_widgets, self.external_widgets, Edit_Controls_Page, self)
            Page_Preview_Page(self, preview_page)


            page.add(page_pages_manager)
            page.update()
        flet.app(target=EDITOR_GUI)
    
    def __save_file(self, *args):
        open(self.storyboard_file_name, "w+", encoding="utf-8").write(json.dumps(self.storyboard_json))
        self.page.snack_bar = flet.SnackBar(flet.Text("Saved!"))
        self.page.snack_bar.open = True
        self.page.update()
    
    def update_preview(self):
        self.preview_frame.clean()
        Page_Preview_Page(self, self.preview_frame)
    
    def __on_close(self):
        pass