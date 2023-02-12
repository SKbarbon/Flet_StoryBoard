from flet import *
from ..pages.edit_controls_page import Edit_Controls_Page
import flet



def Page_Preview_Page (self_class, ThePage):
    def generate_element(element, num, class_type):
        def edit_it(me):
            Edit_Controls_Page(self_class, self_class.built_in_widgets, False, num, class_type)
        return Container(element, on_click=edit_it)

    preview_settings = self_class.storyboard_json['preview_settings']
    
    THE_PREVIEW = flet.Container()
    THE_PREVIEW.width = 200
    THE_PREVIEW.height = 300
    THE_PREVIEW.bgcolor = "red"
    Elements = flet.Column(width=THE_PREVIEW.width, height=THE_PREVIEW.height)
    THE_PREVIEW.content = Elements
    self_class.preview_frame = Elements
    for set in preview_settings:
        if hasattr(THE_PREVIEW, set): setattr(THE_PREVIEW, set, preview_settings[set])

    built_in_widgets = self_class.built_in_widgets
    num = 0
    for I in self_class.storyboard_json["controls"]:
        class_type = built_in_widgets[str(next(iter(I)))]['class']()
        for i in I[str(next(iter(I)))]['properties']:
            if hasattr(class_type, i): setattr(class_type, i, I[str(next(iter(I)))]['properties'][i])
        if I[str(next(iter(I)))]['on_row_center'] == True:
            # Elements.controls.append(Container(Row([class_type], alignment="center"), on_click=print))
            Elements.controls.append(generate_element(Row([class_type], alignment="center"), num, str(next(iter(I)))))
        else:
            Elements.controls.append(generate_element(class_type,  num, str(next(iter(I)))))
        
        num = num + 1

    # ThePage.controls.append(Text("\n"))
    ThePage.controls.append(Row([THE_PREVIEW], alignment="center"))
    if ThePage.page != None: ThePage.update()