import flet



class StringField (flet.TextField):
    def __init__ (self, on_change_function, original_value, field_name:str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.on_change_function = on_change_function
        self.field_name = field_name

        self.multiline = True
        self.text_size = 20
        self.height = 60
        self.width = 180
        self.border = None
        self.hint_text = f"{field_name}.."
        self.value = original_value
        self.on_change = self.on_change_value
    

    def on_change_value (self, e):
        self.on_change_function(self.field_name, self.value)
    

    @property
    def field_value (self):
        return self.__field_value