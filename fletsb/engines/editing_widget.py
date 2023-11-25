from fletsb.tools import delete_widget_by_id
from fletsb.uikit.banner_alert import error_banner_alert
from fletsb.uikit import fields
from fletsb import tools
import flet, traceback



class EditingWidget(flet.Column):
    def __init__(self, storyboard_class, widget_id:int):
        super().__init__()
        self.storyboard_class = storyboard_class
        self.widget_id = widget_id

        widget_class = tools.search_for_widget_id(storyboard_class, widget_id)
        self.widget_class = widget_class

        #? Check if the widget exists in the storyboard.
        if widget_class == None:
            self.controls.append(flet.Row([
                flet.Text(
                "Error while searching\nfor this widget.\n\nMaybe this widget\nis no longer exists",
                weight=flet.FontWeight.W_300,
                color="red",
                text_align=flet.TextAlign.CENTER
            )
            ], alignment=flet.MainAxisAlignment.CENTER))
            self.alignment = flet.MainAxisAlignment.CENTER
        

        # Start the UI
        self.scroll = True
        self.title_label = flet.Text(
            f"\n    Edit '{widget_class.data['widget_name']}'",
            size=23,
            weight=flet.FontWeight.BOLD
        )
        self.controls.append(self.title_label)

        self.id_label = flet.Text(f"        ID: {widget_class.data['id']}", size=12, color=flet.colors.GREY,
                                  weight=flet.FontWeight.BOLD)
        self.controls.append(self.id_label)

        # Generating fields
        for field in widget_class.properties_data():
            self.id_label = flet.Text(f"        {field}", size=12, color=flet.colors.GREY, weight=flet.FontWeight.BOLD)
            self.controls.append(self.id_label)
            
            fld_type = widget_class.properties_data()[field]['type']
            fld_value = widget_class.data['properties'][field]
            if fld_type == "str":
                fld = fields.StringField(
                        on_change_function=self.on_prop_changed,
                        original_value=fld_value, 
                        field_name=f"{field}"
                    )
                self.controls.append(flet.Row([fld], alignment=flet.MainAxisAlignment.CENTER))
            
            elif fld_type == "int":
                fld = fields.NumbersField(
                    field_name=field,
                    on_change_function=self.on_prop_changed,
                    original_number=f"{int(fld_value)}"
                )
                self.controls.append(fld)
            
            elif fld_type == "color":
                fld = fields.ColorField(
                    field_name=field,
                    on_change_function=self.on_prop_changed
                )
                self.controls.append(fld)
            
            elif fld_type == "list":
                options = widget_class.properties_data()[field]['options']
                fld = fields.OptionsField(
                    on_change=self.on_prop_changed,
                    feild_name=field,
                    original_value=fld_value, 
                    options=options
                )
                self.controls.append(flet.Row([fld], alignment=flet.MainAxisAlignment.CENTER))
            

        # The delete widget button
        self.controls.append(flet.Row([
            flet.TextButton(content=flet.Text("Delete", color="red"), tooltip="Delete the widget", on_click=self.delete_widget)
        ], alignment=flet.MainAxisAlignment.CENTER))
    

    def on_prop_changed (self, prop_name:str, prop_value):
        # print(f"New prop edited: name: {prop_name}, value: {prop_value}")
        self.widget_class.data['properties'][prop_name] = prop_value
        self.widget_class.update_subs()
        self.widget_class.update_flet_object()

        self.storyboard_class.main_cls.save_storyboard_content()
    

    def delete_widget (self, e=None):
        try:
            delete_widget_by_id(storyboard_class=self.storyboard_class, widget_id=self.widget_id)
        except:
            traceback.print_exc()
            self.page.banner = error_banner_alert(
                title="Widget cannot be deleted 😕!",
                text="""There was an error while trying to delete the widget from the file.
                """
            )
            self.page.banner.open = True
            self.page.overlay.clear()
            warning_audio_src = "https://cdn.pixabay.com/download/audio/2022/11/20/audio_3371f818f5.mp3?filename=error-2-126514.mp3"
            self.page.overlay.append(flet.Audio(warning_audio_src, autoplay=True, volume=0.5))
            self.page.update()

            self.storyboard_class.main_cls.editor_canvas_engine.update_canvas()
            self.storyboard_class.main_cls.save_storyboard_content()