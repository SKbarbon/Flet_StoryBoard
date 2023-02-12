import os
import flet
import json
from .ui_tools.built_in_widgets import BuiltIn_Widgets




def load_flet_storyboard(storyboard_name:str, page:flet.Page=None, functions={}) -> flet.Container:
    if str(storyboard_name).endswith(".fletsb"): pass
    else: storyboard_name = storyboard_name + ".fletsb"
    if os.path.isfile(storyboard_name) == False:
        raise OSError(f"Cannot found '{storyboard_name}' flet storyboard")
    
    THE_PREVIEW = flet.Column()
    CONT = flet.Container()
    storyboard_json = json.loads(open(storyboard_name, encoding="utf-8").read())

    for control in storyboard_json["controls"]:
        prop = control[next(iter(control))]["properties"]
        center_it = control[next(iter(control))]["on_row_center"]
        CLASS = BuiltIn_Widgets[str(next(iter(control)))]['class']()
        if "on_click_function" in control[next(iter(control))]:
            if control[next(iter(control))]["on_click_function"]["function_name"] == "none": pass
            elif str(control[next(iter(control))]["on_click_function"]["function_name"]) not in functions: pass
            else:
                setattr(CLASS, str(control[next(iter(control))]["on_click_function"]["attr_name"]), functions[str(control[next(iter(control))]["on_click_function"]["function_name"])])

        for i in prop:
            if hasattr(CLASS, i):
                setattr(CLASS, i, prop[i])
        if center_it:
            THE_PREVIEW.controls.append(flet.Row([CLASS], alignment="center"))
        else:
            THE_PREVIEW.controls.append(CLASS)
    
    preview_settings = storyboard_json["preview_settings"]
    for i in preview_settings:
        if hasattr(THE_PREVIEW, i):
            setattr(THE_PREVIEW, i, preview_settings[i])
        if hasattr(CONT, i):
            setattr(CONT, i, preview_settings[i])
    

    CONT.content = THE_PREVIEW
    if page != None:
        page.vertical_alignment = flet.MainAxisAlignment.CENTER
        page.add(flet.Row([CONT], alignment="center"))
    return CONT