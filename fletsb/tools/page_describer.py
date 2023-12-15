



class PageDescriber:
    def __init__(self, editor_class) -> None:
        self.editor_class

    def describe (self) -> str:
        text_describtion = ""
        current_page_name = self.editor_class.current_page_name
        
        text_describtion = text_describtion + f"Current Page Name: '{current_page_name}'"

        text_describtion = text_describtion + "Page Content:"

    
    def index_and_resturn_describe (self, parent, parent_is_page=False, tap_amount="    ") -> str:
        tap_amount = tap_amount
        t = ""

        if parent_is_page:
            for i in parent.controls:
                t = t + f"\n{tap_amount}{i.data['widget_name']}"
        else:
            pass

        for i in parent.controls:
            t = t + f"\n{tap_amount}{i.data['widget_name']}"
