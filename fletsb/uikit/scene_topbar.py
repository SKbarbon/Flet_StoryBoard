import flet

class SceneTopbar (flet.Row):
    """A topbar that being used on a scene object."""
    def __init__ (self, title:str="", actions=None):
        super().__init__()
        self.controls.append(flet.Text("    ", height=15))

        self.title=title
        self._title_label = flet.Text(
            self.title, 
            weight="bold",
            size=28
        )
        self.controls.append(self._title_label)

        self.controls.append(flet.Text("", expand=True))

        self.actions = actions
        if actions is not None:
            for a in actions:
                self.controls.append(a)

        self.controls.append(flet.Text("    ", height=15))

    def update(self):
        self._title_label.value = self.title
        return super().update()