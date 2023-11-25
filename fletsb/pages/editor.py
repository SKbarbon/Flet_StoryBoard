from fletsb.uikit.banner_alert import error_banner_alert
from fletsb import engines
from fletsb import StoryBoard
from fletsb.uikit import Scene
from fletsb import pages
from fletsb import uikit
import flet, json, threading, traceback


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
                editor_class=self,
                on_click_floating_btn=self.on_add_new_widget_to_page,
                on_ask_ai=self.ask_ai_to_add
            ),
            support_top_bar_controlers=False
        )

        # data
        self.current_page_name = "main"
        self.storyboard_content = json.loads(open(project_path, encoding="utf-8").read())
        self.storyboard_class = StoryBoard(main_class=self)
        self.storyboard_controls = []

        self.storyboard_changes_history = []

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

        # Update pages browser, the one that show all users storyboard pages
        self.buttom_bar.update_pages_browser()

    
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
        if message.lower() == "fullscreen":
            self.page.window_full_screen = True
            self.page.update()
        else:
            self.ai_engine.request_to_add(message=message)
    

    def change_right_section_content (self, content:flet.Control):
        self.right_section.content = content
        if self.right_section.page != None:
            self.right_section.update()
    

    def open_tab_on_sheet (self, tab_name:str):
        def close_sheet(e=None): self.application_class.show_the_sheet = False
        if tab_name == "Settings":
            tb = pages.Settings(close_function=close_sheet).view
            # self.application_class.sheet_is_fullscreen = True
        else:
            tb = flet.Text(tab_name)
        
        self.application_class.sheet_container.content = tb
        self.application_class.show_the_sheet = True
    

    def on_create_new_page (self):
        self.page.dialog = flet.AlertDialog(
            content=flet.Column([
                flet.Text("Create new page", size=23, weight="bold"),
                flet.TextField(hint_text="Page name"),
                flet.TextButton("Create")
            ], alignment=flet.MainAxisAlignment.CENTER, horizontal_alignment=flet.CrossAxisAlignment.CENTER,
                height=200),
            open=True
        )

        self.page.update()

    def change_canvas_page(self, page_name:str):
        """Change the page that you are editing."""
        if page_name in self.storyboard_content['pages']:
            self.current_page_name = page_name

            self.editor_canvas_engine.update_canvas()
            # Update pages browser, the one that show all users storyboard pages
            self.buttom_bar.update_pages_browser()


    def on_keyboard_event (self, e:flet.KeyboardEvent):
        if e.key == "," and e.meta:
            self.open_tab_on_sheet("Settings")
    

    def save_storyboard_content(self):
        """Save the current content by overwrite it on top the old file."""
        # print("Save..")

        try:
            open(self.project_path, "w+", encoding="utf-8").write(json.dumps(self.storyboard_content, indent=4))
        except:
            traceback.print_exc()
            self.page.banner = error_banner_alert(
                title="Cannot save changes 😕",
                text="There was an error while trying to save changes. Please share this error with us\ncontaining the project file and the step you did."
            )
            self.page.banner.open = True
            self.page.overlay.clear()
            warning_audio_src = "https://cdn.pixabay.com/download/audio/2022/11/20/audio_3371f818f5.mp3?filename=error-2-126514.mp3"
            self.page.overlay.append(flet.Audio(warning_audio_src, autoplay=True, volume=0.5))
            self.page.update()



    def _back_to_last_change_in_history(self):
        """Go back to the previous change on the storyboard history."""
        #! NOT WORKING
        if len(self.storyboard_changes_history) > 1:
            self.storyboard_changes_history.remove(self.storyboard_changes_history[-1])
            self.storyboard_content = self.storyboard_changes_history[-1]  # Get the previous state


            self.editor_canvas_engine.update_canvas()
            self.save_storyboard_content()
            print("Undo")