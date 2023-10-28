from .widget import Widget
import flet



class Image (Widget):
    def __init__(self, storyboard_class) -> None:
        super().__init__(storyboard_class)

        self.flet_object = flet.Image("")

        self.data['widget_name'] = "Image"
    

    def update_flet_object(self):
        super().update_flet_object()

        properties = self.data['properties']
        src = properties['src']
        src_base64 = properties['src_base64']
        width = properties['width']
        height = properties['height']
        expand = properties['expand']


        if src_base64 != "":
            # If src_base64
            self.flet_object.src_base64 = src_base64
        else:
            self.flet_object.src = src
        
        self.flet_object.width = width
        self.flet_object.height = height
        self.flet_object.expand = expand


        if self.flet_object.page != None:
            self.flet_object.update()
    

    def properties_data(self):
        return {
            "src": {"type": "str", "default_value": "https://picsum.photos/200"},
            "src_base64": {"type": "str", "default_value":""},
            "width": {"type": "int", "default_value": 150},
            "height": {"type": "int", "default_value": 150},
            "expand": {"type": "bool", "default_value": False}
        }