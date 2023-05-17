import flet


class StoryBoard:
    def __init__(self, page, main_class):
        self.__page: flet.Page = page
        self.__main_class = main_class
        self.functions = {}

    def add_function(self, function_name, function):
        """
Define function, so the storyboard's widgets can access to. Like `function name` property of the `Button` widget need to have a Defined function.
        """
        self.functions[function_name] = function
        self.points = {}

    def add_flet_control(self, control, on_centered=True):
        """
        Add a flet control to the storyboard.
        if `on_centered = True` that means that the control will center the storyboard.
        """
        if on_centered:
            r = flet.Row([control], alignment=flet.MainAxisAlignment.CENTER)
            self.__page.add(r)
            self.__page.update()
        else:
            self.__page.add(control)

    def get_point(self, point_name: str):
        """
        The point is a place you choose to store some data in.
        You will get `None` as a return if the point have nothing yet.
        """
        if point_name not in self.points:
            return None
        else:
            return self.points[point_name]

    def navigate_to_page(self, page_name: str):
        """
        Go to a page name
        """
        if page_name not in self.__main_class.dict_content["pages"]:
            raise KeyError(f"Page '{page_name}' is not found.")

        viewerEngine = self.__main_class.viewerEngine
        viewerEngine = viewerEngine(
            self.__main_class,
            self.__main_class.dict_content,
            page_name,
            self.__page,
            self.__page,
            self.__main_class.development_mode
        )
        self.__page.update()

    def close_window(self):
        """Close the window"""
        self.__page.window_close()