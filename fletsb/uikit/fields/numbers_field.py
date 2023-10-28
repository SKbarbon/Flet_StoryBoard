import flet



class NumbersField (flet.Row):
    def __init__ (self, field_name:str, on_change_function, original_number:int, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.field_name = field_name
        self.on_change_function = on_change_function

        self.alignment = flet.MainAxisAlignment.CENTER
        self.spacing = 5

        self.minus_btn = flet.TextButton("-", tooltip="Minus one", height=40, on_click=self.minus_one)
        self.controls.append(self.minus_btn)

        self.number_field = flet.TextField(
            value=f"{original_number}", 
            width=50, 
            text_align=flet.TextAlign.CENTER, 
            on_change=self.on_change_number
        )
        self.controls.append(self.number_field)

        self.plus_btn = flet.TextButton("+", tooltip="Plus one", height=40, on_click=self.plus_one)
        self.controls.append(self.plus_btn)
    

    def on_change_number (self, e):
        try:
            int(self.number_field.value)
        except:
            self.number_field.value = "0"
            self.number_field.update()
            return
        self.on_change_function(self.field_name, self.number_field.value)
    

    def plus_one(self, e):
        self.number_field.value = str(int(self.number_field.value)+1)
        self.number_field.update()

        self.on_change_number(None)
    

    def minus_one (self, e):
        self.number_field.value = str(int(self.number_field.value)-1)
        self.number_field.update()

        self.on_change_number(None)