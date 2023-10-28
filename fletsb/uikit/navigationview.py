import flet

class NavigationView (flet.Column):
    def __init__ (self, title:str, on_click_close):
        super().__init__()

        # Stored-Events data
        self.last_selected = None
        self.all_navigations = {}

        # UI
        self.normal_navigationlink_bgcolor = "#509bff"


        self.controls.append(flet.TextButton(
            content=flet.Text("Close", color="white", weight="bold"),
            on_click=on_click_close)
        )

        self.title_label = flet.Text(
            value=f"{title}",
            weight="bold",
            size=35
        )
        self.controls.append(flet.Row([flet.Text(""), self.title_label], spacing=50))


        self.navigations_row = flet.Row([flet.Text("      ")], scroll=flet.ScrollMode.AUTO, spacing=5)
        self.controls.append(self.navigations_row)

        self.content_place = flet.Container()
        self.controls.append(self.content_place)

    

    def add_new_navigation (self, navigation_name:str, navigation_content:flet.Control):
        def on_open_navigationpage (e):
            self.open_navigation(navigation_name=navigation_name)

        label = flet.Text(f"{navigation_name}", color=flet.colors.WHITE)
        c = flet.Container(
            content=flet.Row([
                label
            ], alignment=flet.MainAxisAlignment.CENTER),
            bgcolor=self.normal_navigationlink_bgcolor,
            border_radius=18,
            width=150,
            height=40,
            tooltip=f"Open {navigation_name}"
        )
        self.navigations_row.controls.append(flet.TextButton(content=c, on_click=on_open_navigationpage))

        self.all_navigations[navigation_name] = {
            "content": navigation_content,
            "flet_object": c
        }
    

    def open_navigation (self, navigation_name:str):
        if navigation_name not in self.all_navigations:
            print(f"Error Passed: No navigation named '{navigation_name}'")
            return
        if self.last_selected != None:
            self.last_selected.content.controls[0].color = "white"
            self.last_selected.bgcolor = self.normal_navigationlink_bgcolor
            self.last_selected.update()
            
        c = self.all_navigations[navigation_name]['flet_object']
        label = c.content.controls[0]
        self.last_selected = c
        label.color = "black"
        c.bgcolor = "white"

        self.content_place.content = self.all_navigations[navigation_name]['content']

        if self.content_place.page != None:
            c.update()
            self.content_place.update()


if __name__ == "__main__":
    def test (page:flet.Page):
        page.theme_mode = flet.ThemeMode.DARK
        n = NavigationView("Test", print)
        page.add(n)

        n.add_new_navigation("Home", flet.Text("Home!"))
        n.update()

        n.add_new_navigation("Settings", flet.Text("Settings!"))
        n.update()

        n.add_new_navigation("Community", flet.Text("Communithy!"))
        n.update()
    
    flet.app(target=test)