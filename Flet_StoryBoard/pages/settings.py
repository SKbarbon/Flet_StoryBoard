from flet import Page
import flet
import time

from .Settings.pages import page_settings_page

class SettingsPage:
    def __init__(self, page:Page, main_class) -> None:
        self.page : Page = page
        self.main_class = main_class
        #? Create a copy of things.
        self.__last_keyboard_manager = main_class.manage_keyboard_commands
        self.__last_controls = list(page.controls)
        self.__lat_appbar = page.appbar
        self.__last_on_resize_function = main_class.on_page_resize
        
        #? For keyboard events
        self.current_selected_page = None
        self.page_opend = True
        #? Hide all page controls
        self.hide_all()

        #? ReSet all page controls
        page.on_keyboard_event = self.keyboard_keys_manager
        page.on_resize = self.on_page_resize
        page.controls.clear()
        page.appbar = None
        page.bgcolor = "black"
        page.update()

        main_row = flet.Row(alignment="center")
        page.add(main_row)

        #? pages browseing section
        pages_browser_container = flet.Container(border_radius=12)
        self.pages_broswer = flet.Column(width=page.width/3, height=page.height-50, scroll=True)
        pages_browser_container.content = self.pages_broswer
        main_row.controls.append(pages_browser_container)
        page.update()

        #? viewing selected page section
        page_viewing_section_container = flet.Container(bgcolor="#1C1C1E", border_radius=12)
        self.page_viewing_section = flet.Column(width=page.width-(page.width/3)-50, height=page.height-50, scroll=True)
        page_viewing_section_container.content = self.page_viewing_section
        main_row.controls.append(page_viewing_section_container)
        page.update()

        #? The title and back_btn
        title = flet.Text(" Settings", size=28, weight="bold", color="white")
        self.pages_broswer.controls.append(flet.Row([
            flet.IconButton("CLOSE_ROUNDED", on_click=self.go_back, icon_color="white", width=30), title
        ], spacing=0))

        self.pages_broswer.controls.append(flet.Text(""))

        #? show all settings pages
        for p in self.get_all_settings_pages():
            self.pages_broswer.controls.append(page_navigator_frame_button(p, self.get_all_settings_pages()[p]["icon"], self.get_all_settings_pages()[p]["function"],self))
        
        page.update()

    def open_new_settings_page(self, control):
        """Open a new sub-page on settings page"""
        pass

    def route_to_page (self):
        """Use flet Route to a page"""
    
    def hide_all (self):
        page : Page = self.page
        for i in range(10):
            for c in page.controls:
                c.opacity = c.opacity - 0.1
                page.appbar.opacity = page.appbar.opacity - 0.1
                c.update()
            for ac in page.appbar.actions:
                ac.opacity = ac.opacity - 0.1
                ac.update()
            page.appbar.leading.opacity = page.appbar.leading.opacity - 0.1
            page.appbar.leading.update()
            page.appbar.title.opacity = page.appbar.title.opacity - 0.1
            page.appbar.title.update()
            time.sleep(0.01)

    def go_back (self, *e):
        self.page_opend = False
        page : Page = self.page
        page.on_keyboard_event = self.__last_keyboard_manager
        page.controls.clear()
        page.bgcolor = "black"
        page.appbar = self.__lat_appbar

        for c in self.__last_controls:
            c.opacity = 1.0
            page.controls.append(c)
        
        for ac in page.appbar.actions:
            ac.opacity = 1.0

        page.appbar.leading.opacity = 1.0
        page.appbar.title.opacity = 1.0
        
        page.on_resize = self.__last_on_resize_function
        page.update()

    def on_page_resize (self, e):
        page = self.page
        self.pages_broswer.width = page.width/3 - 50
        self.pages_broswer.height = self.page.height - 50
        self.page_viewing_section.width = page.width-(page.width/3-50)-50
        self.page_viewing_section.height = page.height-50
        self.page.update()
    
    def get_all_settings_pages (self):
        return {
            "Pages" : {"icon":"PREVIEW_ROUNDED", "function":page_settings_page, "name":"Pages"},
            "Editor" : {"icon":"SETTINGS_ROUNDED", "function":editor_page, "name":"Editor"}
        }
    
    def keyboard_keys_manager (self, e):
        if self.page_opend == False: return
        pass


#? Generate page button
def page_navigator_frame_button (name:str, icon, function, settings_class:SettingsPage, as_a_click=False):
    def on_hov (e):
        if str(e.data) == "true":
            container.bgcolor = flet.colors.WHITE60
        else:
            container.bgcolor = None
        container.update()
        if e.control == settings_class.current_selected_page:
            e.control.bgcolor = "blue"
            e.control.update()
    
    def on_click (e):
        if settings_class.current_selected_page == None:
            settings_class.current_selected_page = container
            container.bgcolor = "blue"
            if container.page == None:
                settings_class.page.update()
            else:
                container.update()
        else:
            settings_class.current_selected_page.bgcolor = None
            if settings_class.current_selected_page.page != None:
                settings_class.current_selected_page.update()
            settings_class.current_selected_page = container
            container.bgcolor = "blue"
            if container.page == None:
                settings_class.page.update()
            else:
                container.update()
            
        function(settings_class)
        
        

    container = flet.Container(width=200, height=40, border_radius=12, expand=True, 
    on_hover=on_hov, on_click=on_click)
    r = flet.Row([flet.Text("  ")], alignment="center", width=200)
    container.content = r

    ICON = flet.Icon(icon, size=20, color="white")
    r.controls.append(ICON)

    NAME = flet.Text(name, size=17, color="white", expand=True, text_align="left")
    r.controls.append(NAME)

    if as_a_click:
        container.bgcolor = "blue"
        on_click(container)

    return flet.Row([container], alignment="center")


#? Pages


def editor_page (settings_class:SettingsPage):
    v = settings_class.page_viewing_section
    v.clean()
    v.controls.append(flet.Text("soon", color="white"))
    v.update()