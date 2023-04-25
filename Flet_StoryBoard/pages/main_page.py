#! This is the editing page of a storyboard.
from flet import Page, Row, Text
from ..WIDGETS.All import all_widgets
import flet
import os
import json
import time
import requests


#* local imports
from ..sections.left_section import leftSection
from ..sections.preview_section import previewSection
from ..sections.edit_section import editSection
from ..Engines.edit_widget_engine import editWidgetsEngine
from ..Engines.edit_subwidgets_engin import editSubWidgetsEngine
from ..Engines.suggesting_engine import SuggestingEngine
from ..WIDGETS.All import all_widgets
from ..pages.settings import SettingsPage


class mainPage:
    def __init__(self, file_path):
        if not os.path.isfile(file_path):
            raise FileExistsError(f"There is no Flet StoryBoard on path '{file_path}' .")
        

        self.current_page_name = "main"
        self.file_path = file_path
        self.development_mode = True
        self.dict_content = json.loads(open(file_path, encoding="utf-8").read())

        #? Copy of classes
        self.all_widgets = all_widgets
        self._editWidgetsEngine = editWidgetsEngine
        self._editSubWidgetsEngine = editSubWidgetsEngine

        #? Run the app
        flet.app(target=self.app)

    def app (self, page:Page):
        page.title = f"Flet StoryBoard - {self.file_path}"
        page.spacing = 0
        page.bgcolor = "black"
        page.vertical_alignment = flet.MainAxisAlignment.CENTER
        page.window_width = 850
        page.window_height = 650
        page.window_min_width = 850
        page.window_min_height = 640
        self.page = page
        page.appbar = self.generate_app_bar()
        page.window_center()
        page.update()

        # The main row
        self.main_row = Row(scroll=False)
        page.add(self.main_row)

        #? append the sections
        self.left_section = leftSection(page, self, self.main_row)
        self.preview_section = previewSection(page, self, self.main_row)
        self.edit_section = editSection(page, self, self.main_row)

        #? Set finals of page.
        page.on_resize = self.on_page_resize
        page.on_keyboard_event = self.manage_keyboard_commands


        #? Setup the storyboard suggestions engine.
        self.suggesting_engine = SuggestingEngine(self)
        time.sleep(0.5)
        self.suggesting_engine.push_new_suggestion()

    def on_page_resize (self, *event):
        page = self.page
        self.left_section.main_container.width = self.page.width / 4 - 30
        self.left_section.main_container.height = self.page.height - 70
        self.preview_section.main_view.width = page.width-(page.width/4)*2
        self.preview_section.main_view.height = page.height-150
        self.edit_section.main_column.width = self.page.width / 4 - 10
        self.edit_section.main_column.height = page.height - 70

        self.page.update()
    
    def pages_browser (self):
        def create_a_page (e):
            self.create_new_page(str(e.control.value))
            self.page.appbar = self.generate_app_bar()
            self.page.update()
        def open_a_page (e):
            page_name = str(e.control.content.controls[0].value)
            if page_name in self.dict_content["pages"]:
                self.current_page_name = page_name
            self.preview_section.update_preview(self.current_page_name)
            self.last_checked_page_button.bgcolor = flet.colors.GREY_700
            self.last_checked_page_button = e.control
            e.control.bgcolor = "blue"
            time.sleep(0.3)
            self.suggesting_engine.push_new_suggestion()
            self.page.update()
        def ask_for_new_page_name (e):
            mr.scroll = False
            tf = flet.TextField(label="Page name", on_submit=create_a_page, height=40, color="white")
            mr.controls = [tf]
            mr.update()
            tf.focus()
        mr = flet.Row([], width=250, scroll=True)
        mr.controls.append(flet.TextButton(content=flet.Text("✨", size=18), on_click=self.edit_page_suggestion_state, width=35))
        new_page_button = flet.Container(flet.Row([flet.Text("+ Page", size=12, color="black")], alignment="center"), on_click=ask_for_new_page_name, 
        bgcolor="white", width=60, height=30, border_radius=12)
        mr.controls.append(new_page_button)

        for p in self.dict_content["pages"]:
            c = flet.Container(flet.Row([
                flet.Text(p, color="white", size=12)
            ], alignment="center"), bgcolor=flet.colors.GREY_700, width=60, height=30, border_radius=12, on_click=open_a_page)
            mr.controls.append(c)
            if str(p) == str(self.current_page_name):
                c.bgcolor = "blue"
                self.last_checked_page_button = c

        return mr
    
    def generate_app_bar (self):
        a = flet.AppBar(
            bgcolor=self.page.bgcolor,
            leading=flet.Row([
                Text("    "),
                flet.Icon(flet.icons.DASHBOARD_ROUNDED, size=18, color="white"),
                Text("Flet StoryBoard", color="white", weight="bold", size=15)
            ], spacing=15
            ),
            actions=[
                Row([
                    flet.TextButton(content=flet.Text("Settings", size=12, color="white"), 
                    on_click=self.open_settings_page),
                    flet.ElevatedButton("Save", bgcolor="white", color="black", width=100, height=35, 
                    on_click=self.save_all, tooltip="click to save | also control + S"),
                    Text("    ")
                ], alignment=15)
            ],
            title=self.pages_browser(),
            center_title=True
        )

        return a
    

    def manage_keyboard_commands (self, event):
        key = event.key # It would be a key like: 'A' or 'Enter'.
        shift = event.shift # It would be a bool value of where the shift key is clicked or not.
        ctrl = event.ctrl # It would be a bool value of where the control key is clicked or not.
        alt = event.alt # It would be a bool value of where the option key is clicked or not.
        meta = event.meta # It would be a bool value of where the command key is clicked or not.

        if str(key).lower() == "s" and ctrl:
            #? Clicked to save file
            self.save_all()
        elif str(key).lower() == "s" and meta:
            #? Clicked to save file
            self.save_all()
    

    def save_all (self, *args):
        new_content = json.dumps(self.dict_content)
        file = open(self.file_path, "w+", encoding="utf-8")
        file.write(new_content)

        page = self.page
        page.snack_bar = flet.SnackBar(
            content=flet.Text(f"This Flet StoryBoard '{self.file_path}' is saved!"),
            action="Alright!"
        )
        page.snack_bar.open = True
        page.update()
    

    def add_new_widget (self, widget_name, page_name=None):
        widget_number = len(self.dict_content["pages"][self.current_page_name]["widgets"])-1
        widget_class = all_widgets[widget_name]["class"]
        widget_class = widget_class(self, self.preview_section.main_view_collumn, widget_number=widget_number)
        
        self.dict_content["pages"][self.current_page_name]["widgets"].append(widget_class.template)
        
        self.preview_section.update_preview(self.current_page_name)
        self.page.update()

        self.edit_a_widget(len(self.dict_content["pages"][self.current_page_name]["widgets"])-1)
        
        time.sleep(0.5)
        self.suggesting_engine.push_new_suggestion()

        return widget_class
    
    def edit_a_widget (self, widget_number_on_content):
        self.edit_section.edit_widget_using_engine(widget_number_on_content)
        self.page.update()
    

    def create_new_page (self, page_name):
        page_dict = {
            "settings" : {
                "bgcolor" : "black",
                "suggestions_rules" : "none"
            },
                "widgets" : [
                            
            ]
        }
        self.dict_content["pages"][page_name] = page_dict
        self.current_page_name = str(page_name)
        self.page.appbar = self.generate_app_bar()
        self.preview_section.update_preview(self.current_page_name)
    

    def edit_page_suggestion_state (self, *a):
        def go_back (e):
            self.left_section.show_new_content(last_content)
            self.page.update()
        
        def apply_and_start (name_of_sug):
            self.dict_content["pages"][self.current_page_name]["settings"]["suggestions_rules"] = str(name_of_sug)
            go_back("")
            self.suggesting_engine.push_new_suggestion()

        def make_a_rule_button_option (name):
            def on_choose (e):
                apply_and_start(name)
            b = flet.ElevatedButton(f"{name}", on_click=on_choose, bgcolor="white", color="blacK", width=150, height=45)
            return flet.Row([b], alignment="center")

        last_content = self.left_section.main_container
        c = flet.Column(width=last_content.width, height=last_content.height)

        back_btn = flet.TextButton("< Back", on_click=go_back)
        c.controls.append(back_btn)

        title = flet.Text("Chose the suggestion rules for this page.", color="white", size=17, weight="bold")
        c.controls.append(title)

        all_rules = requests.get("https://raw.githubusercontent.com/SKbarbon/Flet_StoryBoard/main/rules/all.json").text
        all_rules = json.loads(all_rules)
        
        for rule_option in all_rules["all_rules"]:
            c.controls.append(make_a_rule_button_option(rule_option))

        c.controls.append(flet.Row([flet.Text("more will come soon", color="white", size=13)], alignment="center"))
        c.scroll = True
        self.left_section.show_new_content(c)
    
    def open_settings_page (self, *e):
        SettingsPage(self.page, self)