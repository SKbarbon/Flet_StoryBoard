import json


def Create_StoryBoard(file_name, template="default", storyboard_suggestions=False, 
    main_page_suggestions_rules="none", support_bard_ai=False):

    if template == "default":
        storyboard_default_template = {
            "storyboard_settings": {
                "template": "default",
                "storyboard_suggestions": storyboard_suggestions,
                "allow_scroll": False,
                "support_bard" : support_bard_ai
            },
            "pages": {
                "main": {
                    "settings": {
                        "bgcolor": "#333333",
                        "suggestions_rules": f"{main_page_suggestions_rules}"
                    },
                    "widgets": [

                    ]
                }
            }
        }

        file = open(f"{file_name}.fletsb", "w+", encoding="utf-8")
        file.write(json.dumps(storyboard_default_template))
        return True
    else:
        print("External templates are not supported yet.")
