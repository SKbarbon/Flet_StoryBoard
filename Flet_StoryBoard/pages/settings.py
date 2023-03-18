import flet
import json
from ..built_in_widgets.color_picker import colorPicker

def Settings (main_class):
    def save_all (me):
        d = {}
        for i in all_f:
            d.update({f"{i}":all_f[i].value})
        main_class.file_as_dict["page_settings"].update(d)
        main_class.prev_engine.update()
        main_class.page.update()
    
    page_info = main_class.page_settings
    main = flet.Column(width=500, height=550, scroll=True)
    Title = flet.Text(f"  Settings", size=25, weight="bold", expand=True)
    save_button = flet.TextButton("done edit", on_click=save_all, expand=True)
    main.controls.append(flet.Row([Title, save_button], alignment="center"))
    main.controls.append(flet.Divider())

    t1 = flet.Text("  Page settings", size=18)
    main.controls.append(t1)

    all_f = {}
    for i in page_info:
        if type(page_info[i]) == type(str()):
            tf = flet.TextField(label=i, value=page_info[i])
            all_f.update({f"{i}":tf})
            main.controls.append(flet.Row([tf], alignment="center"))
        
        elif type(page_info[i]) == type(int()):
            tf = flet.TextField(label=i, value=page_info[i])
            all_f.update({f"{i}":tf})
            main.controls.append(flet.Row([tf], alignment="center"))
        
        elif type(page_info[i]) == type(bool()):
            sw = flet.Switch(value=page_info[i], label="{value}%")
            all_f.update({f"{i}":sw})
            tx = flet.Text(i)
            main.controls.append(flet.Row([tx, sw], alignment="center"))

    save_button2 = flet.TextButton("done edit", on_click=save_all)
    main.controls.append(flet.Row([save_button2], alignment="center"))
    return main