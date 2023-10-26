import flet


class SceneButtonbarEditor (flet.Row):
    """A topbar that being used on a scene object."""
    def __init__ (self, on_accept_suggestion=None, on_ask_ai=None, on_click_floating_btn=None):
        super().__init__()
        self.controls.append(flet.Text("    ", height=15))

        self.ai_suggestion_field = flet.TextField(
            hint_text="Ask AI to add..",
            border="none",
            text_size=15,
            on_submit=lambda e: self.process_action(e, on_ask_ai),
            text_style=flet.TextStyle(weight=flet.FontWeight.W_200)
        )
        ai_chat_row = flet.Row([
            flet.Container(
                content=flet.Icon("CHAT_BUBBLE_OUTLINE_ROUNDED", color="white"),
                on_click=lambda e: self.process_action(e, on_accept_suggestion)
            ),
            self.ai_suggestion_field,
        ])
        self.controls.append(ai_chat_row)

        self.controls.append(flet.Text("", expand=True))

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
    

    def process_action (self, e, action):
        if action == None: return
        ctrl : flet.Control = e.control

        ctrl.disabled = True
        ctrl.update()
        action()
        ctrl.disabled = False
        ctrl.update()
    

    def change_text_hint (self, new_hint:str):
        self.ai_suggestion_field.hint_text = new_hint
        self.ai_suggestion_field.value = ""
        if self.ai_suggestion_field.page != None:
            self.ai_suggestion_field.update()


    def update(self):
        self._title_label.value = self.title
        return super().update()