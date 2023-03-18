from flet import *
import flet
import os
import json

# local import
from .createStoryBoard import CreateStoryBoard
from .ui_set.pick_control_section import pickControlSection
from .Engines.preview_engine import previewEngine
from .Engines.edit_control_engine import editControlEngine
from .pages.settings import Settings

class EditStoryBoard:
    """
    This will make you edit the an exist storyboard or create a new one if not exist.
    """
    def __init__ (self, file_path:str, external_functions:list=[]):
        if str(file_path).endswith(".fletsb"): pass
        else: file_path = file_path + ".fletsb"

        #? Check if the file exist.
        if os.path.isfile(file_path) == True:
            pass
        else:
            CreateStoryBoard()
            if os.path.isfile(file_path) == False: return
        
        #? Get storyboard info
        self.storyboard_name = file_path
        self.external_functions = external_functions
        self.file_as_dict = json.loads(open(f"{file_path}", encoding="utf-8").read())
        self.page_settings = self.file_as_dict["page_settings"]

        #? show the window
        self.__run_window()
    
    def __run_window(self):
        def main (page:Page):
            def on_resize (me):
                pick_control_section.width = page.width / 4 - 30
                pick_control_section.height = page.height
                preview_page_section.width = page.width - float(float(page.width/4)*2)
                preview_page_section.height = page.height
                edit_controls_section.width = page.width / 4 - 20
                edit_controls_section.height = page.height

                page.update()
                

            # page.window_full_screen = True
            self.page = page
            page.on_keyboard_event = self.keyboard_commands_manager
            page.on_resize = on_resize
            page.spacing = 0
            page.window_width = 850; page.window_height = 700; 
            page.window_min_height = 700
            page.window_min_width = 850
            page.bgcolor = "black"
            page.window_center()
            page.vertical_alignment = flet.MainAxisAlignment.CENTER
            page.appbar = flet.AppBar(
                bgcolor="black",
                leading=Row([
                    Text("  "),
                    Icon("DASHBOARD_CUSTOMIZE_ROUNDED", color="white"),
                    Text("Flet storyBoard", color="white")
                ]),
                actions=[
                    flet.TextButton(content=flet.Text("settings", color="white", size=12), on_click=self.settings_sheet),
                    flet.Text("  "),
                    flet.Container(content=flet.Row([flet.Text("Save storyboard", size=14, color="black")], alignment="center"), 
                    on_click=self.save_file, bgcolor="white", border_radius=10, width=150, height=30, tooltip="You can also click 'command + s'"),
                    flet.Text("    ")
                ]
            )
            page_row = flet.Row(expand=True, alignment="left")
            page.add(page_row)

            pick_control_section = flet.Column(scroll=True)
            pick_control_section.width = page.width / 4
            pick_control_section.height = page.height
            self.pick_control_section = pick_control_section
            page_row.controls.append(Container(content=pick_control_section, border_radius=10))

            preview_page_section = flet.Column(alignment="center", auto_scroll=True)
            preview_page_section.width = page.width - float(float(page.width/4)*2)
            preview_page_section.height = page.height
            self.preview_page_section = preview_page_section
            con_preview_page_section = Container(content=preview_page_section, border=flet.border.all(0.15, "white"), border_radius=10)
            page_row.controls.append(con_preview_page_section)

            edit_controls_section = flet.Column(scroll=True)
            edit_controls_section.width = page.width / 4
            edit_controls_section.height = page.height
            self.edit_controls_section = edit_controls_section
            page_row.controls.append(Container(content=edit_controls_section, border_radius=10))


            # generate the sections
            pickControlSection(pick_control_section, self.on_start_edit_control) # for the controls picker section.
            self.prev_engine = previewEngine(self, preview_page_section, development=True, bgview=con_preview_page_section)


            page.update()
        flet.app(target=main)
    
    def save_file (self, *args):
        open(f"{self.storyboard_name}", "w+", encoding="utf-8").write(json.dumps(self.file_as_dict))
        self.page.snack_bar = flet.SnackBar(
        content=flet.Text(""),
        action="",
        )
        page = self.page
        page.snack_bar = flet.SnackBar(flet.Text(f"StoryBoard '{self.storyboard_name}' edits is saved!"))
        page.snack_bar.open = True
        self.prev_engine.update()
        page.update()

    
    def on_start_edit_control (self, type, is_new, number_on_list):
        editControlEngine(self, self.edit_controls_section, is_new, type, number_on_list)
        self.page.update()
    

    def keyboard_commands_manager (self, event):
        if event.key == "S" and event.ctrl == True: self.save_file()
        if event.key == "S" and event.meta == True: self.save_file()
    

    def settings_sheet (self, *args):
        page : flet.Page = self.page
        v = Settings(self)
        page.dialog = flet.AlertDialog(
            content=v
        )

        page.dialog.open = True
        page.update()