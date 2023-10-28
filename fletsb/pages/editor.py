from fletsb import engines
from fletsb import StoryBoard
from fletsb.uikit import Scene
from fletsb import pages
from fletsb import uikit
import flet, json, threading


class Editor (Scene):
    def __init__(self, project_name:str, project_path:str, page:flet.Page, application_class):
        self.project_path = project_path
        self.application_class = application_class
        self.application_class.user_on_edit_state = True
        super().__init__(
            page=page,
            topbar=uikit.SceneTopbar(
                title=f"{project_name}",
                actions=[
                    flet.TextButton(
                        content=flet.Text("Community", color="white"), 
                        tooltip="Open Community page",
                        on_click=lambda e: self.open_tab_on_sheet("Community")
                    ),
                    flet.TextButton(
                        content=flet.Text("Settings", color="white"), 
                        tooltip="Open Settings page",
                        on_click=lambda e: self.open_tab_on_sheet("Settings")
                    ),
                    flet.TextButton(content=flet.Container(
                        content=flet.Row([
                            flet.Text("Exit", color="black", weight=flet.FontWeight.W_300)
                        ], alignment=flet.MainAxisAlignment.CENTER),
                        bgcolor="white",
                        border_radius=13,
                        width=120, height=35
                    ), tooltip="Exit the project")
                ]
            ),
            controls=[],
            button_bar=uikit.SceneButtonbarEditor(
                on_click_floating_btn=self.on_add_new_widget_to_page,
                on_ask_ai=self.ask_ai_to_add
            )
        )

        # data
        self.current_page_name = "main"
        self.storyboard_content = json.loads(open(project_path, encoding="utf-8").read())
        self.storyboard_class = StoryBoard(main_class=self)
        self.storyboard_controls = []

        # UI
        self.editor_canvas_engine = engines.EditorCanvas(main_class=self)
        self.right_section = flet.Container(
            bgcolor=flet.colors.BLACK,
            border_radius=18,
            content=flet.Row([
                flet.Text(
                    "Select a widget\nto edit", 
                    color="#a3a3a3", 
                    size=14, 
                    text_align=flet.TextAlign.CENTER,
                    weight=flet.FontWeight.W_300
                )
            ], alignment=flet.MainAxisAlignment.CENTER)
        )

        self.ai_engine = engines.AiSuggestions(storyboard_class=self.storyboard_class)


        self.add_new_controls([flet.Row([
            self.editor_canvas_engine.view,
            self.right_section
        ], alignment=flet.MainAxisAlignment.CENTER)])

        self.editor_canvas_engine.update_canvas()
    
    def start_edit_widget (self, widget_id):
        self.right_section.content = engines.EditingWidget(
            storyboard_class=self.storyboard_class,
            widget_id=widget_id
        )
        self.right_section.update()


    def exit_project (self, e):
        self.application_class.self.user_on_edit_state = False
    

    def on_add_new_widget_to_page(self):
        add_new_widget_engine = engines.AddNewWidget(editor_class=self, add_to="page")
        self.right_section.content = add_new_widget_engine
        self.right_section.update()
    

    def ask_ai_to_add (self, message:str):
        self.ai_engine.request_to_add(message=message)
    

    def change_right_section_content (self, content:flet.Control):
        self.right_section.content = content
        if self.right_section.page != None:
            self.right_section.update()
    

    def open_tab_on_sheet (self, tab_name:str):
        def close_sheet(e=None): self.application_class.show_the_sheet = False
        if tab_name == "Settings":
            tb = pages.Settings(close_function=close_sheet).view
        else:
            tb = flet.Text(tab_name)
        self.application_class.sheet_container.content = tb
        self.application_class.show_the_sheet = True
    

    def save_storyboard_content(self):
        """Save the current content by overwrite it on top the old file."""
        # print("Save..")
        open(self.project_path, "w+", encoding="utf-8").write(json.dumps(self.storyboard_content, indent=4))