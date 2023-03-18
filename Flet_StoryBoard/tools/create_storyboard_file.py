import os
import json



def createStoryboardFile (file_name, bgcolor):
    json_file = {
        "storyboard_information" : {
            "version" : 1.1
        },
        "page_settings" : {
            "title" : file_name,
            "bgcolor" : bgcolor,
            "width" : 800,
            "height" : 600,
            "auto_fullscreen" : False,
            "allow_resize" : True,
            "center_all" : True,
            "scroll" : False,
            "auto_scroll" : True
        },
        "controls" : [
            {
                "class" : "Row",
                "kind" : "control",
                "properties" : {
                    "alignment" : "center"
                },
                "controls" : [
                    {
                        "class" : "Text",
                        "kind" : "control",
                        "properties" : {
                            "value" : "Hello, world!",
                            "color" : "blue",
                            "size" : 20
                        }
                    }
                ]
            }
        ]
    }
    
    try:
        open(f"{file_name}.fletsb", "w+", encoding="utf-8").write(json.dumps(json_file))
    except:
        pass