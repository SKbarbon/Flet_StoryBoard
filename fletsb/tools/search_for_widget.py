from fletsb import widgets




def search_for_widget_id (storyboard_class, widget_id:int) -> widgets.Widget:
    """Search for widget by its id. Returns `None` if no widget found."""
    def childs_fitcher(parent_widget:widgets.Widget, widget_id:int):
        if parent_widget.data['controls'] != None:
            for c in parent_widget.controls:
                if c.data['id'] == widget_id:
                    return c
                else:
                    r = childs_fitcher(parent_widget=c, widget_id=widget_id)
                    if r != None:
                        return r
        
        if parent_widget.data['content'] != None:
            if parent_widget.content.data['id'] == widget_id:
                return parent_widget.content


    for w in storyboard_class.main_cls.storyboard_controls:
        if int(w.data['id']) == widget_id:
            return w
        else:
            ws = childs_fitcher(parent_widget=w, widget_id=widget_id)
            if ws != None:
                return ws
    
    return None