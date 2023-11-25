import flet



class ColorField (flet.Column):
    def __init__(self, field_name:str, on_change_function, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.field_name = field_name
        self.on_change_function = on_change_function

        self.colors_options = ["black", "white", "#fa8c8c", "#8ce1fa"]
        self.border_color_of_frame = "#828282"

        self.grid_colors = flet.Row(spacing=5, alignment=flet.MainAxisAlignment.CENTER)
        self.controls.append(self.grid_colors)

        self.add_color_options()

    
    def add_color_options (self):
        self.grid_colors.controls.clear()

        for col in self.colors_options:
            cf = flet.Container(
                bgcolor=col,
                data=col,
                width=28,
                height=28,
                border_radius=10,
                border=flet.border.all(1.5, color="#828282"),
                tooltip=f"{col}",
                on_click=self.on_choose_color,
                on_hover=self.on_hover
            )
            self.grid_colors.controls.append(cf)
        
        self.grid_colors.controls.append(flet.Container(
            bgcolor="#686868",
            data=col,
            width=28,
            height=28,
            border_radius=10,
            border=flet.border.all(1.5, color="#828282"),
            content=flet.Icon(name=flet.icons.MORE_HORIZ_ROUNDED),
            on_click=self.on_choose_custom_color,
            tooltip="Custom color"
        ))

    def on_choose_color (self, e):
        self.on_change_function(self.field_name, e.control.data)
    

    def on_choose_custom_color (self, e):
        self.page.dialog = flet.AlertDialog(content=flet.Column([
            flet.Text("Custom Color", size=26, weight="bold"),
            flet.Row([
                flet.TextField(hint_text="Color name or #Hex", on_change=lambda e: self.on_change_function(self.field_name, e.control.value))
            ], alignment=flet.MainAxisAlignment.CENTER)
        ], width=350, height=100), open=True)
        self.page.update()
    
    def on_hover (self, e):
        if e.data == "true":
            e.control.border = flet.border.all(width=3, color="white")
        else:
            e.control.border = flet.border.all(width=1.5, color="#828282")
        
        e.control.update()