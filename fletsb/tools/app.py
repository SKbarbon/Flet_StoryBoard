from ..production import Production
import flet



def app (file_path:str, target, flet_app_view: flet.AppView=flet.AppView.FLET_APP):
    """Use the `app` function to start a Flet StoryBoard application via a target.
    
    The target will get a single argument for the `StoryBoard` class."""
    def flet_app (page:flet.Page):
        def on_res(e):
            p.view.width = page.width
            p.view.height = page.height
            p.view.update()
        # -----
        page.spacing = 0
        page.padding = 0
        page.vertical_alignment = flet.MainAxisAlignment.CENTER
        page.horizontal_alignment = flet.CrossAxisAlignment.CENTER
        page.window_title_bar_hidden = True

        p = Production(file_path=file_path)
        page.add(p.view)
        page.update()

        # events
        page.on_resize = on_res
        page.update()
        page.window_center()

        # Run target
        target(p.storyboard_class)
    flet.app(target=flet_app, view=flet_app_view)