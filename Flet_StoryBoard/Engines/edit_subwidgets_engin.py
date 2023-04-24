import flet

from ..WIDGETS.All import all_widgets
from ..Tools.color_picker import colorPicker
from ..Tools.list_picker import ListPopup

# main_widget_mother_class: is the widgets mother like row or column.
class editSubWidgetsEngine:
    def __init__(self, main_class, main_widget_mother_class, section_view:flet.Column, widget_number) -> None:
        self.main_class = main_class
        self.main_widget_mother_class = main_widget_mother_class
        self.section_view = section_view
        self.widget_number = widget_number

        self.all_fields = {}
        
        self.show_edit_tools()
    
    def show_edit_tools (self):
        #? Update the viewerEngine.
        self.main_class.preview_section.update_preview(self.main_class.current_page_name)

        #? Start..
        self.section_view.clean()
        content = self.main_widget_mother_class.template["widgets"]
        class_name = content[self.widget_number]["widget_class_name"]
        widget_content = content[self.widget_number]

        if class_name not in all_widgets:
            #? if widget not found.
            self.section_view.controls.append(flet.Row([flet.Text(f"There is no supported\nwidget named '{class_name}'.", color="white")]))
            return
        
        the_class = all_widgets[class_name]["class"]
        the_class = the_class(self.main_class, self.main_widget_mother_class.preview_section, widget_number=self.widget_number)
        default_args = the_class.args
        
        title = flet.Text(f"Edit {class_name}", size=25, weight="bold", color="white")
        self.section_view.controls.append(title)

        for t in widget_content["properties"]:
            prop_name = t
            prop_value = widget_content["properties"][t]
            if prop_name not in default_args: print("Error while load widget properties in edit engine."); self.section_view.clean(); return
            prop_type = default_args[prop_name]["type"]
            
            #* This statments bellow is for adding the fields for edit a widget.
            if type(prop_type()) == type(str()):
                tf = flet.TextField(width=160, bgcolor="white", color="black", label=prop_name)
                tf.value = prop_value
                self.section_view.controls.append(flet.Row([tf], alignment="center"))
                self.all_fields[prop_name] = tf
                if "multi_line" in default_args[prop_name]:
                    tf.multiline = True
            elif type(prop_type()) == type(int()):
                slid = flet.Slider(min=0, max=500, divisions=500, label="{value}", width=160)
                slid.value = int(prop_value)
                self.section_view.controls.append(flet.Row([flet.Text(f"{prop_name}:", color="white", width=150)], alignment="center"))
                self.section_view.controls.append(flet.Row([slid], alignment="center"))
                self.all_fields[prop_name] = slid
            elif type(prop_type()) == type(bool()):
                tog = flet.Switch()
                tog.value = prop_value
                self.section_view.controls.append(flet.Row([flet.Text(f"{prop_name}",color="white", size=13), tog], alignment="center", spacing=25))
                self.all_fields[prop_name] = tog
            elif type(prop_type()) == type(colorPicker()):
                self.section_view.controls.append(flet.Text(""))
                colp = colorPicker(self.section_view, title_name=prop_name, drop_width=120, selected_color=prop_value, add_it=False)
                self.section_view.controls.append(flet.Row([colp.v], alignment="center"))
                self.all_fields[prop_name] = colp
            elif type(prop_type()) == type(list()):
                dr = flet.Dropdown(width=160, label=prop_name)
                for i in default_args[prop_name]["options"]:
                    dr.options.append(flet.dropdown.Option(f"{i}"))
                dr.value = prop_value
                self.section_view.controls.append(flet.Row([dr], alignment="center"))
                self.all_fields[prop_name] = dr
            elif type(prop_type()) == type(ListPopup()):
                lp = ListPopup(default_args[prop_name]["options"], self.main_class, prop_value, prop_name)
                self.section_view.controls.append(flet.Row([lp.self_ui], alignment="center"))
                self.all_fields[prop_name] = lp
        

        #* This button bellow for widgets that support sub-widgets.
        if hasattr(the_class, "support_sub_widgets"):
            add_sub_widget_button = flet.TextButton("Add sub-widget", on_click=the_class.widgets_to_add_in)
            self.section_view.controls.append(flet.Row([add_sub_widget_button], alignment="center"))

        

        #* This slider bellow is for rearrange the widget on the page.
        rearrange_slider = flet.Slider(min=0, max=len(content), 
        value=self.widget_number, label="{value}", width=160, divisions=len(content))
        self.section_view.controls.append(flet.Row([flet.Text(f"reArrange:", color="white", width=150)], alignment="center"))
        self.section_view.controls.append(flet.Row([rearrange_slider], alignment="center"))
        self.rearrange_slider = rearrange_slider
        
        self.section_view.controls.append(flet.Text("\n"))
        #* Down bellow is for done_button and delete_btn.
        done_button = flet.ElevatedButton("Done", bgcolor="white", color="black", width=150, height=40, on_click=self.done_edit)
        self.section_view.controls.append(flet.Row([done_button], alignment="center"))

        delete_button = flet.TextButton(content=flet.Text("delete", color="red", size=13), on_click=self.delete_widget)
        self.section_view.controls.append(flet.Row([delete_button], alignment="center"))
    
    def done_edit (self, *args):
        new_widget_properties_dict = {}
        for P in self.all_fields:
            new_widget_properties_dict[P] = self.all_fields[P].value
        

        if int(self.widget_number) == int(self.rearrange_slider.value):
            #? If the widget arrange is the same.
            self.main_widget_mother_class.template["widgets"][self.widget_number]["properties"].update(new_widget_properties_dict)
        else:
            #? If the widget arrange is NOT the same.
            if int(self.rearrange_slider.value) >= int(len(self.main_widget_mother_class.template["widgets"])):
                self.main_widget_mother_class.template["widgets"][self.widget_number]["properties"].update(new_widget_properties_dict)
                copy_of_content = self.main_widget_mother_class.template["widgets"][self.widget_number]
                del self.main_widget_mother_class.template["widgets"][self.widget_number]
                
                self.main_widget_mother_class.template["widgets"].append(copy_of_content)

                self.widget_number = int(len(self.main_widget_mother_class.template["widgets"])-1)
            else:
                self.main_widget_mother_class.template["widgets"][self.widget_number]["properties"].update(new_widget_properties_dict)
                copy_of_content = self.main_widget_mother_class.template["widgets"][self.widget_number]
                
                self.main_widget_mother_class.template["widgets"][int(self.rearrange_slider.value)] = copy_of_content
                del self.main_widget_mother_class.template["widgets"][self.widget_number]

                self.widget_number = int(self.rearrange_slider.value)

        
        #? Update the viewer engine to see the edit changes.
        self.main_widget_mother_class.update_preview()
        self.main_class.preview_section.update_preview(self.main_class.current_page_name)
        self.main_class.page.update()

        #? ReOpen the editor again
        editSubWidgetsEngine(main_class=self.main_class, main_widget_mother_class=self.main_widget_mother_class, section_view=self.section_view, widget_number=self.widget_number)
        self.main_class.page.update()

    def delete_widget (self, *args):
        del self.main_widget_mother_class.template["widgets"][self.widget_number]
        self.section_view.clean()

        #? Update the viewer engine to see the edit changes.
        self.main_class.preview_section.update_preview(self.main_class.current_page_name)
        self.main_class.page.update()