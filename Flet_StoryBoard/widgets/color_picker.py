import flet



class ColorPicker:

    def __init__(self, selected_color="black", label="pick a color"):
        self.ui_self = None
        self.__color_preview = None
        self.selected_color = selected_color
        self.label = label

        DropMain = flet.Dropdown(
            width=150,
            label=label,
            value=self.selected_color,
            color=flet.colors.BLUE_GREY_800,
            on_change=self.__choose_color
        )
        self.DropMain = DropMain

        all_normal_colors = ["white", "black", "pink", "orange", "red", "blue", "green", "purple", "other"]
        for color in all_normal_colors:
            DropMain.options.append(flet.dropdown.Option(f"{color}"))

        color_preview = flet.Container(width=50, height=60, bgcolor=self.selected_color, border_radius=10, border=flet.border.all(0.3, "black"))
        self.__color_preview = color_preview

        ui_self = flet.Row([DropMain, color_preview], alignment="center")
        self.ui_self = ui_self
    
    def __choose_color(self, me):
        def update_hex_color(me):
            if str(me.control.value) == "#": return
            self.selected_color = me.control.value
            self.__color_preview.bgcolor = str(self.selected_color)
            self.ui_self.update()
        self.selected_color = me.control.value
        if str(self.selected_color) == "other":
            self.ui_self.clean()
            hex_color_index = flet.TextField(label="hex color", color="black", width=150, on_change=update_hex_color)
            self.ui_self.controls.append(hex_color_index)
            color_preview = flet.Container(width=50, height=60, bgcolor=self.selected_color, border_radius=10, 
            border=flet.border.all(0.3, "black"), on_click=self.__back_now)
            self.__color_preview = color_preview
            self.ui_self.controls.append(color_preview)
        else:
            self.__color_preview.bgcolor = self.selected_color
            self.__color_preview.update()
        
        self.ui_self.update()
    
    def __back_now(self, me):
        self.selected_color = "black"
        self.ui_self.clean()
        DropMain = flet.Dropdown(
            width=150,
            label=self.label,
            value=self.selected_color,
            color=flet.colors.BLUE_GREY_800,
            on_change=self.__choose_color
        )
        self.DropMain = DropMain

        all_normal_colors = ["white", "black", "pink", "orange", "red", "blue", "green", "purple", "other"]
        for color in all_normal_colors:
            DropMain.options.append(flet.dropdown.Option(f"{color}"))

        color_preview = flet.Container(width=50, height=60, bgcolor=self.selected_color, border_radius=10, border=flet.border.all(0.3, "black"))
        self.__color_preview = color_preview

        self.ui_self.controls.append(DropMain)
        self.ui_self.controls.append(color_preview)

        self.ui_self.update()