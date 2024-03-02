import flet
from ...tools.color_picker import ColorPicker

class DropDown(object):
    def __init__(self, main_class, parent, *args, **kwargs) -> None:
        self.parent = parent
        self.main_class = main_class
        self.self_object = flet.Dropdown(
            on_focus=self.on_focus,
            on_change=self.on_change
        )
        # all args
        self.args = {
            "items":{"type": str, "default_value": "None"},
            "width": {"type": int, "default_value": 200},
            "height": {"type": int, "default_value": 65},
            "border_radius": {"type": int, "default_value": 12},
            "bgcolor": {"type": ColorPicker, "default_value": "#414141"},
            "color": {"type": ColorPicker, "default_value": "#dcdcdc"},
            "alignment": {"type": list, "options": ["left", "center", "right"], "default_value": "center"},
            "on blur": {"type": str, "default_value": ""},
            "on change": {"type": str, "default_value": ""},
            "on focus": {"type": str, "default_value": ""},
        }

        # Template dict
        # This is where the widget data will be stored.
        self.template = {
            "widget_class_name": "DropDown",
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

        def generate_item_list(string):
            separated_list = [item.strip() for item in string.split(',')]
            return separated_list

        tf.width = props["width"]
        tf.height = props["height"]
        tf.bgcolor = props["bgcolor"]
        tf.color = props["color"]
        tf.border_radius = props["border_radius"]

        # clear previous options
        tf.options.clear()
        if props["items"] != "":
            for item in generate_item_list(props["items"]):
                tf.options.append(flet.dropdown.Option(item))
        self.tf = tf

        if self.self_object.page is not None:
            self.self_object.update()


    def on_focus(self, event):
        if self.main_class.development_mode:
            return
        else:
            props = self.template["properties"]
            if props["on focus"] == "":
                return

            if props["on focus"] in self.main_class.storyboard_class.functions:
                self.main_class.storyboard_class.functions[props["on start"]]()
            else:
                fn = props["on focus"]
                print(f"Pass error: There is not function found called {fn}")

    def on_change(self, event):
        if self.main_class.development_mode:
            return
        else:
            props = self.template["properties"]
            if props["on blur"] != "":
                self.main_class.storyboard_class.functions[props["on blur"]](self.self_object.value)
            if props["on change"] == "":
                return

            if props["on change"] in self.main_class.storyboard_class.functions:
                self.main_class.storyboard_class.functions[props["on change"]](self.self_object.value)
            else:
                fn = props["on change"]
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