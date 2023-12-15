from fletsb.uikit.paragraph_with_translate_ability import ParagraphWithTranslateAbility
import flet, traceback, time, threading


class SceneButtonbarEditor (flet.Row):
    """A topbar that being used on a scene object."""
    def __init__ (self, editor_class, on_accept_suggestion=None, on_ask_ai=None, on_click_floating_btn=None):
        super().__init__()
        self.editor_class = editor_class
        self.controls.append(flet.Text("    ", height=15))

        self.ai_suggestion_field = flet.TextField(
            hint_text="Ask AI to add..",
            border="none",
            text_size=15,
            on_submit=lambda e: self.process_action(e, on_ask_ai, e.control.value),
            text_style=flet.TextStyle(weight=flet.FontWeight.W_300),
            tooltip="Run a quick command, or ask AI to add a thing to the canvas."
        )

        self.content_of_ai_icon = flet.IconButton(
            icon="CHAT_BUBBLE_OUTLINE_ROUNDED", 
            icon_color="white",
            on_click=lambda e: self.process_action(e, on_accept_suggestion),
            width=50,
            height=50
        )
        ai_chat_row = flet.Row([
            flet.AnimatedSwitcher(
                content=self.content_of_ai_icon,
                duration=250,
                transition=flet.AnimatedSwitcherTransition.FADE
            ),
            self.ai_suggestion_field,
        ])
        self.ai_chat_row = ai_chat_row
        self.controls.append(ai_chat_row)

        self.controls.append(flet.Text("", expand=True))


        # Multiple Pages Manager
        self.pages_browser_row = flet.Row([
            flet.TextButton("+ Page", tooltip="Create new page", on_click=lambda e: self.editor_class.on_create_new_page(), data="+page")
        ], scroll=flet.ScrollMode.HIDDEN, width=300)
        self.controls.append(self.pages_browser_row)

        self.controls.append(flet.Text("    ", height=15))
        # Floatin btn
        self.floating_btn = flet.Container(content=flet.Row([
            flet.Text("+", size=15, color="white", weight=flet.FontWeight.BOLD)
        ], alignment=flet.MainAxisAlignment.CENTER),
            bgcolor="#3b93f5",
            border_radius=15,
            width=45,
            height=45,
            on_click=lambda e: self.process_action(e, on_click_floating_btn)
        )
        self.controls.append(self.floating_btn)

        self.controls.append(flet.Text("    ", height=15))
    

    def process_action (self, e, action, data=None):
        if action == None: return
        ctrl : flet.Control = e.control

        ctrl.disabled = True
        ctrl.update()
        try:
            if data != None:
                action(data)
            else:
                action()
        except:
            traceback.print_exc()
        ctrl.disabled = False
        if isinstance(ctrl, flet.TextField):
            ctrl.value = ""
        ctrl.update()
    

    def change_text_hint (self, new_hint:str):
        self.ai_suggestion_field.hint_text = new_hint
        self.ai_suggestion_field.value = ""
        if self.ai_suggestion_field.page != None:
            self.ai_suggestion_field.update()
    

    def update_pages_browser(self):
        page_plus_btn = None
        for i in self.pages_browser_row.controls:
            if isinstance(i, flet.TextButton):
                page_plus_btn = i
        
        self.pages_browser_row.controls.clear()
        self.pages_browser_row.controls.append(page_plus_btn)

        for p in self.editor_class.storyboard_content['pages']:
            self.pages_browser_row.controls.append(flet.ElevatedButton(
                text=str(p),
                tooltip=f"Edit '{p}' page | Long-Press to manage",
                bgcolor="white",
                color="blue",
                data=str(p),
                on_click=lambda e: self.editor_class.change_canvas_page(page_name=e.control.data),
                on_long_press=lambda e: self.editor_class.to_rename_a_page(page_name=e.control.data)
            ))
        
        if self.pages_browser_row.page != None:
            self.pages_browser_row.update()
    

    def new_ai_suggestion (self, text:str):
        def sheet_of_suggestion ():
            self.page.dialog = flet.AlertDialog(content=flet.Column(controls=[
                    ParagraphWithTranslateAbility(text=f"{text}"),
                ], scroll=flet.ScrollMode.ADAPTIVE, width=500), open=True)
            self.page.update()
        
        def remove_suggestion_after_while ():
            time.sleep(60)
            self.ai_chat_row.controls[0].content = self.content_of_ai_icon
            self.ai_chat_row.controls[0].update()
        

        self.editor_class.application_class.push_notifications(
            icon="NEW_RELEASES_OUTLINED", 
            icon_color="#DEB64B", 
            title="AI have a feedback to say 👨‍💻!",
            on_click=sheet_of_suggestion
        )

        self.ai_chat_row.controls[0].content = flet.TextButton(content=flet.Text("😃", size=25), tooltip="Click to see my feedback!",
                                                               on_click=lambda e: sheet_of_suggestion(), width=50, height=50)
        self.ai_chat_row.controls[0].update()

        threading.Thread(target=remove_suggestion_after_while, daemon=True).start()
        


    def update(self):
        self._title_label.value = self.title
        return super().update()