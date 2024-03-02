import flet
from ...tools.color_picker import ColorPicker


class FilePicker(object):
    def __init__(self, main_class, parent, *args, **kwargs) -> None:
        self.parent = parent
        self.main_class = main_class
        self.self_object = flet.ElevatedButton(on_click=self.on_button_click)
        self.pick_files_dialogue = None
        self.is_instanced = False

        # all args
        file_methods = ["get_directory_path", "pick_files", "save_file"]
        self.args = {
            "text": {"type": str, "default_value": "Open file"},
            "function name": {"type": str, "default_value": ""},
            "pick type": {"type": list, "options": file_methods, "default_value": "pick_files"},
            "allow multiple": {"type": bool, "default_value": True},
            "width": {"type": int, "default_value": 150},
            "height": {"type": int, "default_value": 45},
            "alignment": {"type": list, "options": ["left", "center", "right"], "default_value": "center"},
            "bgcolor": {"type": ColorPicker, "default_value": "black"},
            "text_color": {"type": ColorPicker, "default_value": "blue"}
        }

        # Template dict
        # This is where the widget data will be stored.
        self.template = {
            "widget_class_name": "FilePicker",
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

        if self.self_object.page is not None:
            self.self_object.update()

    def on_button_click(self, event):
        if self.main_class.development_mode:
            return

        props = self.template["properties"]
        fn_name = props["function name"]
        pick_type = props["pick type"]

        # Handles file picking and return values
        def open_file(pick_files_dialogue):
            if pick_type == "pick_files":
                pick_files_dialogue.pick_files(allow_multiple=props["allow multiple"])
            elif pick_type == "save_file":
                pick_files_dialogue.save_file()
            elif pick_type == "get_directory_path":
                pick_files_dialogue.get_directory_path()

        if not fn_name:
            return

        if fn_name in self.main_class.storyboard_class.functions:
            if not self.is_instanced:
                self.pick_files_dialogue = flet.FilePicker(on_result=self.main_class.storyboard_class.functions[fn_name])
                self.main_class.storyboard_class.add_flet_overlay(self.pick_files_dialogue)
                self.is_instanced = True
        else:
            print(f"Pass error: There is no function found called {fn_name}")
            return

        open_file(self.pick_files_dialogue)

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
