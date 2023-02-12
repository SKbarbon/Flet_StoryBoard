import json




def create_flet_storyboard(name):
    """
    This function allow you to create a storyboard file.
    """
    index_file =  {
        "storyboard_information" : {
            "version" : 1.0
        },
        "preview_settings" : {
            "bgcolor" : "white",
            "width" : 300,
            "height" : 250,
            "border_radius" : 8,
            "expand" : False
        },
        "mother_view" : {
            
        },
        "controls" : [
            
        ]
    }

    if str(name).endswith(".fletsb"):
        open(f"{name}", "w+", encoding="utf-8").write(json.dumps(index_file))
    else:
        open(f"{name}.fletsb", "w+", encoding="utf-8").write(json.dumps(index_file))
    return True