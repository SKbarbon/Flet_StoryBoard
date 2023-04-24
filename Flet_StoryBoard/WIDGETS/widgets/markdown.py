import flet
from ...Tools.color_picker import colorPicker

class Markdown (object):
    def __init__(self, main_class, parent, *args, **kwrds) -> None:
        self.parent = parent
        self.main_class = main_class
        self.self_object = flet.Markdown(selectable=True, extension_set="gitHubWeb", 
        code_style=flet.TextStyle(font_family="Roboto Mono", color="blue"))

        #? all args
        self.args = {
            "content" : {"type":str, "default_value":"", "multi_line":True},
            "code_theme" : {"type":list, "options":["a11y-dark", "arta", "atom-one-dark", "dark", "default"], "default_value":"default"},
            "width" : {"type":int, "default_value":150},
            "height" : {"type":int, "default_value":150},
            "alignment" : {"type":list, "options":["left", "center", "right"], "default_value":"left"}
        }

        #? Template dict
        #* This is where the widget data will be stored.
        self.template = {
            "widget_class_name" : "Markdown",
            "properties" : {}
        }
        for p in self.args:
            self.template["properties"][p] = self.args[p]["default_value"]
        
        self.update()

    
    def update (self, new_props:dict=None):
        m = self.self_object
        props = self.template["properties"]
        
        if new_props != None:
            for i in new_props:
                self.template["properties"][i] = new_props[i]

        
        m.value = props["content"]
        m.width = props["width"]
        m.height = props["height"]
        
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