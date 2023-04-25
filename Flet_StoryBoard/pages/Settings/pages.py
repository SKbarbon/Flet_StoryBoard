from flet import *
import flet

from ...Tools.color_picker import colorPicker

def page_settings_page (settings_class):
    def allow_scrolling (e):
        settings_class.main_class.dict_content["storyboard_settings"]["allow_scroll"] = e.control.value
        page : flet.Page = settings_class.page
        page.snack_bar = flet.SnackBar(flet.Text(f"Done! But this is not saved, you must go click 'Save' on the editor."))
        page.snack_bar.open = True
        settings_class.main_class.preview_section.update_preview()
        page.update()

    def on_change_bgcolor (color):
        settings_class.main_class.dict_content["pages"][current_page_name]["settings"]["bgcolor"] = color
        page : flet.Page = settings_class.page
        page.snack_bar = flet.SnackBar(flet.Text(f"Done! But this is not saved, you must go click 'Save' on the editor."))
        page.snack_bar.open = True
        settings_class.main_class.preview_section.update_preview()
        page.update()

    v = settings_class.page_viewing_section
    v.clean()

    current_page_name = settings_class.main_class.current_page_name
    title = flet.Text(f"\n   Pages - {current_page_name}", color="white", weight="bold", size=28)
    v.controls.append(title)

    if "allow_scroll" not in settings_class.main_class.dict_content["storyboard_settings"]:
        settings_class.main_class.dict_content["storyboard_settings"]["allow_scroll"] = False
    Allow_Scrolling = flet.Row([
        flet.Text("Allow scrolling", color="white", width=300),
        flet.Switch(on_change=allow_scrolling,
        value=settings_class.main_class.dict_content["storyboard_settings"]["allow_scroll"])
    ], alignment="center")
    v.controls.append(Allow_Scrolling)

    cp = colorPicker(v, settings_class.main_class.dict_content["pages"][current_page_name]["settings"]["bgcolor"], 
    on_choose_color=on_change_bgcolor, title_name="bgcolor", add_it=False)
    v.controls.append(flet.Container(flet.Row([cp.v], alignment="center"), bgcolor="black"))

    v.update()