from fletsb.uikit import fields
import flet



class PageSettingsForum (flet.Column):
    """The settings forum to edit a page properties."""
    def __init__ (self, editor_class, page_name):
        super().__init__()
        self.editor_class = editor_class
        self.refresh_forum()

        self.scroll = flet.ScrollMode.ALWAYS
        self.auto_scroll = True
    
    def refresh_forum (self):
        self.controls.clear()
        self.controls.append(flet.Text(f"Page is {self.editor_class.current_page_name}", color=flet.colors.GREY_400, weight=flet.FontWeight.W_300))

        current_page_settings = self.editor_class.storyboard_content['pages'][self.editor_class.current_page_name]['settings']
        for option in self.all_default_settings_properties:
            # Field data
            field_type = self.all_default_settings_properties[option]['type']
            field_default_value = self.all_default_settings_properties[option]['default']
            if option in current_page_settings: field_real_value = current_page_settings[option]
            else: field_real_value = field_default_value

            # Generate option title
            title_label = flet.Text(str(option).replace("_", " ").capitalize(), weight=flet.FontWeight.W_400)
            self.controls.append(title_label)

            # Option field
            if field_type == "str":
                fld = fields.StringField(
                    on_change_function=self.on_change_setting_option,
                    original_value=field_real_value,
                    field_name=option
                )
                self.controls.append(flet.Row([fld], alignment=flet.MainAxisAlignment.CENTER))
            
            elif field_type == "bool":
                title_label.visible = False
                fld = fields.BoolField(
                    field_name=option,
                    on_change_function=self.on_change_setting_option,
                    original_value=field_real_value
                )
                self.controls.append(fld)

            elif field_type == "color":
                fld = fields.ColorField(
                    field_name=option,
                    on_change_function=self.on_change_setting_option
                )
                self.controls.append(fld)
        

        if self.page != None:
            self.update()
    

    def on_change_setting_option (self, option_name, new_value):
        page_name = self.editor_class.current_page_name
        self.editor_class.storyboard_content['pages'][page_name]['settings'][option_name] = new_value

        self.editor_class.editor_canvas_engine.update_canvas()
        self.editor_class.editor_canvas_engine.update_page_properties()
        self.editor_class.update()

        # Save changes
        self.editor_class.save_storyboard_content()


    @property
    def all_default_settings_properties(self):
        return {
            "center_align": {'type': 'bool', 'default': True},
            "scroll": {'type': 'bool', 'default': True},
            "auto_scroll": {'type': 'bool', 'default': True},
            "bgcolor": {'type': 'color', "default": "black"}
        }