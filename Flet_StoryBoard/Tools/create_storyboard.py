import json


def Create_StoryBoard (file_name, template="default", storyboard_suggestions=False, main_page_suggestions_rules="none"):
    if template == "default":
        storyboard_defualt_template = {
            "storyboard_settings" : {
                "template" : "default",
                "storyboard_suggestions" : storyboard_suggestions,
                "allow_scroll" : False
            },
            "pages" : {
                "main" : {
                    "settings" : {
                        "bgcolor" : "black",
                        "suggestions_rules" : f"{main_page_suggestions_rules}"
                    },
                    "widgets" : [
                        
                    ]
                }
            }
        }


        file = open(f"{file_name}.fletsb", "w+", encoding="utf-8")
        file.write(json.dumps(storyboard_defualt_template))
        return True
    else:
        print("External templates are nor supported yet.")