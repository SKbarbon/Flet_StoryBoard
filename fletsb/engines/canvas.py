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

        if not main_class.storyboard_class.development_mode:
            self.view.expand = True
            self.view.border_radius = 0


    def update_canvas(self):
        self.main_class.storyboard_controls.clear()
        self.main_col.controls.clear()

        for c in self.main_class.storyboard_content['pages'][f"{self.main_class.current_page_name}"]['widgets']:
            w = self.widget_gen(widget_data=c)
            self.main_col.controls.append(self.control_wraping(w))
            self.main_class.storyboard_controls.append(w)


        self.update_page_properties()
        
        if self.main_col.page != None:
            self.main_col.update()
    
    
    def update_page_properties (self):
        page_settings = self.main_class.storyboard_content['pages'][self.main_class.current_page_name]['settings']

        if page_settings['center_align']:
            self.main_col.horizontal_alignment = flet.CrossAxisAlignment.CENTER
            self.main_col.alignment = flet.MainAxisAlignment.CENTER
        else:
            self.main_col.horizontal_alignment = None
            self.main_col.alignment = None
        
        self.main_col.scroll = page_settings['scroll']
        self.main_col.auto_scroll = page_settings['auto_scroll']
        self.view.bgcolor = page_settings['bgcolor']

        # Update page title
        if self.main_col.page != None:
            self.main_col.page.title = self.main_class.current_page_name
            self.main_col.page.update()
    

    def control_wraping (self, widget_class):
        return widget_class.flet_object


    def widget_gen (self, widget_data:dict):
        return self._widget_generator(widget_data=widget_data)

    def _widget_generator (self, widget_data:dict) -> widgets.Widget:
        wid_cls_nm = widget_data['widget_name']

        wid_cls = tools.get_widget_class_by_name(widget_name=wid_cls_nm)
        wid_cls = wid_cls(
            storyboard_class=self.main_class.storyboard_class
        )
        
        wid_cls.data = widget_data
        wid_cls.update_subs()
        wid_cls.update_flet_object()

        return wid_cls