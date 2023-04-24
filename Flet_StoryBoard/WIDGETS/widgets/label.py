import flet
from ...Tools.color_picker import colorPicker
from ...Tools.list_picker import ListPopup


class Label (object):
    def __init__(self, main_class, parent, *args, **kwrds) -> None:
        self.parent = parent
        self.main_class = main_class
        self.self_object = flet.Row()
        self.title_object = flet.Text()
        self.icon_object = flet.Icon()

        self.self_object.controls.append(self.icon_object)
        self.self_object.controls.append(self.title_object)

        #? all args
        all_icons = []
        for icon in flet.icons.__dict__:
            name = str(icon)
            if name.startswith("__"): pass
            else:
                all_icons.append(name)
        self.args = {
            "title" : {"type":str, "default_value":"Just me and coffee"},
            "icon" : {"type":ListPopup, "options":all_icons, "default_value":"EMOJI_FOOD_BEVERAGE_ROUNDED"},
            "title_color" : {"type":colorPicker, "default_value":"white"},
            "icon_color" : {"type":colorPicker, "default_value":"white"},
            "title_size" : {"type":int, "default_value":18},
            "icon_size" : {"type":int, "default_value":18},
            "spacing" : {"type":int, "default_value":15},
            "title_bold" : {"type":int, "default_value":True},
            "alignment" : {"type":list, "options":["left", "center", "right"], "default_value":"center"}
        }

        #? Template dict
        #* This is where the widget data will be stored.
        self.template = {
            "widget_class_name" : "Label",
            "properties" : {}
        }
        for p in self.args:
            self.template["properties"][p] = self.args[p]["default_value"]
        
        self.update()

    
    def update (self, new_props:dict=None):
        r = self.self_object
        t = self.title_object
        I = self.icon_object
        props = self.template["properties"]
        
        if new_props != None:
            for i in new_props:
                self.template["properties"][i] = new_props[i]

        r.spacing = props["spacing"]

        t.value = props["title"]
        t.color = props["title_color"]
        t.size = props["title_size"]
        if props["title_bold"]:
            t.weight = "bold"
        else:
            t.weight = "normal"
        
        I.name = props["icon"]
        I.color = props["icon_color"]
        I.size = props["icon_size"]
        
        
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