import flet

# local imports
from ..tools.all_controls import get_all_supported_controls
from ..built_in_widgets.color_picker import colorPicker
from ..ui_set.pick_control_section import pickControlSection


class editControlEngine:

    def __init__(self, main_class, mainview, is_new, type, number_on_list=0) -> None:
        mainview.clean()
        self.mainview = mainview
        self.main_class = main_class
        self.is_new = is_new
        self.type = type
        self.number_on_list = number_on_list

        Title = flet.Text(f"Edit {type}", size=21, weight="bold", color="white")
        mainview.controls.append(Title)
        mainview.controls.append(flet.Text("\n"))

        self.build_the_edit_section()
    
    def build_the_edit_section (self):
        default_properties = get_all_supported_controls()[self.type]["properties"]
        self.all_inputs = {}

        for i in default_properties:
            prop_type = default_properties[i]["type"]
            prop_default_value = default_properties[i]["default"]

            if type(prop_type()) == type(str()):
                tf = flet.TextField(color="white", width=180, label=i, value=prop_default_value, border_color="white")
                self.all_inputs.update({f"{i}":tf})
                self.mainview.controls.append(flet.Row([tf], alignment="center"))
            elif type(prop_type()) == type(int()):
                sl = flet.Slider(min=0, max=250, divisions=250, label="{value}%", width=180, value=prop_default_value, thumb_color="white")
                self.all_inputs.update({f"{i}":sl})
                self.mainview.controls.append(flet.Row([flet.Text(f"{i}", size=12, width=180, color="white")], alignment="center"))
                self.mainview.controls.append(flet.Row([sl], alignment="center"))
            elif type(prop_type()) == type(bool()):
                sw = flet.Switch(width=80, value=prop_default_value)
                self.all_inputs.update({f"{i}":sw})
                self.mainview.controls.append(flet.Row([flet.Text(f"{i}", size=12, width=100, color="white"), sw], alignment="center"))
            
            elif type(prop_type()) == type(list()):
                dr = flet.Dropdown(label=i, width=180, focused_color="white", focused_border_color="white")
                self.all_inputs.update({f"{i}":dr})
                for i in default_properties[i]["selections"]:
                    dr.options.append(flet.dropdown.Option(i))
                dr.value = prop_default_value
                self.mainview.controls.append(flet.Row([dr], alignment="center"))
            
            elif type(prop_type()) == type(colorPicker()):
                if self.is_new:
                    cp = colorPicker(self.mainview, title_name=f"{i}", drop_width=120, color_prev_width=60, add_it=False, selected_color=prop_default_value)
                else:
                    The_Control_Info = self.main_class.file_as_dict["controls"][self.number_on_list]
                    all_prop = The_Control_Info["properties"]
                    cp = colorPicker(self.mainview, title_name=f"{i}", drop_width=120, color_prev_width=60, add_it=False, selected_color=all_prop[i])
                self.all_inputs.update({f"{i}":cp})
                self.mainview.controls.append(flet.Row([cp.v], alignment="center"))
            
        
        self.all_functions = {}
        if "support_functions" in get_all_supported_controls()[self.type]:
            for i in get_all_supported_controls()[self.type]["support_functions"]:
                tf = flet.TextField(label=f"{i}", width=180, color="white", border_color="white")
                self.all_functions.update({f"{i}":tf})
                self.mainview.controls.append(flet.Row([tf], alignment="center"))
        
        if "support_controls" in get_all_supported_controls()[self.type]:
            add_content_button = flet.Container(content=flet.Row([flet.Text("add control")], alignment="center"), bgcolor="white", 
            width=100, height=30, border_radius=8, on_click=self.add_sub_control)
            self.mainview.controls.append(flet.Text("\n"))
            self.mainview.controls.append(flet.Row([add_content_button], alignment="center"))
            

        #! To set the properties of a not-new control
        if self.is_new == False:
            The_Control_Info = self.main_class.file_as_dict["controls"][self.number_on_list]
            all_prop = The_Control_Info["properties"]
            for i in self.all_inputs:
                if i in all_prop:
                    if type(self.all_inputs[i]) != type(colorPicker()):
                        self.all_inputs[i].value = all_prop[i]
                    elif type(self.all_inputs[i]) == type(colorPicker()):
                        self.all_inputs[i].selected_color = all_prop[i]
            if "support_functions" in get_all_supported_controls()[self.type]:
                for i in The_Control_Info["functions"]:
                    if i in self.all_functions:
                        self.all_functions[i].value = The_Control_Info["functions"][i]
        
        #? extra elements
        self.mainview.controls.append(flet.Row([flet.Divider()], width=180, alignment="center"))

        reArrange = flet.Slider(min=0, max=len(self.main_class.file_as_dict["controls"]), divisions=len(self.main_class.file_as_dict["controls"]), 
        width=180, thumb_color="white", label="{value}%")
        self.reArrange = reArrange
        if self.is_new:
            reArrange.value = len(self.main_class.file_as_dict["controls"])
        else:
            reArrange.value = self.number_on_list
        self.mainview.controls.append(flet.Row([flet.Text("reArrange", width=180, color="white")], alignment="center"))
        self.mainview.controls.append(flet.Row([reArrange], alignment="center"))

        save_button = flet.Container(content=flet.Row([flet.Text("Done Edit", size=13, color="black")], alignment="center"),
        bgcolor="white", width=180, height=40, on_click=self.done_edit, border_radius=8)
        self.mainview.controls.append(flet.Row([save_button], alignment="center"))

        if self.is_new == False:
            delete_btn = flet.TextButton(content=flet.Text("delete", color="red", size=13), on_click=self.delete)
            self.mainview.controls.append(flet.Row([delete_btn], alignment="center"))
            

    def done_edit (self, *args):
        edited_dict_data = {}
        
        for i in self.all_inputs:
            if type(self.all_inputs[i]) != type(colorPicker()):
                edited_dict_data.update({f"{i}":self.all_inputs[i].value})
            elif type(self.all_inputs[i]) == type(colorPicker()):
                edited_dict_data.update({f"{i}":self.all_inputs[i].selected_color})
        
        if self.is_new:
            edited_dict_data = {
                "class" : self.type,
                "kind" : "control",
                "properties" : edited_dict_data
            }
            if "support_functions" in get_all_supported_controls()[self.type]:
                edited_dict_data["functions"] = {}
                for i in get_all_supported_controls()[self.type]["support_functions"]:
                    edited_dict_data["functions"].update({f"{i}":""})
            if "support_controls" in get_all_supported_controls()[self.type]:
                edited_dict_data["controls"] = []
            self.number_on_list = len(self.main_class.file_as_dict["controls"])
            self.main_class.file_as_dict["controls"].append(edited_dict_data)
        else:
            edited_dict_data = {
                "class" : self.type,
                "kind" : "control",
                "properties" : edited_dict_data
            }
            if "support_functions" in get_all_supported_controls()[self.type]:
                edited_dict_data.update({"functions":self.main_class.file_as_dict["controls"][self.number_on_list]["functions"]})
                for i in self.all_functions:
                    edited_dict_data["functions"][i] = self.all_functions[i].value
            if "support_controls" in get_all_supported_controls()[self.type]:
                edited_dict_data.update({"controls":self.main_class.file_as_dict["controls"][self.number_on_list]["controls"]})
            self.main_class.file_as_dict["controls"][self.number_on_list] = edited_dict_data
        
        
        
        if int(self.reArrange.value) != self.number_on_list:
            if int(self.reArrange.value) >= len(self.main_class.file_as_dict["controls"]):
                self.main_class.file_as_dict["controls"].append(edited_dict_data)
                del self.main_class.file_as_dict["controls"][self.number_on_list]
            else:
                self.main_class.file_as_dict["controls"][int(self.reArrange.value)] = edited_dict_data
                del self.main_class.file_as_dict["controls"][self.number_on_list]

        self.mainview.clean()
        if int(self.reArrange.value) == len(self.main_class.file_as_dict["controls"]):
            self.reArrange.value = self.reArrange.value - 1
            self.reArrange.update()
        editControlEngine(self.main_class, self.mainview, False, self.type, int(self.reArrange.value))
        self.main_class.prev_engine.update()
        self.mainview.update()

    def delete (self, *args):
        del self.main_class.file_as_dict["controls"][self.number_on_list]
        self.main_class.prev_engine.update()
        self.mainview.clean()
        self.mainview.update()
    


    def add_sub_control (self, me):
        def on_pick_control(control_class_name, is_new, number_on_list):
            editSubContent(self.main_class, self.type, is_new, self.number_on_list, v, control_class_name, number_on_list)
        
        page : flet.Page = me.page
        
        if page.width < 800: v = flet.Column(width=page.width, height=page.height, scroll=True)
        else: v = flet.Column(width=page.width / 2, height=page.height, scroll=True)

        if self.is_new:
            v.controls.append(flet.Text("You need to add the the control to the page first", color="white"))
        else:
            pickControlSection(v, on_pick_control)
            
        
        page.dialog = flet.AlertDialog(
            content=flet.Container(content=v, bgcolor="black", border_radius=10)
        )

        page.dialog.open = True
        page.update()


