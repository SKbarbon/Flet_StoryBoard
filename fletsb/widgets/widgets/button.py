import flet
from ...tools.color_picker import ColorPicker


class Button(object):
    def __init__(self, main_class, parent, *args, **kwargs) -> None:
        self.parent = parent
        self.main_class = main_class
        self.self_object = flet.ElevatedButton(on_click=self.on_button_click)

        # all args
        self.args = {
            "text": {"type": str, "default_value": "click me"},
            "function name": {"type": str, "default_value": ""},
            "text_color": {"type": ColorPicker, "default_value": "black"},
            "bgcolor": {"type": ColorPicker, "default_value": "white"},
            "alignment": {"type": list, "options": ["left", "center", "right"], "default_value": "center"},
            "width": {"type": int, "default_value": 95},
            "height": {"type": int, "default_value": 40},
            "hide": {"type": bool, "default_value": False}
        }

        # Template dict
        # This is where the widget data will be stored.
        self.template = {
            "widget_class_name": "Button",
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

        t.text = props["text"]
        t.color = props["text_color"]
        t.bgcolor = props["bgcolor"]
        t.width = props["width"]
        t.height = props["height"]
        t.visible = props["hide"] == False

        if self.self_object.page is not None:
            self.self_object.update()

    def on_button_click(self, event):
        if self.main_class.development_mode:
            return
        else:
            props = self.template["properties"]
            if props["function name"] == "":
                return

            if props["function name"] in self.main_class.storyboard_class.functions:
                self.main_class.storyboard_class.functions[props["function name"]]()
            else:
                fn = props["function name"]
                print(f"Pass error: There is not function found called {fn}")

    def return_widget(self):
        props = self.template["properties"]
        if self.main_class.development_mode:
            self.self_object.disabled = True
        if props["alignment"] == "left":
            return flet.Row([flet.Text("    "), self.self_object])
        elif props["alignment"] == "center":
            return flet.Row([self.self_object], alignment=flet.MainAxisAlignment.CENTER)
        else:
            return flet.Row([self.self_object, flet.Text("    ")], alignment=flet.alignment.center_right)
