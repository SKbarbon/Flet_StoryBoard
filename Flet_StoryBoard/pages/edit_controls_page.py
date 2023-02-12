from flet import *
from ..widgets.color_picker import ColorPicker
import flet
import random
import time


def Edit_Controls_Page(self_class, built_in_widgets, its_new=True, number_on_list=0, class_type=None):
    def SAVE_ALL(me):
        self_class.storyboard_json['controls']
        #? if add to the last.
        new_data = {
            f"{class_type}" : {
                "on_row_center" : True,
                "properties" : {
                    
                }
            }
        }
        for controler in GET_CONTROL_EDIT_CONTROLERS['properties']:
            saved = data_saver[f"{controler}"]
            if type(saved) != type(ColorPicker()):
                new_data[f"{class_type}"]['properties'].update({f"{controler}":saved.value})
            else:
                new_data[f"{class_type}"]['properties'].update({f"{controler}":saved.selected_color})
        
        if "multi_select-prop" in GET_CONTROL_EDIT_CONTROLERS:
            for i in GET_CONTROL_EDIT_CONTROLERS['multi_select-prop']:
                new_data[f"{class_type}"]['properties'].update({f"{i}":saved.value})
        
        if "on_click_support" in GET_CONTROL_EDIT_CONTROLERS:
            new_data[f"{class_type}"]["on_click_function"] = {"attr_name" : str(data_saver["on_click_function"].label), "function_name" : str(data_saver["on_click_function"].value)}


        if int(arrangement_set.value) >= len(self_class.storyboard_json['controls']):
            self_class.storyboard_json['controls'].append(new_data)
        else:
            self_class.storyboard_json['controls'][int(arrangement_set.value)] = new_data
        
        self_class.update_preview()
        Edit_Controls_Page(self_class, built_in_widgets, its_new=False, number_on_list=int(arrangement_set.value), class_type=class_type)

    def DELETE_THIS(me):
        del self_class.storyboard_json['controls'][number_on_list]
        edit_control_section.clean()
        self_class.update_preview()
    
    #! SET DATA
    standerd_width = 210
    font_sizes = 15

    if its_new == False: control_info = self_class.storyboard_json['controls'][number_on_list][f'{class_type}']
    if its_new: number_on_list = len(self_class.storyboard_json['controls'])
    edit_control_section = self_class.ewp
    GET_CONTROL_EDIT_CONTROLERS = built_in_widgets[class_type]
    data_saver = {}
    #! UI GENERATE
    edit_control_section.clean()

    main_title = Text(f"  Edit {class_type}", weight="bold", size=18, color="black")
    edit_control_section.controls.append(main_title)
    edit_control_section.controls.append(Row([Divider()], alignment="center"))

    for controler in GET_CONTROL_EDIT_CONTROLERS['properties']:
        value_ = GET_CONTROL_EDIT_CONTROLERS['properties'][controler]
        
        #? If the controler need a string value.
        if type(value_()) == type(str()):
            Title = Text(f"{controler}", color="black", size=font_sizes, width=standerd_width)
            if its_new:
                Index = TextField(value="", color="black", width=standerd_width, height=60)
            else:
                Index = TextField(value=control_info['properties'][str(controler)], color="black", width=standerd_width, height=60)
            data_saver.update({f"{controler}":Index})
            edit_control_section.controls.append(Row([Title], alignment="center"))
            edit_control_section.controls.append(Row([Index], alignment="center"))
        
        #? If the controler need a number value.
        elif type(value_()) == type(int()):
            Title = Text(f"{controler}", color="black", size=font_sizes, width=standerd_width/2-40)
            if its_new:
                Index = TextField(value="15", color="black", width=standerd_width/2, height=60, keyboard_type=flet.KeyboardType.NUMBER)
            else:
                Index = TextField(value=control_info['properties'][str(controler)], color="black", width=standerd_width/2, height=60, keyboard_type=flet.KeyboardType.NUMBER)
            data_saver.update({f"{controler}":Index})
            edit_control_section.controls.append(Row([Title, Index], alignment="center"))
        
        #? If the controler need a bool value.
        elif type(value_()) == type(bool()):
            Title = Text(f"{controler}", color="black", size=font_sizes, width=standerd_width/2+20)
            if its_new:
                if str(controler) == "visible": Index = Switch(width=standerd_width/2-30, value=True)
                else: Index = Switch(width=standerd_width/2-30)
            else:
                Index = Switch(width=standerd_width/2-30, value=control_info['properties'][str(controler)])
            data_saver.update({f"{controler}":Index})
            edit_control_section.controls.append(Row([Title, Index], alignment="center"))
        
        #? if its a color picker.
        elif type(value_()) == type(ColorPicker()):
            
            if its_new:
                Index = ColorPicker(label=f"{controler}")
            else:
                Index = ColorPicker(label=f"{controler}", selected_color=control_info['properties'][str(controler)])
            data_saver.update({f"{controler}":Index})
            edit_control_section.controls.append(Index.ui_self)
        
    
    #? if multi-touch is exist.
    if "multi_select-prop" in GET_CONTROL_EDIT_CONTROLERS:
        for msp in GET_CONTROL_EDIT_CONTROLERS['multi_select-prop']:
            Index = Dropdown(
                width=standerd_width-5,
                label=f"{msp}",
                color="black",
                bgcolor="white"
            )
            for i in GET_CONTROL_EDIT_CONTROLERS['multi_select-prop'][str(msp)]:
                Index.options.append(flet.dropdown.Option(f"{i}"))
                Index.value = random.choice(GET_CONTROL_EDIT_CONTROLERS['multi_select-prop'][str(msp)])
            if its_new == False:
                Index.value = control_info['properties'][str(msp)]
            edit_control_section.controls.append(Row([Index], alignment="center"))
            data_saver.update({f"{msp}":Index})
    
    #? if the control support functions.
    if "on_click_support" in GET_CONTROL_EDIT_CONTROLERS:
        Index = Dropdown(
            label=GET_CONTROL_EDIT_CONTROLERS["on_click_support"],
            width=standerd_width,
            value="none"
        )
        if its_new: Index.value = "none"
        else:
            Index.value = control_info["on_click_function"]["function_name"]
        d = flet.dropdown.Option("none")
        Index.options.append(d)
        for i in self_class.functions:
            d = flet.dropdown.Option(i)
            Index.options.append(d)
        edit_control_section.controls.append(Row([Index], alignment="center"))
        data_saver.update({f"on_click_function":Index})
    
    #! arrangement set
    arrangement_set = Dropdown(
        width=standerd_width-20,
        label="arrangement",
        color="black"
    )
    for I in range(len(self_class.storyboard_json['controls'])+1):
        arrangement_set.options.append(flet.dropdown.Option(f"{I}"))
    arrangement_set.value = f"{len(self_class.storyboard_json['controls'])}"

    if its_new == False:
        arrangement_set.value = str(number_on_list)

    edit_control_section.controls.append(Row([arrangement_set], alignment="center"))

    edit_control_section.controls.append(Row([Divider()], alignment="center"))

    Done_Btn = ElevatedButton("Done!", color="white", bgcolor="black", on_click=SAVE_ALL)
    edit_control_section.controls.append(Row([Done_Btn], alignment="center"))

    if its_new == False:
        delete_btn = TextButton(content=Text("delete", color="red"), on_click=DELETE_THIS)
        edit_control_section.controls.append(Row([delete_btn], alignment="center"))
    
    edit_control_section.controls.append(Row([Divider()], alignment="center"))

    edit_control_section.update()