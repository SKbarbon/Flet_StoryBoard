from fletsb import widgets
import json, os



class CreateStoryBoardFile:
    def __init__(self, file_path:str) -> None:
        open(file_path, "w+", encoding="utf-8").write(json.dumps(self.file_content()))

    def file_content (self) -> dict:
        return {
            "settings" : {
                "last_id": 0,
                "canvas": {
                    "freeform": False
                }
            },
            "pages" : {
                "main" : {
                    "settings": {
                        "center_align": True,
                        "scroll": False,
                        "auto_scroll": False,
                        "bgcolor": None
                    },
                    "widgets": [

                    ]
                }
            }
        }