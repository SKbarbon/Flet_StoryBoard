from fletsb.uikit.banner_alert import error_banner_alert
from fletsb import engines
from fletsb import StoryBoard
from fletsb.uikit import Scene
from fletsb import pages
from fletsb import uikit
from fletsb import tools
import flet, json, traceback

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
                    flet.Container(content=flet.Row([flet.Icon(
                        name=flet.icons.REMOVE_RED_EYE_ROUNDED,
                        color="white",
                        size=15
                    )], alignment=flet.MainAxisAlignment.CENTER), bgcolor="#3b93f5", border_radius=10, width=30, height=30, 
                        on_click=lambda e: self.open_tab_on_sheet(tab_name="Preview"), tooltip="Full Window Preview"),
                    flet.TextButton(content=flet.Container(
                        content=flet.Row([
                            flet.Text("Exit", color="black", weight=flet.FontWeight.W_300)
                        ], alignment=flet.MainAxisAlignment.CENTER),
                        bgcolor="white",
                        border_radius=13,
                        width=120, height=35
                    ), tooltip="Exit the project", on_click=self.exit_project)
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
        self.storyboard_class = StoryBoard(main_class=self, development_mode=True)
        self.storyboard_controls = []

        self.storyboard_changes_history = []

        # UI
        self.preview_canvas = engines.Canvas(main_class=self)

        self.editor_canvas_engine = engines.EditorCanvas(main_class=self)
        self.right_section_placeholder = flet.Row([
            flet.Text(
                "Select a widget\nto edit", 
                color="#a3a3a3", 
                size=14, 
                text_align=flet.TextAlign.CENTER,
                weight=flet.FontWeight.W_300
            )
        ], alignment=flet.MainAxisAlignment.CENTER)
        self.right_section = flet.Container(
            bgcolor=flet.colors.BLACK,
            border_radius=18,
            content=self.right_section_placeholder
        )

        self.ai_engine = engines.AiSuggestions(storyboard_class=self.storyboard_class)


        self.add_new_controls([flet.Row([
            self.editor_canvas_engine.view,
            self.right_section
        ], alignment=flet.MainAxisAlignment.CENTER)])

        self.editor_canvas_engine.update_canvas()

        # Update pages browser, the one that show all users storyboard pages
        self.buttom_bar.update_pages_browser()

        # Start the AI suggestion loop engine
        engines.LoopAiPageSuggestion(editor_class=self)

    
    def start_edit_widget (self, widget_id):
        self.right_section.content = engines.EditingWidget(
            storyboard_class=self.storyboard_class,
            widget_id=widget_id
        )
        self.right_section.update()


    def exit_project (self, e):
        self.application_class.user_on_edit_state = False
        # self.page.window_close()
    

    def on_add_new_widget_to_page(self):
        add_new_widget_engine = engines.AddNewWidget(editor_class=self, add_to="page")
        self.right_section.content = add_new_widget_engine
        self.right_section.update()
    

    def ask_ai_to_add (self, message:str):
        if message.lower() == "fullscreen":
            self.page.window_full_screen = True
            self.page.update()
        else:
            try:
                self.ai_engine.request_to_add(message=message)
            except:
                traceback.print_exc()
                self.application_class.push_error_banner(
                    title="Cannot talk to AI 🤖❌!",
                    text="There was an issue while talking to AI. Please check your internet connection then try again."
                )
    

    def change_right_section_content (self, content:flet.Control):
        self.right_section.content = content
        if self.right_section.page != None:
            self.right_section.update()
    

    def open_tab_on_sheet (self, tab_name:str):
        def close_sheet(e=None): self.application_class.show_the_sheet = False
        if tab_name == "Settings":
            tb = pages.Settings(close_function=close_sheet, editor_class=self).view
        
        elif tab_name == "Preview":
            tb = self.preview_canvas.view
            self.application_class.sheet_is_fullscreen = True
            self.preview_canvas.update_canvas()
            self.preview_canvas.update_page_properties()
        
        elif tab_name == "Community":
            tb = pages.CommunityPage(close_function=close_sheet)
        else:
            tb = flet.Text(tab_name)
        
        self.application_class.sheet_container.content = tb
        self.application_class.show_the_sheet = True

        if tab_name == "Settings": tb.back_btn.focus()
    

    def on_create_new_page (self):
        def on_done_name (e):
            if str(page_name_field.value) == "main": return
            if str(page_name_field.value).replace(" ", "") == "": return
            main_page_settings = self.storyboard_content['pages']['main']['settings']
            self.storyboard_content['pages'][page_name_field.value] = {"settings": main_page_settings, "widgets": []}
            self.buttom_bar.update_pages_browser()

            self.page.dialog.open = False
            self.page.dialog.update()
            self.current_page_name = page_name_field.value
            self.save_storyboard_content()
            self.editor_canvas_engine.update_canvas()
            self.buttom_bar.update_pages_browser()

            self.application_class.push_notifications(
                icon="CREATE_SHARP",
                icon_color="#ADD8E6",
                title=f"Page '{page_name_field.value}' is created 😇!"
            )

        page_name_field = flet.TextField(hint_text="Page name", on_submit=on_done_name)
        self.page.dialog = flet.AlertDialog(
            content=flet.Column([
                flet.Text("Create new page", size=23, weight="bold"),
                page_name_field
            ], alignment=flet.MainAxisAlignment.CENTER, horizontal_alignment=flet.CrossAxisAlignment.CENTER,
                height=100),
            open=True,
            actions=[flet.TextButton("Create", on_click=on_done_name)]
        )

        self.page.update()
        page_name_field.focus()
    


    def to_rename_a_page (self, page_name:str):
        def rename (new_name:str):
            self.storyboard_content['pages'][new_name] = self.storyboard_content['pages'][page_name]
            del self.storyboard_content['pages'][page_name]
            self.page.dialog.open = False; self.page.update()
            self.current_page_name = new_name
            self.save_storyboard_content()
            self.editor_canvas_engine.update_canvas()
            self.buttom_bar.update_pages_browser()

            self.application_class.push_notifications(
                icon="DRIVE_FILE_RENAME_OUTLINE_OUTLINED",
                icon_color="#65a765",
                title=f"Page '{page_name}' renamed to '{new_name}' ✨!"
            )

        def delete ():
            del self.storyboard_content['pages'][page_name]
            self.page.dialog.open = False; self.page.update()

            self.current_page_name = "main"
            self.save_storyboard_content()
            self.editor_canvas_engine.update_canvas()
            self.buttom_bar.update_pages_browser()

            self.application_class.push_notifications(
                icon="DELETE_ROUNDED",
                icon_color="#ff8080",
                title=f"Page '{page_name}' is deleted successfully 😇!"
            )

            self.right_section.content = self.right_section_placeholder
            self.right_section.update()
        # ------
        col = flet.Column(
                alignment=flet.MainAxisAlignment.CENTER,
                height=200, width=250,
                horizontal_alignment=flet.CrossAxisAlignment.CENTER
            )
        if page_name in self.storyboard_content['pages'] and page_name != "main":
            col.controls.append(flet.Text(f"Edit '{page_name}'", size=23, weight="bold"))
            col.controls.append(flet.Row([
                flet.TextField(label="Rename", value=page_name, on_submit=lambda e: rename(new_name=e.control.value),
                                width=200, tooltip="Click Enter after you type the new page name")
                ], alignment=flet.MainAxisAlignment.CENTER))
            col.controls.append(flet.Row([flet.TextButton(content=flet.Text("delete", color="red"), on_click=lambda e: delete())], alignment=flet.MainAxisAlignment.CENTER))
        else:
            col.controls.append(flet.Text(f"You cannot edit a page named '{page_name}' 🙂!"))
        
        self.page.dialog = flet.AlertDialog(content=col, open=True)
        self.page.update()


    def change_canvas_page(self, page_name:str):
        """Change the page that you are editing."""
        if page_name in self.storyboard_content['pages']:
            self.current_page_name = page_name

            self.preview_canvas.update_canvas()
            self.preview_canvas.update_page_properties()

            self.editor_canvas_engine.update_canvas()
            self.editor_canvas_engine.update_page_properties()
            # Update pages browser, the one that show all users storyboard pages
            self.buttom_bar.update_pages_browser()
            
            self.right_section.content = self.right_section_placeholder
            self.update()


    def on_keyboard_event (self, e:flet.KeyboardEvent):
        if e.key == "," and e.meta:
            self.open_tab_on_sheet("Settings")
        elif str(e.key).lower() == "escape":
            self.change_canvas_page(page_name=self.current_page_name)
    

    def save_storyboard_content(self):
        """Save the current content by overwrite it on top the old file."""
        # print("Save..")

        # Remove the widgets that must be removed
        for cc in self.storyboard_content['pages'][self.current_page_name]['widgets']:
            if cc['delete_me']:
                self.storyboard_content['pages'][self.current_page_name]['widgets'].remove(cc)


        try:
            open(self.project_path, "w+", encoding="utf-8").write(json.dumps(self.storyboard_content, indent=4))
        except:
            traceback.print_exc()
            self.application_class.push_error_banner(
                title="Cannot save changes 😕!",
                text="There was an error while trying to save changes. Please share this error with us\ncontaining the project file and the step you did."
            )



    def _back_to_last_change_in_history(self):
        """Go back to the previous change on the storyboard history."""
        #! NOT WORKING
        if len(self.storyboard_changes_history) > 1:
            self.storyboard_changes_history.remove(self.storyboard_changes_history[-1])
            self.storyboard_content = self.storyboard_changes_history[-1]  # Get the previous state


            self.editor_canvas_engine.update_canvas()
            self.save_storyboard_content()
            print("Undo")