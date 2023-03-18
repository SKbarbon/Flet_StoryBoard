from flet import Container, Row, Column
import flet


def none(*args):
    pass

class colorPicker:

    def __init__(self, mainview=None, selected_color="white", on_choose_color=none, add_it=True, title_name="select color", drop_width=200, color_prev_width=50) -> None:
        if mainview == None: return
        self.__all_colors = ["None", "white", "black", "pink", "red", "green", "yellow", "hex-color"]

        self.drop_width = drop_width
        self.on_choose_color = on_choose_color
        self.mainview = mainview
        self.selected_color = selected_color

        v = Container()
        self.v = v

        main_dropdown = flet.Dropdown(width=drop_width, value=selected_color, label=title_name, on_change=self.on_choose)
        for i in self.__all_colors:
            main_dropdown.options.append(flet.dropdown.Option(i))
        self.mainDropdown = main_dropdown

        color_preview = flet.Container(width=color_prev_width, height=50, bgcolor=self.selected_color, border_radius=8, border=flet.border.all(0.1, "white"))
        self.color_preview = color_preview

        main_row = Row(controls=[
            main_dropdown,
            color_preview
        ])
        self.main_row = main_row

        v.content = main_row
        if add_it:
            mainview.controls.append(v)
    

    def on_choose (self, me):
        def on_change_color (me):
            tfc.value = str(tfc.value).replace(" ", "")
            tfc.update()
            if tfc.value != "#":
                new_color_selected = tfc.value
                self.selected_color = tfc.value
                self.color_preview.bgcolor = tfc.value
                self.on_choose_color(tfc.value)
            self.v.update()
        
        def back_to_orig (me):
            self.color_preview.on_click = None
            self.selected_color = "white"
            self.mainDropdown.value = self.selected_color
            self.color_preview.bgcolor = self.selected_color
            self.main_row.controls[0] = self.mainDropdown
            self.v.update()

        new_color_selected = me.control.value
        tfc = flet.TextField(label="hex-color", value="#0", width=self.drop_width, on_change=on_change_color, on_submit=on_change_color)

        if str(new_color_selected) == "hex-color":
            self.main_row.controls[0] = tfc
            self.color_preview.on_click = back_to_orig
        elif str(new_color_selected) == "None":
            self.color_preview.bgcolor = None
            self.selected_color = None
            self.on_choose_color(new_color_selected)
        else:
            self.color_preview.bgcolor = new_color_selected
            self.selected_color = new_color_selected
            self.on_choose_color(new_color_selected)
        
        self.v.update()
    
    def update(self):
        self.mainDropdown.value = self.selected_color
        self.color_preview.bgcolor = self.selected_color
        self.v.update()