import flet


class Image(object):
    def __init__(self, main_class, parent, *args, **kwargs) -> None:
        self.parent = parent
        self.main_class = main_class
        self.self_object = flet.Image(fit=flet.ImageFit.COVER)

        # all args
        self.args = {
            "src": {"type": str, "default_value": "https://picsum.photos/id/237/200/300"},
            "width": {"type": int, "default_value": 150},
            "height": {"type": int, "default_value": 150},
            "border_radius": {"type": int, "default_value": 75},
            "alignment": {"type": list, "options": ["left", "center", "right"], "default_value": "center"},
        }

        # Template dict
        # This is where the widget data will be stored.
        self.template = {
            "widget_class_name": "Image",
            "properties": {}
        }
        for p in self.args:
            self.template["properties"][p] = self.args[p]["default_value"]

        self.update()

    def update(self, new_props: dict = None):
        img = self.self_object
        props = self.template["properties"]

        if new_props is not None:
            for i in new_props:
                self.template["properties"][i] = new_props[i]

        img.src = props["src"]
        img.width = props["width"]
        img.height = props["height"]
        img.border_radius = props["border_radius"]

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
