from fletsb import widgets



def get_widget_class_by_name (widget_name:str) -> widgets.Widget:
    ws = {
        "Title": widgets.Title,
        "Row": widgets.Row
    }


    if widget_name in ws:
        return ws[widget_name]
    else:
        raise Exception(f"Error: No supported widget named '{widget_name}'.")