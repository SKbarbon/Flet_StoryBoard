from fletsb import tools
import flet



class StoryBoard:
    """A storyboard class allow you to manage the storyboard via your backend and apply changes on real-time 
    without saving these change and updates on your fletsb file."""
    def __init__(self, main_class, development_mode:bool) -> None:
        self.__main_class = main_class
        self.development_mode = development_mode

        # storyboard stored data
        self._last_id = int(main_class.storyboard_content['settings']['last_id'])

        # In-Usage data
        self.defined_functions = {}
    

    def define_function(self, function_name:str, function):
        """Define a function to be called on a widget event.
        
        You must go to widget properties and add the function name there to call it on event."""
        self.defined_functions[function_name] = function

    def navigate_to_page_name (self, page_name:str):
        """Navigate to certain page."""
        self.main_cls.change_canvas_page(page_name=page_name)

    def translate_page (self, target_language:str):
        """Translate the current page to a givin language."""
        pass

    def edit_widget_prop (self, widget_identifier_name:str, property_name:str, new_value):
        """Update a widget's property. The changes will apply immediately."""
        if widget_identifier_name == "":
            raise Exception("You must give a real widget_identifier_name")
    
    def get_property_value (self, widget_identifier_name:str, property_name:str):
        if widget_identifier_name == "":
            raise Exception("You must give a real widget_identifier_name")


    def get_new_widget_id (self):
        self._last_id = self._last_id + 1
        self.main_cls.storyboard_content['settings']['last_id'] = self.main_cls.storyboard_content['settings']['last_id'] + 1

        return self._last_id
    

    @property
    def main_cls (self):
        return self.__main_class
    
    @property
    def availble_pages (self):
        pages = []
        for p in self.main_cls.storyboard_content['pages']:
            pages.append(p)
        return pages
    
    @property
    def page (self) -> flet.Page:
        """returns flet.Page class. Or `None` if not found"""
        return self.main_cls.view.page