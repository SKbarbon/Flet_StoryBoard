import flet
from ...Tools.color_picker import colorPicker

class Title (object):
    def __init__(self, main_class, parent, *args, **kwrds) -> None:
        self.parent = parent
        self.main_class = main_class
        self.self_object = flet.Text("")


        #? all args
        self.args = {
            "title" : {"type":str, "default_value":"myTitle"},
            "title_color" : {"type":colorPicker, "default_value":"white"},
            "size" : {"type":int, "default_value":23},
            "width" : {"type":int, "default_value":350},
            "italic" : {"type":bool, "default_value":False},
            "bold" : {"type":bool, "default_value":True},
            "hide" : {"type":bool, "default_value":False},
            "expand" : {"type":bool, "default_value":False},
            "alignment" : {"type":list, "options":["left", "center", "right"], "default_value":"center"},
            "text_align" : {"type":list, "options":["left", "center", "right"], "default_value" : "left"}
        }

        #? Template dict
        #* This is where the widget data will be stored.
        self.template = {
            "widget_class_name" : "Title",
            "properties" : {}
        }
        for p in self.args:
            self.template["properties"][p] = self.args[p]["default_value"]
        
        self.update()

    
    def update (self, new_props:dict=None):
        t = self.self_object
        props = self.template["properties"]
        
        if new_props != None:
            for i in new_props:
                self.template["properties"][i] = new_props[i]

        t.value = props["title"]
        t.size = props["size"]
        t.color = props["title_color"]
        t.width = props["width"]
        t.expand = props["expand"]
        t.italic = props["italic"]
        t.visible = props["hide"] == False
        if str(props["text_align"]).lower() == "left":
            t.text_align = flet.TextAlign.LEFT
        elif str(props["text_align"]).lower() == "center":
            t.text_align = flet.TextAlign.CENTER
        elif str(props["text_align"]).lower() == "right":
            t.text_align = flet.TextAlign.RIGHT
        if props["bold"] == True:
            t.weight = "bold"
        else:
            t.weight = "normal"
        
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