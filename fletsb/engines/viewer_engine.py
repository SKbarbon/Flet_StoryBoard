from flet import Page, Container
import flet

from ..widgets.All import all_widgets


class viewerEngine:
    def __init__(self, main_class, content_dict: dict, page_name, parent_view, widgets_parent_view, development=True):
        """
        This is the engine of preview.
        parent_view -> is the Container in the develop case, and Page in the production case
        widgets_parent_view -> is the Column in the develop case, and Page in the production case
        """
        self.main_class = main_class
        self.content = content_dict
        self.page_name = page_name
        self.parent_view = parent_view
        self.widgets_parent_view = widgets_parent_view
        self.development = development

        self.last_clicked = None  # last widget clicked to edit. this is for make a border color around it to know
        # it's selected.

        self.update_page()
        self.push_views()

    def push_views(self):
        page_name: str = self.page_name
        content = self.content["pages"][page_name]
        sub_widgets = content["widgets"]

        self.widgets_parent_view.controls.clear()
        num = 0
        for widget in sub_widgets:
            if widget["widget_class_name"] in all_widgets:
                widget_class = all_widgets[widget["widget_class_name"]]["class"]
                widget_class = widget_class(self.main_class, self.widgets_parent_view, widget_number=num)
                if hasattr(widget_class, "support_sub_widgets"):
                    widget_class.update(widget["properties"], widget["widgets"])
                else:
                    widget_class.update(widget["properties"])
                if self.development:
                    self.create_development_container(widget_class.return_widget(), num)
                else:
                    self.widgets_parent_view.controls.append(widget_class.return_widget())
            num = num + 1

    def update_page(self):
        p: flet.Container = self.parent_view
        page_settings = self.content["pages"][self.page_name]["settings"]
        bgcolor = page_settings["bgcolor"]
        p.bgcolor = bgcolor

        if "allow_scroll" in self.main_class.dict_content["storyboard_settings"]:
            self.widgets_parent_view.scroll = self.main_class.dict_content["storyboard_settings"]["allow_scroll"]

    def create_development_container(self, cls, widget_number):
        def on_click(cls):
            if self.last_clicked != None:
                self.last_clicked.border = None
            self.last_clicked = c
            self.last_clicked.border = flet.border.all(2, "#b887fc")
            # ? This function will call the main_page edit.
            self.main_class.edit_a_widget(widget_number)

        c = flet.Container(cls, on_click=on_click, border_radius=8)
        self.widgets_parent_view.controls.append(c)
        return c
