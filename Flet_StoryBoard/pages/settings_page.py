from flet import AlertDialog
import flet
import time

from ..pages.page_preview import Page_Preview_Page
from ..widgets.color_picker import ColorPicker


def push_settings(page:flet.Page, self_class):
    last_on_close = page.on_close


    def close_settings(me):
        D.open = False
        page.window_prevent_close = False
        page.on_close = last_on_close
        self_class.preview_page.clean()
        if "width" in preview_data:
            try: int(width_edit.value)
            except: return
            self_class.storyboard_json["preview_settings"].update({"width" : int(width_edit.value)})
        if "height" in preview_data:
            try: int(height_edit.value)
            except: return
            self_class.storyboard_json["preview_settings"].update({"height":int(height_edit.value)})
        if "border_radius" in preview_data:
            try: int(border_radius_edit.value)
            except: return
            self_class.storyboard_json["preview_settings"].update({"border_radius":int(border_radius_edit.value)})
        if "bgcolor" in preview_data:
            self_class.storyboard_json["preview_settings"].update({"bgcolor":str(bgcolor_edit.selected_color)})

        Page_Preview_Page(self_class, self_class.preview_page)
        page.update()
    
    preview_data = self_class.storyboard_json["preview_settings"]
    standered_width = 250
    D = AlertDialog(modal=True)

    main_column = flet.Column(width=600)
    sheet = flet.Container(main_column, width=600)

    Close_Btn = flet.IconButton("CLOSE_SHARP", on_click=close_settings, tooltip="close the settings sheet")
    main_column.controls.append(Close_Btn)


    Title = flet.Text("Settings", size=28)
    main_column.controls.append(Title)

    main_column.controls.append(flet.Divider())

    SubTitle1 = flet.Text("Preview settings", size=18)
    main_column.controls.append(SubTitle1)
    main_column.controls.append(flet.Text("This is the preview settings on this edit page, and the result widget settings.", size=12))
    
    if "width" in preview_data:
        width_edit = flet.TextField(label="width", value=f"{preview_data['width']}", width=standered_width)
        main_column.controls.append(width_edit)

    
    if "height" in preview_data:
        height_edit = flet.TextField(label="height", value=f"{preview_data['height']}", width=standered_width)
        main_column.controls.append(height_edit)

    if "border_radius" in preview_data:
        border_radius_edit = flet.TextField(label="border_radius", value=f"{preview_data['border_radius']}", width=standered_width)
        main_column.controls.append(border_radius_edit)
    
    
    if "bgcolor" in preview_data:
        bgcolor_edit = ColorPicker(selected_color=f"{preview_data['bgcolor']}", label="bgcolor")
        main_column.controls.append(bgcolor_edit.ui_self)



    D.open = True
    D.content = sheet
    page.add(D)
    page.window_prevent_close = True
    page.update()