from fletsb import uikit
import flet



class Settings ():
    def __init__ (self, close_function, editor_class):
        self.editor_class = editor_class
        self.close_function = close_function
        
        self.view = uikit.NavigationView("Settings", self.close_settings)

        self.page_settings = uikit.PageSettingsForum(
            editor_class=self.editor_class,
            page_name=str(self.editor_class.current_page_name)
        )

        self.view.add_new_navigation(navigation_name="Page", navigation_content=flet.Container(content=self.page_settings, padding=30), on_navigate=self.page_settings.refresh_forum)
        self.view.add_new_navigation(navigation_name="Editor & Canvas", navigation_content=flet.Row([
            flet.Text(f"No settings or options availble for Editor & Canvas yet.")
        ], alignment=flet.MainAxisAlignment.CENTER))

        self.view.open_navigation("Page")


    @property
    def editor_settings (self):
        return flet.Text("Editor")


    def close_settings (self, e):
        self.close_function()