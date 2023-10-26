from fletsb import tools
import flet


class Widget:
    def __init__(self, storyboard_class) -> None:
        self.flet_object = flet.Text("EMPTY WIDGET", color="red")
        self.storyboard_class = storyboard_class

        self.data = {
            "widget_name" : "",
            "widget_identifier_name" : "",
            "properties" : {},
            "content" : None,
            "controls" : None
        }


        # subs
        self.controls = []
        self.content = None
    


    def update_flet_object (self):
        # Update the sub-controls or sub-content of this widget.
        if self.data['controls'] != None:
            self.flet_object.controls.clear()
            for c in self.controls:
                self.flet_object.controls.append(c.flet_object)
        elif self.data['content'] != None:
            self.flet_object.content = self.content
        
        if self.flet_object.page != None:
            self.flet_object.update()
    

    def edit_props_from_dict (self, new_data:dict):
        for i in new_data:
            if i in self.data['properties']:
                self.data['properties'][i] = new_data[i]
    

    def update_subs (self):
        """Update the `self.data` (The dict of the widget) and update it with new sub controls and content updates"""
        if self.data['controls'] != None:
            self.generate_sub_widgets()
            for c in self.controls:
                c.update_subs()
            self.data['controls'] = []
            for cd in self.controls:
                self.data['controls'].append(cd.data)
        
        if self.data['content'] != None:
            self.content.update_subs()
            self.data['content'] = self.content
    


    def generate_sub_widgets (self):
        self.controls.clear()
        self.flet_object.controls.clear()
        for c in self.data['controls']:
            wc = tools.get_widget_class_by_name(widget_name=c['widget_name'])
            wc = wc(storyboard_class=self.storyboard_class)
            wc.data = c
            self.controls.append(wc)
            self.flet_object.controls.append(wc.flet_object)

            wc.update_subs()
            wc.update_flet_object()
        
        if self.flet_object.page != None:
            self.flet_object.update()


    def properties_data(self):
        return {
            
        }