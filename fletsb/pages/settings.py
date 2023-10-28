from fletsb import uikit
import flet



class Settings ():
    def __init__ (self, close_function):
        self.close_function = close_function
        
        self.view = uikit.NavigationView("Settings", self.close_settings)

        for nav in ["Page", "Editor"]:
            self.view.add_new_navigation(navigation_name=nav, navigation_content=flet.Text(f"{nav}"))

        self.view.open_navigation("Page")   

    def close_settings (self, e):
        self.close_function()