#! For sub-content edit.
class editSubContent:

    def __init__(self, main_class, father_control_class_name, is_new, number_on_list, dialog_view, sub_control_class_name, sub_control_number_on_list) -> None:
        self.mainview = dialog_view
        self.main_class = main_class
        self.father_type = father_control_class_name
        self.father_number = number_on_list
        self.type = sub_control_class_name
        self.is_new = is_new
        self.build()
        self.mainview.update()
    
    def build (self):
        self.mainview.clean()
        Title = flet.Text(f"Edit {self.type}", size=21, weight="bold", color="white")
        self.mainview.controls.append(Title)
        default_properties = get_all_supported_controls()[self.type]["properties"]
        self.all_inputs = {}

        for i in default_properties:
            prop_type = default_properties[i]["type"]
            prop_default_value = default_properties[i]["default"]

            if type(prop_type()) == type(str()):
                tf = flet.TextField(color="white", width=180, label=i, value=prop_default_value, border_color="white")
                self.all_inputs.update({f"{i}":tf})
                self.mainview.controls.append(flet.Row([tf], alignment="center"))
            elif type(prop_type()) == type(int()):
                sl = flet.Slider(min=0, max=250, divisions=250, label="{value}%", width=180, value=prop_default_value, thumb_color="white")
                self.all_inputs.update({f"{i}":sl})
                self.mainview.controls.append(flet.Row([flet.Text(f"{i}", size=12, width=180, color="white")], alignment="center"))
                self.mainview.controls.append(flet.Row([sl], alignment="center"))
            elif type(prop_type()) == type(bool()):
                sw = flet.Switch(width=80, value=prop_default_value)
                self.all_inputs.update({f"{i}":sw})
                self.mainview.controls.append(flet.Row([flet.Text(f"{i}", size=12, width=100, color="white"), sw], alignment="center"))
            
            elif type(prop_type()) == type(list()):
                dr = flet.Dropdown(label=i, width=180, focused_color="white", focused_border_color="white")
                self.all_inputs.update({f"{i}":dr})
                for i in default_properties[i]["selections"]:
                    dr.options.append(flet.dropdown.Option(i))
                dr.value = prop_default_value
                self.mainview.controls.append(flet.Row([dr], alignment="center"))
            
            elif type(prop_type()) == type(colorPicker()):
                if self.is_new:
                    cp = colorPicker(self.mainview, title_name=f"{i}", drop_width=120, color_prev_width=60, add_it=False, selected_color=prop_default_value)
                else:
                    The_Control_Info = self.main_class.file_as_dict["controls"][self.number_on_list]
                    all_prop = The_Control_Info["properties"]
                    cp = colorPicker(self.mainview, title_name=f"{i}", drop_width=120, color_prev_width=60, add_it=False, selected_color=all_prop[i])
                self.all_inputs.update({f"{i}":cp})
                self.mainview.controls.append(flet.Row([cp.v], alignment="center"))
        

        save_button = flet.Container(content=flet.Row([flet.Text("Done Edit", size=13, color="black")], alignment="center"),
        bgcolor="white", width=180, height=40, on_click=self.done_edit, border_radius=8)
        self.mainview.controls.append(flet.Row([save_button], alignment="center"))
    
    def done_edit (self, me):
        control_info = get_all_supported_controls()[self.type]
        edited_dict_data = {}
        for i in self.all_inputs:
            if type(self.all_inputs[i]) != type(colorPicker()):
                edited_dict_data.update({f"{i}":self.all_inputs[i].value})
            elif type(self.all_inputs[i]) == type(colorPicker()):
                edited_dict_data.update({f"{i}":self.all_inputs[i].selected_color})
        
        edited_dict_data = {
            "class" : self.type,
            "kind" : "control",
            "properties" : edited_dict_data
        }
        if "support_controls" in control_info:
            edited_dict_data.update({"controls":[]})
            self.main_class.file_as_dict["controls"][self.father_number]["controls"].append(edited_dict_data)
        else:
            self.main_class.file_as_dict["controls"][self.father_number]["controls"].append(edited_dict_data)
        
        
        self.main_class.prev_engine.update()
        self.mainview.page.dialog.open = False
        self.mainview.page.update()