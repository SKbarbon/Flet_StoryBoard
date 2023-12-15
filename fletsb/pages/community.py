import flet



class CommunityPage (flet.Column):
    def __init__(self, close_function) -> None:
        super().__init__()
        # Data
        self.close_function = close_function

        # Look and Shape
        self.alignment = flet.MainAxisAlignment.CENTER
        self.horizontal_alignment = flet.CrossAxisAlignment.CENTER

        # UI
        image_path = "/Users/yousifaladwani/Documents/GitHub/python/flet_projects/Flet_StoryBoard-beta/assets/imgs/cool.png"
        self.controls.append(flet.Image(image_path, width=50, height=50))

        self.controls.append(flet.Text("Stay Tuned!", weight=flet.FontWeight.BOLD))

        self.controls.append(flet.TextButton("close", on_click=self.close_page))
    
    def close_page (self, e):
        self.close_function()