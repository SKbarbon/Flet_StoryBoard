"""
The bardAPI integration.
"""
from bardapi import Bard
import os, flet, random, time, json


new_widgets_template = """
You are an AI for UI builder in a software called `Flet_StoryBoard`. Users will ask you to make something on their storyboard. The storyboard is a actually a json file that contain a UI stuff. Note that all your responses must be as json syntax. If a user tell you anything that unrelated to your job, return a `ok=false` on json. You can add new widgets. If the user ask you to put a widget that is not defined down bellow, then you choose one of the available widgets bellow that are similar to it.

The widgets are available are with their own properties:
- Title: title, title_color, size, width, italic, bold, hide, expand, alignment, text_align.
- Button: text, function_name, text_color, bgcolor, alignment, width, height, hide.
- Markdown: content, width, height, alignment.
- Open Url: text, url, text_color, bgcolor, alignment, width, height, border_radius, hide.
- Image: src, width, height, border_radius, alignment.
- TextField: text, label, hint_text, width, height, border_radius, bgcolor, color, alignment.

Note: do NOT set the `widget_class_name` to a name that does not exists above.

This is an example of how your json responses must look like:
```json
{
    "all" : [
        {
            "widget_class_name": "Title",
            "properties": {
                "title": "myTitle",
                "title_color": "white",
                "size": 23,
                "width": 350,
                "italic": false,
                "bold": true,
                "hide": false,
                "expand": false,
                "alignment": "center",
                "text_align": "left"
            }
        },
        {
            "widget_class_name": "Title",
            "properties": {
                "title": "myTitle2",
                "title_color": "white",
                "size": 23,
                "width": 350,
                "italic": false,
                "bold": true,
                "hide": false,
                "expand": false,
                "alignment": "center",
                "text_align": "left"
            }
        }
    ]
}
```

The user message is:
```user_message
</usermessage/>
```

Dont set the `widget_class_name` on the json to a name that does not exists above, For example if the user ask for a text, there is no Text widget, so you must search for a similar supported widget like the `title`.
Do not use any widget name except: Title, Button, Markdown, Open Url, Image or TextField.
Put all the widgets as shown on the previous json example.
"""

class BardapiSupport:
    def __init__(self, push_on_top_views_function, main_class) -> None:
        main_class.main_row.opacity = 0.2
        main_class.main_row.update()

        self.main_class = main_class
        container = flet.Container(on_click=self.close_the_input)
        self.container = container

        if self.get_bard_token() != None:
            bard_token = flet.TextField(hint_text="Put your bard Token..", 
                                        bgcolor="white", color="black")
            container.content = flet.Column([
                flet.Row([flet.Text("Your Bard Token")], alignment="center"),
                flet.Row([bard_token], alignment="center"),
                flet.Row([flet.Container(flet.Text("How to get the API token? Its totally free!", color="blue"), on_click=self.how_to_get_bard_token_page)], alignment="center")
            ], alignment="center")
            self.ress = push_on_top_views_function(self.container)
            if bard_token.page != None:
                bard_token.focus()
        else:
            ai_message_input = flet.TextField(
                border_radius=18,
                hint_text="",
                bgcolor="white",
                on_submit=self.on_message_submit,
                color="black"
            )

            container.content = flet.Column([
                flet.Row([ai_message_input], alignment="center"),
                flet.Row([flet.Text("The Bard AI", color="white")], alignment="center")
            ], alignment="center")
            self.ress = push_on_top_views_function(self.container)

            if ai_message_input.page != None:
                ai_message_input.focus()
            
            texts = ["Image with random cat image..", "A title that contain a cat emoji..", "A simple sign in page.."]
            for i in str(random.choice(texts)):
                ai_message_input.hint_text = ai_message_input.hint_text + i
                ai_message_input.update()
                time.sleep(0.02)
    
    def on_message_submit (self, e):
        e.control.disabled = True
        e.control.update()
        
        try: result = self.ask_bard(e.control.value)
        except: print("Error with connecting with bard."); return

        try:
            result = self.load_the_respone_to_dict(result)
        except Exception as e:
            print(f"Error:\n{e}")
            self.ress()
            return
        
        for new_widget in result['all']:
            wid = self.main_class.add_new_widget(new_widget["widget_class_name"])
            wid.update(new_widget['properties'])
            self.main_class.preview_section.update_preview(self.main_class.current_page_name)
            self.main_class.edit_a_widget(len(self.main_class.dict_content["pages"][self.main_class.current_page_name]["widgets"]) - 1)
            self.main_class.page.update()

        self.ress()
    
    def close_the_input (self, e):
        self.ress()
        self.main_class.main_row.opacity = 1.0
        self.main_class.main_row.update()

    def get_bard_token (self):
        if not os.path.isfile (".bardapi"):
            return None
        
        bardapi_token = open(".bardapi", encoding="utf-8").read()

        return bardapi_token
    
    def ask_bard (self, message):
        token = self.get_bard_token()
        if token == None:
            return False

        os.environ['_BARD_API_KEY'] = f"{token}"
        bard = Bard(timeout=10)
        message_new = new_widgets_template.replace("</usermessage/>", message)
        return str(bard.get_answer(message_new)['content'])
    
    def load_the_respone_to_dict (self, respone:str):
        full_string = ""
        found_it = False
        for i in str(respone).split("\n"):
            if found_it:
                if str(i).startswith("```"):
                    break
                full_string = full_string + f"\n{i}"
            
            if str(i).startswith("```json"):
                found_it = True
        
        return json.loads(full_string)
    
    def how_to_get_bard_token_page (self, e):
        p : flet.Page = e.page
        p.launch_url("")