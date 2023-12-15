from fletsb import tools
import flet



class AddNewWidget (flet.Column):
    """The `add_to` prop must be string named 'page' or a fletsb widget class."""
    def __init__(self, editor_class, add_to, on_done_adding=None) -> None:
        super().__init__()
        self.editor_class = editor_class
        self.add_to = add_to
        self.on_done_adding = on_done_adding
        
        self.all_widgets = tools.get_all_widgets()

        self.title = flet.Text("\n    Widgets", weight=flet.FontWeight.BOLD, size=20)
        self.controls.append(self.title)

        for w in self.all_widgets:
            wf = self.widget_label_frame(wid_name=w, wid_icon=self.all_widgets[w])
            self.controls.append(flet.TextButton(content=wf, on_click=self.add_new_widget_to_content, data=w))
        

        self.scroll = flet.ScrollMode.ALWAYS
    

    def add_new_widget_to_content (self, e):
        wdgt_cls = tools.get_widget_class_by_name(e.control.data)
        if wdgt_cls == None: return

        wdgt_cls = wdgt_cls(storyboard_class=self.editor_class.storyboard_class)

        for wp in wdgt_cls.properties_data():
            wdgt_cls.data['properties'][wp] = wdgt_cls.properties_data()[wp]['default_value']

        # IDs management
        object_id = self.editor_class.storyboard_class.get_new_widget_id()
        wdgt_cls.data['id'] = object_id

        # Start adding the widget
        if self.add_to == "page":
            self.editor_class.storyboard_content['pages'][self.editor_class.current_page_name]['widgets'].append(wdgt_cls.data)
            self.editor_class.editor_canvas_engine.update_canvas()
        else:
            widget_class = self.add_to
            widget_class.data['controls'].append(wdgt_cls.data)
            widget_class.update_subs()
            widget_class.update_flet_object()
        
        self.editor_class.save_storyboard_content()
        
        if self.on_done_adding != None:
            self.on_done_adding()
    

    def widget_label_frame (self, wid_name:str, wid_icon:str):
        def on_hov (e):
            if e.data == "true":
                e.control.border = flet.border.all(width=0.5, color=flet.colors.WHITE)
                e.control.update()
            else:
                e.control.border = None
                e.control.update()
        
        return flet.Container(
            content=flet.Row([
                flet.Text("   "),
                flet.Icon(wid_icon, color="white"),
                flet.Text(wid_name, color="white")
            ]),
            on_hover=on_hov,
            border_radius=18,
            height=40
        )