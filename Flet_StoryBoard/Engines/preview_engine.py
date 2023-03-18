from ..tools.all_controls import get_all_supported_controls
import flet
import os
import json



class previewEngine :

    def __init__ (self, main_class, mainview=None, development=True, file_path="", bgview=None, functions={}):
        self.main_class = main_class
        self.development = development
        self.functions = functions
        
        if mainview == None:
            if os.path.isfile(file_path) == False:
                raise OSError(f"cannot find storyboard with name '{file_path}'")
            file_as_dict = json.loads(open(file_path, encoding="utf-8").read())
        else:
            file_as_dict = main_class.file_as_dict
        self.file_as_dict = file_as_dict
        self.page_info = file_as_dict["page_settings"]
        self.controls = file_as_dict["controls"]
        self.mainview = mainview
        self.bgview=bgview

        if mainview == None:
            self.loader()
        else:
            self.update()
    

    def update (self):
        self.page_info = self.file_as_dict["page_settings"]
        self.controls = self.file_as_dict["controls"]

        if self.mainview == None:
            mainview : flet.Page = self.page
            mainview.auto_scroll = self.page_info["auto_scroll"]
            mainview.clean()
            mainview.scroll = self.page_info["scroll"]
            mainview.title = self.page_info["title"]
            mainview.window_width = self.page_info["width"]
            mainview.window_height = self.page_info["height"]
            mainview.window_full_screen = self.page_info["auto_fullscreen"]
            mainview.window_resizable = self.page_info["allow_resize"]
            mainview.bgcolor = self.page_info["bgcolor"]
            if self.page_info["center_all"]:
                mainview.vertical_alignment = flet.MainAxisAlignment.CENTER
            mainview.update()
        else:
            mainview : flet.Column = self.mainview
            mainview.auto_scroll = self.page_info["auto_scroll"]
            mainview.scroll = self.page_info["scroll"]
            self.bgview.bgcolor = self.page_info["bgcolor"]
            if mainview.page != None: mainview.clean()

        # generate_elements
        num = 0
        for control in self.controls:
            if control["kind"] == "control":
                new_con = self.generate_control(control, num)
                mainview.controls.append(new_con)
            num = num + 1
        
        if isinstance(mainview, flet.Page) == False:
            if mainview.page != None:
                mainview.update()
        

    def loader (self):
        def main (page:flet.Page):
            self.page = page
            self.development = False
            self.update()
            page.update()
        flet.app(target=main)
    
    def generate_control (self, control_dict, number_on_list):
        def on_action (control, action_name, actions_dict):
            def DoThis (me):
                if action_name in actions_dict:
                    if actions_dict[action_name] in self.functions:
                        self.functions[actions_dict[action_name]]()
                    else:
                        print(f"Pass Exception: there is no function called '{actions_dict[action_name]}' that givin.")
                else:
                    pass
            setattr(control, action_name, DoThis)
            

        def edit_now (me):
            self.main_class.on_start_edit_control(control_dict["class"], False, number_on_list)
        # ---
        if self.mainview == None: self.development = False
        control_class = get_all_supported_controls()[control_dict["class"]]["class"]
        control = control_class()
        for i in control_dict["properties"]:
            if hasattr(control, i):
                setattr(control, i, control_dict["properties"][i])
        if "functions" in control_dict:
            if self.development == False:
                for i in control_dict["functions"]:
                    
                    if str(control_dict["functions"][i]) == "": pass
                    else:
                        if hasattr(control, i):
                            on_action(control, i, control_dict["functions"])
        
        #! -- for support sub-controls
        if "support_controls" in get_all_supported_controls()[control_dict["class"]]:
            self.development = False
            num = 0
            for i in control_dict["controls"]:
                s_control = self.generate_control(i, num)
                control.controls.append(s_control)
                num = num + 1
            if self.mainview != None: self.development = True
        #!! -- for support sub-controls
        
        if self.development == True:
            if "expand" in control_dict["properties"]:
                if control_dict["properties"]["expand"] == True:
                    contain = flet.Container(content=control, tooltip="click to edit!", on_click=edit_now, expand=True)
                    return contain
                else:
                    contain = flet.Container(content=control, tooltip="click to edit!", on_click=edit_now)
                    return contain
            else:
                contain = flet.Container(content=control, tooltip="click to edit!", on_click=edit_now)
                return contain
        else:
            return control