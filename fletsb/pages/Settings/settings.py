from ...ui_toolkit.navigationview import NavigationView
import flet


class SettingsPage:
    def __init__ (self, main_class):
        self.remove_the_bgcover = None
        self.navigationview = NavigationView(title="Settings", scrollable_sections=True, on_close=self.close)

        self.navigationview.add_section(section_name="StoryBoard", section_content=flet.Text("StoryBoard"))
        self.navigationview.add_section(section_name="This page", section_content=flet.Text("This page"))

        self.navigationview.open_a_section("This page")
    
    def close (self, e=None):
        self.remove_the_bgcover()