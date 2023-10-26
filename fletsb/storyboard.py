




class StoryBoard:
    """A storyboard class allow you to manage the storyboard via your backend and apply changes on real-time 
    without saving these change and updates on your fletsb file."""
    def __init__(self, main_class) -> None:
        self.__main_class = main_class

        # storyboard stored data
        self.defined_functions = {}
    

    def define_function(self, function_name:str, function):
        """Define a function to be called on a widget event.
        
        You must go to widget properties and add the function name there to call it on event."""
        self.defined_functions.update[function_name] = function

    def navigate_to_page_name (self, page_name:str):
        """Navigate to certain page"""
        pass

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