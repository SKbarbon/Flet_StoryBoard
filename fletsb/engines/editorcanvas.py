from .canvas import Canvas
import flet


class EditorCanvas (Canvas):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        # Experiance data
        self.last_selected_widget = None
    

    def control_wraping(self, widget_class):
        def on_hover (e:flet.HoverEvent):
            if self.last_selected_widget == cont: return
            if str(e.data) == "true":
                cont.border = flet.border.all(2.5, color=flet.colors.GREY)
            else:
                cont.border = None
            if cont.page != None: cont.update()

        def on_click (e):
            self.main_class.start_edit_widget(int(widget_class.data['id']))
            if self.last_selected_widget != None:
                self.last_selected_widget.border = None

                if self.last_selected_widget.page != None:
                    self.last_selected_widget.update()
            
            cont.border = flet.border.all(2.5, color="#5eaaff")
            self.last_selected_widget = cont
            if cont.page != None: cont.update()

        cont = flet.Container(
            content=widget_class.flet_object,
            on_hover=on_hover,
            on_click=on_click,
            border_radius=15,
            tooltip=f"Click to edit this {widget_class.data['widget_name']} | ID '{widget_class.data['id']}'"
        )
        return cont