from .widget import Widget
import flet



class Paragraph (Widget):
    def __init__(self, storyboard_class) -> None:
        super().__init__(storyboard_class)

        self.flet_object = flet.Text("")

        self.data['widget_name'] = "Paragraph"
    

    def update_flet_object(self):
        super().update_flet_object()

        properties = self.data['properties']
        text = properties['text']
        color = properties['color']
        size = properties['size']
        text_align = properties['text_align']

        self.flet_object.value = str(text)
        self.flet_object.color = str(color)
        self.flet_object.size = int(size)
        self.flet_object.text_align = str(text_align)

        if self.flet_object.page != None:
            self.flet_object.update()
    

    def properties_data(self):
        return {
            "text" : {"type":"str", "default_value":"Hello, fletsb!\nThis is a paragraph!!"},
            "color" : {"type": "color", "default_value":"white"},
            "size": {"type":"int", "default_value":15},
            "text_align": {"type":"list", "options":["left", "center", "right"], "default_value": "left"}
        }