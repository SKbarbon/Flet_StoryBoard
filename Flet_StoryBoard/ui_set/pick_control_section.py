import flet

# local imports
from ..tools.all_controls import get_all_supported_controls


def push_control_picker (name, icon, on_pick):
    def onHover (me):
        if me.data == "true":
            v.bgcolor = flet.colors.WHITE54
        else:
            v.bgcolor = flet.colors.WHITE12
        v.update()
    
    v = flet.Container(on_click=on_pick, bgcolor=flet.colors.WHITE12, on_hover=onHover, border_radius=7, height=35)
    mrv = flet.Row()

    ICOn = flet.Icon(icon, color="white", size=20)
    Title = flet.Text(name, color="white")

    mrv.controls.append(flet.Text(" "))
    mrv.controls.append(ICOn)
    mrv.controls.append(Title)

    v.content = mrv
    return v

def pickControlSection (mainview, on_pick):
    def gen (i, all_con):
        def on_click_edit(me):
            on_pick(name, True, 0)
        name = i
        icon = all_con[i]["icon"]
        cont = push_control_picker(name=name, icon=icon, on_pick=on_click_edit)
        return cont
    
    Title = flet.Text("Flet controls", size=21, weight="bold", color="white")
    mainview.controls.append(Title)

    all_con = get_all_supported_controls()
    for i in all_con:
        cont = gen(i, all_con)

        mainview.controls.append(cont)