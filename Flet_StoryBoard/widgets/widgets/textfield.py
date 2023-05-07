import flet
from ...tools.color_picker import ColorPicker


class TextField(object):
    def __init__(self, main_class, parent, *args, **kwargs) -> None:
        self.parent = parent
        self.main_class = main_class
        self.self_object = flet.TextField(
            on_focus=self.on_start_type,
            on_change=self.on_change_text,
            on_submit=self.on_end_type,
            selection_color=flet.colors.BLACK,
            cursor_color=flet.colors.BLACK
        )

        # all args
        self.args = {
            "text": {"type": str, "default_value": ""},
            "label": {"type": str, "default_value": "text.."},
            "hint_text": {"type": str, "default_value": "text.."},
            "can_reveal_password": {"type": bool, "default_value": True},
            "password": {"type": bool, "default_value": False},
            "width": {"type": int, "default_value": 200},
            "height": {"type": int, "default_value": 65},
            "border_radius": {"type": int, "default_value": 12},
            "bgcolor": {"type": ColorPicker, "default_value": "white"},
            "color": {"type": ColorPicker, "default_value": "black"},
            "alignment": {"type": list, "options": ["left", "center", "right"], "default_value": "center"},
            "on start": {"type": str, "default_value": ""},
            "on change": {"type": str, "default_value": ""},
            "on end": {"type": str, "default_value": ""},
            "point name": {"type": str, "default_value": ""}
        }

        # Template dict
        # This is where the widget data will be stored.
        self.template = {
            "widget_class_name": "TextField",
            "properties": {}
        }
        for p in self.args:
            self.template["properties"][p] = self.args[p]["default_value"]

        self.update()

    def update(self, new_props: dict = None):
        tf = self.self_object
        props = self.template["properties"]

        if new_props is not None:
            for i in new_props:
                self.template["properties"][i] = new_props[i]

        tf.value = props["text"]
        tf.label = props["label"]
        tf.hint_text = props["hint_text"]
        tf.password = props["password"]
        tf.can_reveal_password = props["can_reveal_password"]
        tf.width = props["width"]
        tf.height = props["height"]
        tf.bgcolor = props["bgcolor"]
        tf.color = props["color"]
        tf.border_radius = props["border_radius"]

        if self.self_object.page is not None:
            self.self_object.update()

    def on_start_type(self, event):
        if self.main_class.development_mode:
            return
        else:
            props = self.template["properties"]
            if props["on start"] == "":
                return

            if props["on start"] in self.main_class.storyboard_class.functions:
                self.main_class.storyboard_class.functions[props["on start"]]()
            else:
                fn = props["on start"]
                print(f"Pass error: There is not function found called {fn}")

    def on_change_text(self, event):
        if self.main_class.development_mode:
            return
        else:
            props = self.template["properties"]
            if props["point name"] != "":
                self.main_class.storyboard_class.points[props["point name"]] = str(self.self_object.value)
            if props["on change"] == "":
                return

            if props["on change"] in self.main_class.storyboard_class.functions:
                self.main_class.storyboard_class.functions[props["on change"]](self.self_object.value)
            else:
                fn = props["on change"]
                print(f"Pass error: There is not function found called {fn}")

    def on_end_type(self, event):
        if self.main_class.development_mode:
            return
        else:
            props = self.template["properties"]
            if props["point name"] != "":
                self.main_class.storyboard_class.points[props["point name"]] = str(self.self_object.value)
            if props["on end"] == "": return

            if props["on end"] in self.main_class.storyboard_class.functions:
                self.main_class.storyboard_class.functions[props["on end"]](self.self_object.value)
            else:
                fn = props["on end"]
                print(f"Pass error: There is not function found called {fn}")

    def return_widget(self):
        if self.main_class.development_mode:
            self.self_object.disabled = True
        props = self.template["properties"]
        if props["alignment"] == "left":
            return flet.Row([flet.Text("    "), self.self_object])
        elif props["alignment"] == "center":
            return flet.Row([self.self_object], alignment=flet.MainAxisAlignment.CENTER)
        else:
            return flet.Row([self.self_object, flet.Text("    ")], alignment=flet.alignment.center_right)
