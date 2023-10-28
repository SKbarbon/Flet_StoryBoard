from .engines_tools.ai_add_request_prompt import ai_add_request_prompt
from .add_new_widget import AddNewWidget
from fletsb import tools
from freeGPT import Client
import json


class AiSuggestions:
    def __init__(self, storyboard_class) -> None:
        self.storyboard_class = storyboard_class

    def request_to_add (self, message:str):
        if message.replace(" ", "") == "": return
        prmpt = ai_add_request_prompt(message=message)

        ai_respone = Client.create_completion("gpt4", prompt=prmpt)

        ai_respone_dict = json.loads(ai_respone)
        print(ai_respone_dict)

        for wid in ai_respone_dict['widgets']:
            wdgt_cls = tools.get_widget_class_by_name(widget_name=wid['widget_name'])
            #! Adding the widgets.
            wdgt_cls = wdgt_cls(storyboard_class=self.storyboard_class)

            for wp in wdgt_cls.properties_data():
                if wp in wid['properties']:
                    wdgt_cls.data['properties'][wp] = wid['properties'][wp]
                else:
                    wdgt_cls.data['properties'][wp] = wdgt_cls.properties_data()[wp]['default_value']
            

            if "controls" in wid:
                for sub_c in wid['controls']:
                    if tools.get_widget_class_by_name(sub_c['widget_name']) != None:
                        wdgt_cls.data['controls'].append(sub_c)


            # IDs management
            object_id = self.storyboard_class._last_id
            self.storyboard_class._last_id = self.storyboard_class._last_id + 1
            self.storyboard_class.main_cls.storyboard_content['settings']['last_id'] = self.storyboard_class.main_cls.storyboard_content['settings']['last_id'] + 1
            wdgt_cls.data['id'] = object_id

            # Start adding the widget
            self.storyboard_class.main_cls.storyboard_content['pages'][self.storyboard_class.main_cls.current_page_name]['widgets'].append(wdgt_cls.data)
            self.storyboard_class.main_cls.editor_canvas_engine.update_canvas()

            # Save
            self.storyboard_class.main_cls.save_storyboard_content()

            print(wdgt_cls.data)