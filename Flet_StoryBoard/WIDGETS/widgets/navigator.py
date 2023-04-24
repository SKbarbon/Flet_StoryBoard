import flet
from ...Tools.color_picker import colorPicker


class Navigator (object):
    def __init__(self, main_class, parent, *args, **kwrds) -> None:
        self.parent = parent
        self.main_class = main_class
        self.self_object = flet.ElevatedButton(on_click=self.on_button_click)

        #? all args
        all_pages = []
        for i in self.main_class.dict_content["pages"]:
            all_pages.append(i)
        self.args = {
            "text" : {"type":str, "default_value":"click me"},
            "page name" : {"type":list, "options":all_pages, "default_value":"main"},
            "width" : {"type":int, "default_value":150},
            "height" : {"type":int, "default_value":45},
            "alignment" : {"type":list, "options":["left", "center", "right"], "default_value":"center"},
            "bgcolor" : {"type":colorPicker, "default_value":"black"},
            "text_color" : {"type":colorPicker, "default_value":"blue"}
        }

        #? Template dict
        #* This is where the widget data will be stored.
        self.template = {
            "widget_class_name" : "Navigator",
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
        

        t.text = props["text"]
        t.color = props["text_color"]
        t.bgcolor = props["bgcolor"]
        t.width = props["width"]
        t.height = props["height"]
        
        if self.self_object.page != None:
            self.self_object.update()

    
    def on_button_click (self, event):
        if self.main_class.development_mode:
            return
        else:
            props = self.template["properties"]
            self.main_class.storyboard_class.navigate_to_page(props["page name"])
    

    def return_widget (self):
        props = self.template["properties"]
        if self.main_class.development_mode == True: self.self_object.disabled = True
        if props["alignment"] == "left":
            return flet.Row([flet.Text("    "), self.self_object])
        elif props["alignment"] == "center":
            return flet.Row([self.self_object], alignment="center")
        else:
            return flet.Row([self.self_object, flet.Text("    ")], alignment=flet.alignment.center_right)