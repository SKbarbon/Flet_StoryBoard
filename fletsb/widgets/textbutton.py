from .widget import Widget
import flet




class TextButton (Widget):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.flet_object = flet.TextButton(
            on_click=lambda e: self.on_button_event("on_click"),
            on_hover=lambda e: self.on_button_event("on_hover"),
            on_long_press=lambda e: self.on_button_event("on_long_press")
        )
        self.data['widget_name'] = "TextButton"
        self.availble_events = ["on_click", "on_hover", "on_long_press"]
        for ae in self.availble_events:
            self.data['events'][f'{ae}'] = None
    
    def on_button_event (self, event_name:str):
        if self.storyboard_class.development_mode:
            pass
        else:
            if not event_name in self.data['events']: return

            function_name_of_event = self.data['events'][event_name]
            if function_name_of_event == None: return

            if function_name_of_event in self.storyboard_class.defined_functions:
                self.storyboard_class.defined_functions[function_name_of_event]()
            else:
                print(f"No defined function named '{function_name_of_event}'")


    def update_flet_object(self):
        super().update_flet_object()

        properties = self.data['properties']
        text = properties['text']
        tooltip = properties['tooltip']

        self.flet_object.text = str(text)
        self.flet_object.tooltip = str(tooltip)

        if self.flet_object.page != None:
            self.flet_object.update()
    

    def properties_data(self):
        return {
            "text" : {"type":"str", "default_value":"Hello, fletsb!"},
            "tooltip" : {"type":"str", "default_value":"This is a clickable button!"}
        }