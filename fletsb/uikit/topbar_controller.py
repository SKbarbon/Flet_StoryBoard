import flet


class TopbarController (flet.Row):
    def __init__(self, page:flet.Page):
        super().__init__()
        self.page = page
        self.controls.append(flet.Text("    ", height=15))

        self.close_app_button = flet.Container(
            bgcolor="red",
            width=15,
            height=15,
            border_radius=7.5,
            on_click=lambda e: page.window_close(),
            tooltip="Close app"
        )
        self.controls.append(self.close_app_button)

        self.minimize_app_button = flet.Container(
            bgcolor=flet.colors.YELLOW_300,
            width=15,
            height=15,
            border_radius=7.5,
            on_click=lambda e: self.minimise_app(),
            tooltip="Minimise window"
        )
        self.controls.append(self.minimize_app_button)

        self.fullscreen_app_button = flet.Container(
            bgcolor=flet.colors.GREEN_400,
            width=15,
            height=15,
            border_radius=7.5,
            on_click=lambda e: self.full_screen(),
            tooltip="Enter full screen"
        )
        self.controls.append(self.fullscreen_app_button)
    
    def minimise_app(self):
        self.page.window_full_screen = False
        self.page.window_minimized = True
        self.page.update()
    

    def full_screen(self):
        self.page.window_full_screen = True
        self.page.window_minimized = False
        self.page.update()