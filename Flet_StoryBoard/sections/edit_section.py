from flet import Column, Page, Row
import flet

from ..engines.edit_widget_engine import EditWidgetsEngine


class editSection:
    def __init__(self, page:Page, main_class, main_row:Row) -> None:
        self.page : Page = page
        self.main_class = main_class
        self.main_row : Row = main_row

        self.main_column = Column(width=page.width/4, height=page.height,scroll=True)

        main_row.controls.append(self.main_column)
    
    def edit_widget_using_engine (self, widget_number):
        ee = EditWidgetsEngine(main_class=self.main_class, section_view=self.main_column, widget_number=widget_number)