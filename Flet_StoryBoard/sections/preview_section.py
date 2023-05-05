import flet
from ..engines.viewer_engine import viewerEngine


class PreviewSection:
    def __init__(self, page: flet.Page, main_class, main_row: flet.Row):
        self.page: flet.Page = page
        self.main_class = main_class

        self.main_view = flet.Container(
            width=page.width - (page.width / 4) * 2,
            height=page.height - 80,
            border=flet.border.all(0.4, flet.colors.WHITE60),
            border_radius=12
        )
        main_row.controls.append(self.main_view)

        self.main_view_column = flet.Column(alignment=flet.MainAxisAlignment.CENTER)
        self.main_view.content = self.main_view_column

        self.update_preview()
        page.update()

    def update_preview(self, page_name="main"):
        ve = viewerEngine(
            self.main_class,
            self.main_class.dict_content,
            page_name,
            self.main_view,
            self.main_view_column
        )
