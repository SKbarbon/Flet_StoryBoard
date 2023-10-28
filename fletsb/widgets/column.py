from .row import Row
import flet


class Column (Row):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.flet_object = flet.Column()
        self.flet_empty_placeholder_object = flet.Text("Empty Column")
        self.data['widget_name'] = "Column"