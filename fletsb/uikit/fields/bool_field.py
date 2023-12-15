import flet



class BoolField (flet.Row):
    def __init__ (self, field_name:str, on_change_function, original_value:int, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.field_name = field_name
        self.on_change_function = on_change_function

        self.alignment = flet.MainAxisAlignment.CENTER
        self.spacing = 5

        self.controls.append(
            flet.Text(str(field_name).replace("_", " ").capitalize(), color="white", expand=True)
        )

        self.controls.append(
            flet.Switch(value=original_value, on_change=self.on_change_value)
        )
    

    def on_change_value (self, e):
        self.on_change_function(self.field_name, e.control.value)