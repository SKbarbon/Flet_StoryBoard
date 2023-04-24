import flet




def Widget_Browse_Frame (widget_name, widget_info_dict, on_click, page_name):
    def action (event):
        on_click(widget_name, page_name)

    def on_hover (event):
        if event.data == "true":
            event.control.bgcolor = "#474747"
            event.control.update()
        else:
            event.control.bgcolor = "#5C5C5C"
            event.control.update()

    c = flet.Container(width=170, height=35, bgcolor="#5C5C5C", on_click=action, expand=True, on_hover=on_hover)
    c.border_radius = 12

    r = flet.Row([
        flet.Text(" "),
        flet.Icon(widget_info_dict["icon"], size=18, color="white"),
        flet.Text(widget_name, size=13, color="white")
    ], spacing=12)
    c.content = r

    return flet.Row([c], alignment="center")