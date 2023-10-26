from .widget import Widget
import flet


class Title(Widget):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.flet_object = flet.Text("")

        self.data = {
            "widget_name": "Title"
        }
    
    def update_flet_object(self):
        super().update_flet_object()

        properties = self.data['properties']
        text = properties['text']
        color = properties['color']
        size = properties['size']

        self.flet_object.value = str(text)
        self.flet_object.color = str(color)
        self.flet_object.size = int(size)

        if self.flet_object.page != None:
            self.flet_object.update()
    

    def properties_data(self):
        return {
            "text" : {"type":"str", "default_value":"Hello, fletsb!"},
            "color" : {"type": "color", "default_value":"white"},
            "size": {"type":"int", "default_value":18}
        }