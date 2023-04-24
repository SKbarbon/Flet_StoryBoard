# This is the left section part.
from flet import Page, AnimatedSwitcher, Container, Row, Column
import flet
import time

from ..WIDGETS.All import all_widgets
from ..ui_toolkit.widget_browser_frame import Widget_Browse_Frame

class leftSection:
    def __init__(self, page:Page, main_class, main_row:Row) -> None:
        self.page : Page = page
        self.main_class = main_class
        self.main_row = main_row

        self.self_ui = AnimatedSwitcher(transition=flet.AnimatedSwitcherTransition.FADE, duration=500, reverse_duration=250, switch_in_curve=flet.AnimationCurve.EASE, switch_out_curve=flet.AnimationCurve.EASE_IN_BACK)
        self.main_container = Container(bgcolor=page.bgcolor, width=page.width/4-30, height=page.height)
        self.self_ui.content = self.main_container
        main_row.controls.append(self.self_ui)

        #? Show all widgets.
        self.show_all_widgets()


    def show_new_content (self, container:Container):
        self.main_container = container
        self.self_ui.content = container

        if self.self_ui.page != None:
            self.self_ui.update()
        else:
            self.page.update()
        
        if hasattr(self.main_class, "on_page_resize"):
            try: self.main_class.on_page_resize()
            except: pass
    

    def show_all_widgets (self):
        page = self.page
        #* This is the default section.
        
        col = Column(scroll=True)
        title = flet.Text("Widgets", size=25, weight="bold", color="white")
        col.controls.append(title)
        for wid in all_widgets:
            w = Widget_Browse_Frame(wid, all_widgets[wid], self.main_class.add_new_widget, self.main_class.current_page_name)
            col.controls.append(w)
        

        self.main_container = Container(bgcolor=page.bgcolor, width=page.width/4, height=page.height)
        self.main_container.content = col
        self.show_new_content(self.main_container)
        self.page.update()
    

    def show_the_suggestions (self):
        pass