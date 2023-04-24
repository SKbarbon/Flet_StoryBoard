from flet import Page, Row, Column, Container
import flet

from ..Engines.viewer_engine import viewerEngine
from ..Tools.page_info import get_page_bgcolor


class previewSection:
    def __init__(self, page:Page, main_class, main_row:Row):
        self.page : Page = page
        self.main_class = main_class
        
        self.main_view = Container(width=page.width-(page.width/4)*2, height=page.height-80, 
        border=flet.border.all(0.4, flet.colors.WHITE60), border_radius=12)
        main_row.controls.append(self.main_view)

        self.main_view_collumn = Column(alignment="center")
        self.main_view.content = self.main_view_collumn

        self.update_preview()
        page.update()

    def update_preview (self, page_name="main"):
        ve = viewerEngine(self.main_class, self.main_class.dict_content, page_name, self.main_view, self.main_view_collumn)