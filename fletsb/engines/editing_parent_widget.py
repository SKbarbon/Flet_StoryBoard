from fletsb.uikit.navigationview import NavigationView
from fletsb import tools
from fletsb import engines
import flet, time, json


class EditParentWidget (flet.Column):
    """Show a view where the user will be able to edit a parent widget like (Rows, Columns and Stacks)
    
    Where a real-time preview of the widget is shown"""
    def __init__(self, editor_class, widget_id:int, the_close_function) -> None:
        super().__init__()
        self.editor_class = editor_class
        self.the_close_function = the_close_function

        # self.controls.append(flet.Text(f"Edit a class with id {widget_id}"))
        self.widget_class = tools.search_for_widget_id(editor_class.storyboard_class, widget_id)
        if self.widget_class == None:
            self.editor_class.application_class.push_error_banner(
                title="Indexing Child Error 😕!",
                text="There was an error while trying to index this widget child."
            )
            self.controls.append(flet.Text("Check the error banner."))
            self.alignment = flet.MainAxisAlignment.CENTER
            self.horizontal_alignment = flet.CrossAxisAlignment.CENTER
            return
        
        self.nav = NavigationView(
            title="Edit Childs",
            on_click_close=the_close_function
        )

        self.controls.append(self.nav)

        #? The preview
        self.nav.add_new_navigation(
            navigation_name="Preview",
            navigation_content=flet.Column([
                self.widget_class.flet_object
            ], alignment=flet.MainAxisAlignment.CENTER, horizontal_alignment=flet.CrossAxisAlignment.CENTER),
            on_navigate=lambda: self.update()
        )

        #? The List of subviews to edit
        self.list_of_childs = flet.ListView([])
        if self.widget_class.data['controls'] != None:
            self.nav.add_new_navigation(
                navigation_name="Children",
                navigation_content=flet.Container(content=self.list_of_childs, padding=25)
            )
            self.update_childs_list()
        


        #? The edit props page
        self.nav.add_new_navigation(
                navigation_name="Edit Properties",
                navigation_content=flet.Text("Navigating to Edit section"),
                on_navigate=lambda: self.edit_current_widget_properties()
            )


        #? Open the navigation
        self.nav.open_navigation(navigation_name="Preview")
    

    def update_childs_list (self):
        #* Clear the list
        self.list_of_childs.controls.clear()

        #* This is the toprow
        top_row = flet.Row([flet.TextButton("Add New Child", on_click=self.add_new_child_widget_sheet)], alignment=flet.MainAxisAlignment.END)
        self.list_of_childs.controls.append(top_row)

        #* Append the childs
        for iw in self.widget_class.controls:
            self.list_of_childs.controls.append(self.list_item(iw=iw))
        
        #* Update if posible
        if self.list_of_childs.page != None:
            self.list_of_childs.update()
    
    def list_item (self, iw):
        return flet.Row([
            flet.Text(f"{iw.data['widget_name']}", color="white"),
            flet.Text(f"ID:{iw.data['id']}", color=flet.colors.GREY_300, weight=flet.FontWeight.W_300),
            flet.Text("", expand=True),
            flet.TextButton("Edit", on_click=lambda e: self.edit_child(child_id=iw.data['id']))
        ])
        
    
    def add_new_child_widget_sheet (self, e):
        def on_done():
            self.page.dialog.open = False
            self.page.dialog.update()
            self.update_childs_list()
        add_new_wdgt_view = engines.AddNewWidget(editor_class=self.editor_class, add_to=self.widget_class, on_done_adding=on_done)

        self.page.dialog = flet.AlertDialog(content=add_new_wdgt_view, open=True)
        self.page.update()

    
    def edit_child (self, child_id:str):
        def close_sheet_function (e):
            self.editor_class.storyboard_class.main_cls.application_class.show_the_sheet = False
        
        self.editor_class.storyboard_class.main_cls.application_class.sheet_container.content = EditParentWidget(
            editor_class=self.editor_class,
            widget_id=int(child_id),
            the_close_function=close_sheet_function
        )
        self.editor_class.storyboard_class.main_cls.application_class.show_the_sheet = True
    


    def edit_current_widget_properties (self):
        self.editor_class.application_class.show_the_sheet = False

        self.editor_class.editor_canvas_engine.update_canvas()


        self.editor_class.right_section.content = engines.EditingWidget(
            storyboard_class=self.editor_class.storyboard_class,
            widget_id=int(self.widget_class.data['id'])
        )
        self.editor_class.right_section.update()


    def delete_child (self, child_id:str):
        pass

    def add_childs_to_parent (self, widget_type_name:str):
        pass