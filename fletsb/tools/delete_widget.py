from fletsb import widgets




def delete_widget_by_id (storyboard_class, widget_id:int) -> widgets.Widget:
    """"""
    def childs_fitcher(parent_widget:widgets.Widget, widget_id:int):
        if parent_widget.data['controls'] != None:
            for c in parent_widget.controls:
                if c.data['id'] == widget_id:
                    parent_widget.controls.remove(c)
                    return True
                else:
                    childs_fitcher(parent_widget=c, widget_id=widget_id)
        
        if parent_widget.data['content'] != None:
            if parent_widget.content.data['id'] == widget_id:
                if parent_widget.content.data['id'] == widget_id:
                    pass
                else:
                    return childs_fitcher(parent_widget=parent_widget.content, widget_id=widget_id)


    for w in storyboard_class.main_cls.storyboard_controls:
        if int(w.data['id']) == widget_id:
            storyboard_class.main_cls.storyboard_controls.remove(w)
            return w
        else:
            ws = childs_fitcher(parent_widget=w, widget_id=widget_id)
            if ws == True:
                return
    
    return Exception("Cannot found control")