import flet
from ...ui_toolkit.widget_browser_frame import Widget_Browse_Frame


class Row(object):
    def __init__(self, main_class, parent, *args, **kwargs) -> None:
        self.parent = parent
        self.main_class = main_class
        self.self_object = flet.Row()

        self.widget_number = kwargs["widget_number"]

        # Row Special args.
        self.dont_border_subs = True
        self.last_added = None
        self.support_sub_widgets = True

        if main_class.development_mode:
            self.development_mode = True
        else:
            self.development_mode = False

        # all args
        self.args = {
            "width": {"type": int, "default_value": 23},
            "height": {"type": int, "default_value": 150},
            "hide": {"type": bool, "default_value": False},
            "scroll": {"type": bool, "default_value": False},
            "auto_scroll_to_end": {"type": bool, "default_value": True},
            "expand": {"type": bool, "default_value": True},
            "alignment": {"type": list, "options": ["left", "center", "right"], "default_value": "center"},
            "sub_widgets_alignment": {"type": list, "options": ["left", "center", "right"], "default_value": "center"},
        }

        # Template dict
        # This is where the widget data will be stored.
        self.template = {
            "widget_class_name": "Row",
            "properties": {},
            "widgets": []
        }
        for p in self.args:
            self.template["properties"][p] = self.args[p]["default_value"]

        self.update()

    def update(self, new_props: dict = None, new_sub_widgets: dict = None):
        r = self.self_object
        props = self.template["properties"]

        if new_props is not None:
            for i in new_props:
                self.template["properties"][i] = new_props[i]

        if new_sub_widgets is not None:
            for w in new_sub_widgets:
                self.template["widgets"].append(w)

        r.width = props["width"]
        r.height = props["height"]
        r.visible = props["hide"] == False
        r.expand = props["expand"]
        r.scroll = props["scroll"]
        r.alignment = props["sub_widgets_alignment"]
        r.auto_scroll = props["auto_scroll_to_end"]

        if self.self_object.page is not None:
            self.self_object.update()

        self.update_preview()

    # Row tools
    def widgets_to_add_in(self, *args):
        """To show all widgets that are available to add to the row."""
        for i in args:
            i.control.visible = False
            i.control.update()

        def go_back(*e):
            self.main_class.left_section.show_new_content(copy_of_last_container)
            if self.last_added is not None:
                if self.last_added.page is None:
                    self.last_added.border = None
                    self.main_class.page.update()
                else:
                    self.last_added.border = None
                    self.last_added.update()
            self.main_class.on_page_resize()
            for i in args:
                i.control.visible = True
                i.control.update()

        page = self.main_class.page
        # This is the default section.

        # issue: scroll has not attribute True
        col = flet.Column(scroll=True)
        col.controls.append(flet.TextButton("< Back", on_click=go_back))
        title = flet.Text("Widgets in row", size=25, weight=flet.FontWeight.BOLD, color="white")
        col.controls.append(title)
        all_widgets = self.main_class.all_widgets
        for wid in all_widgets:
            w = Widget_Browse_Frame(wid, all_widgets[wid], self.add_new_widget, self.main_class.current_page_name)
            col.controls.append(w)

        main_container = flet.Container(
            content=col,
            bgcolor=page.bgcolor,
            width=page.width / 4,
            height=page.height
        )

        copy_of_last_container = self.main_class.left_section.self_ui.content
        self.main_class.left_section.show_new_content(main_container)
        self.main_class.on_page_resize()
        self.main_class.page.update()

    def add_new_widget(self, widget_name, page_name):
        """To add the widget, and open the edit to edit this new sub-widget."""
        self.dont_border_subs = False
        all_widgets = self.main_class.all_widgets
        widget_class = all_widgets[widget_name]["class"]
        widget_class = widget_class(
            self, self.preview_section,
            widget_number=len(self.template["widgets"]) - 1,
            is_a_sub=True
        )

        self.template["widgets"].append(widget_class.template)
        self.main_class.dict_content["pages"][self.main_class.current_page_name]["widgets"][self.widget_number]["widgets"] = self.template["widgets"]

        self.update_preview()
        editSubWidgetsEngine = self.main_class._editSubWidgetsEngine
        editSubWidgetsEngine = editSubWidgetsEngine(
            self.main_class,
            self,
            self.main_class.edit_section.main_column,
            len(self.template["widgets"]) - 1
        )
        self.main_class.page.update()

    def update_preview(self):
        all_widgets = self.main_class.all_widgets
        self.preview_section.controls.clear()
        sub_widgets = self.template["widgets"]
        num = 0

        for widget in sub_widgets:
            if widget["widget_class_name"] in all_widgets:
                widget_class = all_widgets[widget["widget_class_name"]]["class"]
                widget_class = widget_class(self.main_class, self.preview_section)
                if hasattr(widget_class, "support_sub_widgets"):
                    widget_class.update(widget["properties"], widget["widgets"])
                else:
                    widget_class.update(widget["properties"])
                if self.development_mode:
                    self.create_development_container(widget_class.return_widget(), num)
                else:
                    self.preview_section.controls.append(widget_class.return_widget())
            num = num + 1

        self.main_class.page.update()

    @property
    def preview_section(self):
        return self.self_object

    def return_widget(self):
        props = self.template["properties"]

        if props["alignment"] == "left":
            return flet.Row([flet.Text("    "), self.self_object])
        elif props["alignment"] == "center":
            return flet.Row([self.self_object], alignment=flet.MainAxisAlignment.CENTER, spacing=0)
        else:
            return flet.Row([self.self_object, flet.Text("    ")], alignment=flet.MainAxisAlignment.END)

    def create_development_container(self, cls, widget_number):
        if self.last_added is None:
            c = flet.Container(cls, border_radius=8, border=flet.border.all(2, flet.colors.YELLOW_300))
            self.last_added = c
        else:
            self.last_added.border = None
            c = flet.Container(cls, border_radius=8, border=flet.border.all(2, flet.colors.YELLOW_300))
            self.last_added = c

        self.preview_section.controls.append(c)
        return c
