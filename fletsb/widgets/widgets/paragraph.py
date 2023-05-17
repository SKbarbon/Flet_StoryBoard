import flet
from ...tools.color_picker import ColorPicker


class Paragraph(object):
    def __init__(self, main_class, parent, *args, **kwargs) -> None:
        self.parent = parent
        self.main_class = main_class
        self.self_object = flet.Text("")

        # all args
        self.args = {
            "text": {"type": str,
                     "default_value": "dude,\nThere is no one who loves pain itself, who seeks after it and wants to have it, simply because it is pain 🙃...",
                     "multi_line": True},
            "text_color": {"type": ColorPicker, "default_value": "white"},
            "size": {"type": int, "default_value": 16},
            "width": {"type": int, "default_value": 300},
            "italic": {"type": bool, "default_value": False},
            "bold": {"type": bool, "default_value": False},
            "hide": {"type": bool, "default_value": False},
            "expand": {"type": bool, "default_value": False},
            "alignment": {"type": list, "options": ["left", "center", "right"], "default_value": "center"},
            "text_align": {"type": list, "options": ["left", "center", "right"], "default_value": "left"}
        }

        # Template dict
        # This is where the widget data will be stored.
        self.template = {
            "widget_class_name": "Paragraph",
            "properties": {}
        }
        for p in self.args:
            self.template["properties"][p] = self.args[p]["default_value"]

        self.update()

    def update(self, new_props: dict = None):
        t = self.self_object
        props = self.template["properties"]

        if new_props is not None:
            for i in new_props:
                self.template["properties"][i] = new_props[i]

        t.value = props["text"]
        t.size = props["size"]
        t.color = props["text_color"]
        t.width = props["width"]
        t.expand = props["expand"]
        t.italic = props["italic"]
        t.visible = props["hide"] == False

        if str(props["text_align"]).lower() == "left":
            t.text_align = flet.TextAlign.LEFT
        elif str(props["text_align"]).lower() == "center":
            t.text_align = flet.TextAlign.CENTER
        elif str(props["text_align"]).lower() == "right":
            t.text_align = flet.TextAlign.RIGHT

        if props["bold"]:
            t.weight = "bold"
        else:
            t.weight = "normal"

        if self.self_object.page is not None:
            self.self_object.update()

    def return_widget(self):
        props = self.template["properties"]
        if props["alignment"] == "left":
            return flet.Row([flet.Text("    "), self.self_object])
        elif props["alignment"] == "center":
            return flet.Row([self.self_object], alignment=flet.MainAxisAlignment.CENTER)
        else:
            return flet.Row([self.self_object, flet.Text("    ")], alignment=flet.alignment.center_right)
