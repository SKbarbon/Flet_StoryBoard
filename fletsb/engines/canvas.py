from fletsb import tools
from fletsb import widgets
import flet


class Canvas:
    def __init__(self, main_class) -> None:
        self.main_class = main_class

        self.main_col = flet.Column(
            width=500,
            height=400
        )
        self.view = flet.Container(
            content=self.main_col,
            bgcolor=flet.colors.BLACK,
            border_radius=18
        )


    def update_canvas(self):
        self.main_class.storyboard_controls.clear()
        self.main_col.controls.clear()

        for c in self.main_class.storyboard_content['pages'][f"{self.main_class.current_page_name}"]['widgets']:
            w = self.widget_gen(widget_data=c)
            self.main_col.controls.append(w.flet_object)
            self.main_class.storyboard_controls.append(w)
        
        if self.main_col.page != None:
            self.main_col.update()


    def widget_gen (self, widget_data:dict):
        return self._widget_generator(widget_data=widget_data)

    def _widget_generator (self, widget_data:dict) -> widgets.Widget:
        wid_cls_nm = widget_data['widget_name']

        wid_cls = tools.get_widget_class_by_name(widget_name=wid_cls_nm)
        self.main_class.storyboard_controls.append(wid_cls)

        wid_cls = wid_cls(
            storyboard_class=self.main_class.storyboard_class
        )
        
        wid_cls.data = widget_data
        wid_cls.update_subs()
        wid_cls.update_flet_object()

        return wid_cls