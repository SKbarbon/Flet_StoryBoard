import flet
from ...Tools.color_picker import colorPicker

class Padding (object):
    def __init__(self, main_class, parent, *args, **kwrds) -> None:
        self.parent = parent
        self.main_class = main_class
        self.self_object = flet.Text("")


        #? all args
        self.args = {
            "width" : {"type":int, "default_value":50},
            "height" : {"type":int, "default_value":50},
            "alignment" : {"type":list, "options":["left", "center", "right"], "default_value":"center"}
        }

        #? Template dict
        #* This is where the widget data will be stored.
        self.template = {
            "widget_class_name" : "Padding",
            "properties" : {}
        }
        for p in self.args:
            self.template["properties"][p] = self.args[p]["default_value"]
        
        self.update()

    
    def update (self, new_props:dict=None):
        p = self.self_object
        props = self.template["properties"]
        
        if new_props != None:
            for i in new_props:
                self.template["properties"][i] = new_props[i]

        p.width = props["width"]
        p.height = props["height"]
        
        if self.self_object.page != None:
            self.self_object.update()
        

    def return_widget (self):
        props = self.template["properties"]
        if props["alignment"] == "left":
            return flet.Row([flet.Text("    "), self.self_object])
        elif props["alignment"] == "center":
            return flet.Row([self.self_object], alignment="center")
        else:
            return flet.Row([self.self_object, flet.Text("    ")], alignment=flet.alignment.center_right)