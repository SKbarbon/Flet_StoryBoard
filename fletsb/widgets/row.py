from .widget import Widget
import flet



class Row (Widget):
    def __init__ (self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.flet_object = flet.Row()
        self.flet_empty_placeholder_object = flet.Text("Empty Row")

        self.data['widget_name'] = "Row"
    
        self.data['controls'] = []
        self.controls = []
    

    def update_flet_object(self):
        super().update_flet_object()
        if self.data['controls'] == []:
            self.flet_object.controls.append(self.flet_empty_placeholder_object)
        else:
            if self.flet_empty_placeholder_object in self.flet_object.controls:
                self.flet_object.controls.remove(self.flet_empty_placeholder_object)

        properties = self.data['properties']

        alignment = properties['alignment']
        spacing = properties['spacing']

        self.flet_object.alignment = str(alignment)
        self.flet_object.spacing = int(spacing)

        if self.flet_object.page != None:
            self.flet_object.update()
    

    def properties_data(self):
        return {
            "alignment": {"type":"list", "options":["left", "center", "end"], "default_value":"left"},
            "spacing": {"type":"int", "default_value":5}
        }