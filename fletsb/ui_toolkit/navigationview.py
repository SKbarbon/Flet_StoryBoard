import flet



class NavigationView (object):
    """A view that allow to add sections and section content"""
    def __init__(self, title:str, scrollable_sections=False, on_close=None) -> None:
        self.view = flet.Column(controls=[flet.Text("", height=10)])

        self.title = flet.Text(f"    {title}", size=20, weight=flet.FontWeight.BOLD, 
                               color="white", semantics_label=f"Title: {title}")
        
        if on_close is None:
            self.view.controls.append(self.title)
        else:
            self.title.value = self.title.value.replace("    ", "")
            self.view.controls.append(
                flet.Row([
                    flet.IconButton(icon=flet.icons.CLOSE, on_click=on_close),
                    self.title
                ])
            )

        if scrollable_sections:
            self.sections_row = flet.Row(controls=[flet.Text("  ")], alignment=flet.MainAxisAlignment.CENTER, scroll=scrollable_sections)
        else:
            self.sections_row = flet.Row(alignment=flet.MainAxisAlignment.CENTER)
        self.view.controls.append(self.sections_row)

        self.content_place = flet.AnimatedSwitcher(
            content=flet.Row([flet.Text("Please choose a section", color="white")], alignment="center"),
            transition=flet.AnimatedSwitcherTransition.FADE,
            duration=500,
            reverse_duration=200,
            switch_in_curve=flet.AnimationCurve.EASE_IN,
            switch_out_curve=flet.AnimationCurve.EASE_OUT
        )
        self.view.controls.append(self.content_place)

        # props
        self.all_sections = {}
        self.last_navigation_selected = None


    def add_section (self, section_name:str, section_content:flet.Control, on_navigate=None):
        def start_section (e):
            if self.last_navigation_selected != None:
                self.last_navigation_selected.bgcolor = "white"
                self.last_navigation_selected.color = "black"
                self.last_navigation_selected = e.control
                e.control.bgcolor = "blue"
                e.control.color = "white"
            else:
                self.last_navigation_selected = e.control
                e.control.bgcolor = "blue"
                e.control.color = "white"
            self.open_a_section(section_name=section_name)
            if on_navigate != None:
                on_navigate(section_name)
            self.view.update()
        
        con = self.navigation_link(section_name=section_name, on_click=start_section)
        self.sections_row.controls.append(con)

        self.all_sections.update({
            f"{section_name}": {
                "content" : section_content,
                "flet_class_button" : con,
                "on_navigate" : on_navigate
            }
        })

    def open_a_section (self, section_name:str):
        if section_name not in self.all_sections: return
        if self.all_sections[section_name]['flet_class_button'] is not self.last_navigation_selected and self.last_navigation_selected != None:
            self.last_navigation_selected.bgcolor = "white"
            self.last_navigation_selected.color = "black"
            self.last_navigation_selected = self.all_sections[section_name]['flet_class_button']
            self.last_navigation_selected.bgcolor = "blue"
            self.last_navigation_selected.color = "white"
        elif self.last_navigation_selected == None:
            self.last_navigation_selected = self.all_sections[section_name]['flet_class_button']
            self.last_navigation_selected.bgcolor = "blue"
            self.last_navigation_selected.color = "white"
        
        self.content_place.content = flet.Row([self.all_sections[section_name]['content']], alignment=flet.MainAxisAlignment.CENTER)
        if self.view.page != None:
            self.view.update()

    def navigation_link (self, section_name, on_click):
        return flet.ElevatedButton(text=f"{section_name}", on_click=on_click, bgcolor="white", color="black")


if __name__ == "__main__":
    def test(page:flet.Page):
        page.bgcolor = "black"
        page.padding = 0
        n = NavigationView(title="Example", scrollable_sections=True)
        page.add(n.view)

        n.add_section(section_name="Example1", section_content=flet.Text("Example1 section", color="white"))
        n.add_section(section_name="Example2", section_content=flet.Text("Example2 section", color="white"))

        n.view.update()

    flet.app(target=test)