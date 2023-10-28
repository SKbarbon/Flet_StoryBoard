from fletsb import widgets


def get_all_widgets ():
    return {
        "Title": "TITLE_ROUNDED",
        "Row": "VIEW_COLUMN_ROUNDED",
        "Column": "TABLE_ROWS_ROUNDED",
        "Paragraph": "SHORT_TEXT_ROUNDED",
        "Image": "IMAGE_OUTLINED"
    }


def get_widget_class_by_name (widget_name:str) -> widgets.Widget:
    ws = {
        "Title": widgets.Title,
        "Row": widgets.Row,
        "Column": widgets.Column,
        "Paragraph": widgets.Paragraph,
        "Image": widgets.Image
    }


    if widget_name in ws:
        return ws[widget_name]
    else:
        raise Exception(f"Error: No supported widget named '{widget_name}'.")