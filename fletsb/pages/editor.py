from fletsb import engines
from fletsb import StoryBoard
from fletsb.uikit import Scene
from fletsb import uikit
import flet, sys


class Editor (Scene):
    def __init__(self, project_path:str, page:flet.Page, application_class):
        self.application_class = application_class
        self.application_class.user_on_edit_state = True
        super().__init__(
            page=page,
            topbar=uikit.SceneTopbar(
                title=f"{project_path}",
                actions=[
                    flet.TextButton(content=flet.Container(
                        content=flet.Row([
                            flet.Text("Exit", color="black", weight=flet.FontWeight.W_300)
                        ], alignment=flet.MainAxisAlignment.CENTER),
                        bgcolor="white",
                        border_radius=13,
                        width=120, height=35
                    ), tooltip="Exit the project")
                ]
            ),
            controls=[],
            button_bar=uikit.SceneButtonbarEditor()
        )

        # data
        self.current_page_name = "main"
        self.storyboard_class = StoryBoard(main_class=self)
        self.storyboard_content = {}
        self.storyboard_controls = []

        # UI
        self.editor_canvas_engine = engines.Canvas(main_class=self)
        self.right_section = flet.Container(
            bgcolor=flet.colors.BLACK,
            border_radius=18
        )


        self.add_new_controls([flet.Row([
            self.editor_canvas_engine.view,
            self.right_section
        ], alignment=flet.MainAxisAlignment.CENTER)])
    


    def exit_project (self, e):
        self.application_class.self.user_on_edit_state = False
    

    def testing_content(self):
        self.storyboard_content = {
            "pages" : {
                "main" : {
                    "widgets": [
                        {
                            "widget_name" : "Row",
                            "properties" : {
                                "alignment": "end",
                                "spacing": 50
                            },
                            "controls": [
                                {
                                    "widget_name": "Title",
                                    "properties": {
                                        "text": "Hi",
                                        "color": "red",
                                        "size": 50
                                    },
                                    "controls": None,
                                    "content": None
                                },
                                {
                                    "widget_name": "Title",
                                    "properties": {
                                        "text": "Hi",
                                        "color": "red",
                                        "size": 50
                                    },
                                    "controls": None,
                                    "content": None
                                }
                            ],
                            "content": None
                        }
                    ]
                }
            }
        }

        self.editor_canvas_engine.update_canvas()