from fletsb import utils
from .scene_topbar import SceneTopbar
from .topbar_controller import TopbarController
import flet


class Scene (flet.Column):
    """A scene is a content container, is like the mother of current window content.
    
    A scene can contains multiple sub pages, navigations, Separate topbar, etc..
    """
    def __init__(self, page:flet.Page, topbar:SceneTopbar=None, controls=None, button_bar=None, support_top_bar_controlers=False) -> None:
        super().__init__()
        # Fake spacer
        self.controls.append(flet.Text(""))

        # Window Controlers
        if support_top_bar_controlers and utils.is_phone_platform() == False and page.web == False:
            self.controls.append(flet.WindowDragArea(content=TopbarController(page=page)))


        # Topbar
        if topbar == None:
            self.topbar = flet.Text("", height=0)
        else:
            self.topbar = topbar
        
        self.controls.append(self.topbar)


        # Content
        self.controls_place = flet.Column(
            expand=True
        )
        self.controls.append(self.controls_place)
        if controls is None: controls = []
        self.add_new_controls(controls)
        
        # Buttom bar
        self.buttom_bar = button_bar
        if button_bar == None:
            self.controls.append(flet.Text(""))
        else:
            self.controls.append(button_bar)
        
        # Spacer
        self.controls.append(flet.Text(" ", height=1.5))
    

    def add_new_controls (self, controls):
        for i in controls:
            self.controls_place.controls.append(i)