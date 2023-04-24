import flet
import threading
from ...Tools.color_picker import colorPicker
from ...Tools.list_picker import ListPopup

class Open_Url (object):
    def __init__(self, main_class, parent, *args, **kwrds) -> None:
        self.parent = parent
        self.main_class = main_class
        self.self_object = flet.Container(on_click=self.open_url)
        self.url_text = flet.Text()
        self.url_icon = flet.Icon(size=12)
        self.self_object.content = flet.Row([self.url_icon, self.url_text], alignment="center")

        #? all args
        all_icons = []
        for icon in flet.icons.__dict__:
            name = str(icon)
            if name.startswith("__"): pass
            else:
                all_icons.append(name)
        self.args = {
            "text" : {"type":str, "default_value":"example url"},
            "url" : {"type":str, "default_value":"https://example.com"},
            "link icon" : {"type":ListPopup, "options":all_icons, "default_value":"INSERT_LINK_OUTLINED"},
            "text_color" : {"type":colorPicker, "default_value":"blue"},
            "icon_color" : {"type":colorPicker, "default_value":"blue"},
            "bgcolor" : {"type":colorPicker, "default_value":"black"},
            "alignment" : {"type":list, "options":["left", "center", "right"], "default_value":"center"},
            "width" : {"type":int, "default_value":130},
            "height" : {"type":int, "default_value":30},
            "text_size" : {"type":int, "default_value":15},
            "icon_size" : {"type":int, "default_value":15},
            "border_radius" : {"type":int, "default_value":10},
            "hide" : {"type":bool, "default_value":False}
        }

        #? Template dict
        #* This is where the widget data will be stored.
        self.template = {
            "widget_class_name" : "Open Url",
            "properties" : {}
        }
        for p in self.args:
            self.template["properties"][p] = self.args[p]["default_value"]
        
        self.update()

    
    def update (self, new_props:dict=None):
        c = self.self_object
        t = self.url_text
        ii = self.url_icon
        props = self.template["properties"]
        
        if new_props != None:
            for i in new_props:
                self.template["properties"][i] = new_props[i]


        url = props["url"]
        c.tooltip = f"open '{url}'"
        c.width = props["width"]
        c.bgcolor = props["bgcolor"]
        c.border_radius = props["border_radius"]
        c.height = props["height"]
        c.visible = props["hide"] == False

        t.value = props["text"]
        t.color = props["text_color"]
        t.text_align = props["text_color"]
        t.size = props["text_size"]

        ii.name = props["link icon"]
        ii.color = props["icon_color"]
        ii.size = props["icon_size"]
        if self.self_object.page != None:
            self.self_object.update()
        

    def open_url (self, event):
        if self.main_class.development_mode: return
        url = self.template["properties"]["url"]
        event.control.page.launch_url(url)

    def return_widget (self):
        props = self.template["properties"]
        if props["alignment"] == "left":
            return flet.Row([flet.Text("   "), self.self_object])
        elif props["alignment"] == "center":
            return flet.Row([self.self_object], alignment="center")
        else:
            return flet.Row([self.self_object, flet.Text("    ")], alignment="right")