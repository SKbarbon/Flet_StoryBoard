import flet



class AppBar (object):
    def __init__(self, main_class) -> None:
        self.main_class = main_class
        self.page : flet.Page = main_class.page

        self.main_bar = flet.Container(
            width=self.page.width - 25, 
            height=50, 
            bgcolor="white", 
            border_radius=12
        )
        self.main_row = flet.Row(expand=True)
        self.main_bar.content = self.main_row

        self.title = flet.Text("   Flet_StoryBoard", size=15, weight="bold", color="black", expand=True)
        self.main_row.controls.append(self.title)

        self.refresh()

    def phone_mode (self):
        self.main_row.controls.append(
            flet.IconButton(content=flet.Icon(
            name=flet.icons.MENU_ROUNDED, color="black", 
            size=20
            ), on_click=self.menu_sheet)
        )

    def pad_mode (self):
        pass

    def menu_sheet (self, e=None):
        def close_sheet (e):
            if isinstance(e.control, flet.IconButton):
                remove_function()
                return
            if str(e.data).lower() == "false":
                remove_function()
                return
        
        c = flet.Container(
            bgcolor="white",
            width=self.page.window_width - 30,
            height=self.page.window_height - 50,
            border_radius=12,
            on_hover=close_sheet,
        )

        cc = flet.Column(alignment=flet.MainAxisAlignment.START, expand=True)
        c.content = cc

        r = flet.Row([
            flet.IconButton(content=flet.Icon(
                name=flet.icons.CLOSE_SHARP,
                color="black"
            ), on_click=close_sheet)
        ], alignment=flet.MainAxisAlignment.END)
        cc.controls.append(r)

        remove_function = self.main_class.push_on_stack(flet.Column(controls=[
            flet.Row([
                c
            ], alignment=flet.MainAxisAlignment.CENTER, expand=True)
        ], alignment=flet.MainAxisAlignment.START))

    def refresh (self):
        self.main_row.controls.clear()
        self.main_row.controls.append(self.title)

        if self.page.window_width < 500:
            # if phone
            self.phone_mode()
        else:
            # if desktop, iPad or tablet
            self.pad_mode()