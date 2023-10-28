import flet



class OptionsField (flet.Container):
    def __init__ (self, on_change, feild_name, original_value, options:list, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.on_change_function = on_change
        self.field_name = feild_name

        self.picker = flet.Dropdown(
            value=original_value,
            on_change=self.on_choose_value,
            width=180,
            height=60,
            border="none"
        )

        self.content = self.picker
        self.border_radius = 18
        self.on_hover = self.hovered

        for op in options:
            self.picker.options.append(flet.dropdown.Option(f"{op}"))
    

    def on_choose_value (self, e):
        self.on_change_function(self.field_name, e.data)
    

    def hovered(self, e):
        if str(e.data).lower() == "true":
            self.border = flet.border.all(1.5, color=flet.colors.GREY)
        else:
            self.border = None
        
        self.update()