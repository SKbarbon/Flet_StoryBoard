from .widget import Widget
import flet



class RouteButton (Widget):
    def __init__ (self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.flet_object = flet.ElevatedButton(on_click=self.on_clicked)
        self.data['widget_name'] = "RouteButton"
        self.data['events'] = ["on_navigate"]
    

    def on_clicked (self, e):
        """This function will be used to navigate and call the event"""
        storyboard_class = self.storyboard_class
        
        properties = self.data['properties']
        target_page : str = properties['target_page']

        storyboard_class.navigate_to_page_name(page_name=target_page)
    

    def update_flet_object(self):
        super().update_flet_object()

        properties = self.data['properties']


        text : str = properties['text']
        target_page : str = properties['target_page']
        color : str = properties['color']
        bgcolor : str = properties['bgcolor']
        autofocus : bool = properties['autofocus']
        fixed_size : bool = properties['fixed_size']
        width  : int = properties['width']
        height : int = properties['height']

        self.flet_object.text = text
        self.flet_object.color = color
        self.flet_object.autofocus = autofocus
        self.flet_object.bgcolor = bgcolor

        if fixed_size:
            self.flet_object.width = width
            self.flet_object.height = height
        else:
            self.flet_object.width = None
            self.flet_object.height = None
        
        if self.flet_object.page != None:
            self.flet_object.update()
    

    def properties_data(self):
        return {
            "text" : {"type":"str", "default_value":"Hello, fletsb!"},
            "target_page": {"type": "list", "options": self.storyboard_class.availble_pages, "default_value": "main"},
            "color" : {"type": "color", "default_value":"white"},
            "bgcolor" : {"type": "color", "default_value":"blue"},

            "autofocus": {"type": "bool", "default_value": False},
            "fixed_size": {"type": "bool", "default_value": False},

            "width": {"type": "int", "default_value": 100},
            "height": {"type": "int", "default_value": 40}
        }