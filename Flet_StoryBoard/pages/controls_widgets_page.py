from flet import *
import flet





def Widgets_Page(mainview : flet.Column, built_in_widgets, external_widgets, Edit_Controls_Page, self_class):
    Title1 = Text(" Built-in controls\n & widgets", color="black", size=18, weight="bold")
    mainview.controls.append(Title1)
    GV1 = GridView(
        expand=1,
        runs_count=5,
        max_extent=103,
        child_aspect_ratio=1.0,
        spacing=5,
        run_spacing=5,
    )
    for BWid in built_in_widgets:
        wi = widget_icon_generator(BWid, built_in_widgets[BWid]['icon'], Edit_Controls_Page, self_class, built_in_widgets)
        GV1.controls.append(wi)
    mainview.controls.append(GV1)

    return Title1


def widget_icon_generator(name, icon, on_click_function, self_class, built_in_widgets):
    def on_click(me):
        on_click_function(self_class, built_in_widgets, True, 0, name)
    
    ICN = Row([Icon(f"{icon}", color="black", size=30)], alignment="center")
    NAM = Row([Text(f"{name}", color="black", size=13)], alignment="center")

    CC = Column([Text("", size=3), ICN, NAM], width=60, height=60)
    return Container(CC, border=flet.border.all(0.2, "black"), border_radius=12, on_click=on_click)