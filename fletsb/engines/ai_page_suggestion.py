from fletsb.engines.engines_tools.ai_suggest_to_user_prompt import ai_add_request_prompt
from freeGPT import Client
import threading, time, traceback, json, flet



class LoopAiPageSuggestion:
    """This process is a background loop for AI to give suggestions for the current page."""
    def __init__(self, editor_class) -> None:
        self.editor_class = editor_class
        threading.Thread(target=self.run_in_loop, daemon=True).start()

    def run_in_loop (self):
        print("Ai Loop suggestions Started.")
        time.sleep(1.5)
        while self.editor_class.application_class.user_on_edit_state:
            try:
                self.get_new_suggestion()
            except:
                traceback.print_exc()
            
            #? Wait 8 Minutes
            for i in range(480):
                self.editor_class.buttom_bar.content_of_ai_icon.tooltip = f"Next AI suggestion is at {int(480-i)} seconds."
                if self.editor_class.buttom_bar.content_of_ai_icon.page != None:
                    self.editor_class.buttom_bar.content_of_ai_icon.update()
                if self.editor_class.application_class.user_on_edit_state:
                    time.sleep(1)
        print("Ai Loop suggestions closed.")


    def get_new_suggestion (self):
        self.editor_class.buttom_bar.ai_chat_row.controls[0].content = flet.TextButton(content=flet.Text("🧐", size=25), tooltip="Thinking..",
                                                                                       width=50, height=50)
        self.editor_class.buttom_bar.ai_chat_row.update()

        current_page_name = str(self.editor_class.current_page_name)
        current_page_props = str(json.dumps(self.editor_class.storyboard_content['pages'][self.editor_class.current_page_name]['settings']))
        current_page_content = str(json.dumps(self.editor_class.storyboard_content['pages'][self.editor_class.current_page_name]['widgets']))

        prompt = ai_add_request_prompt(content=current_page_content, page_name=current_page_name, page_props=current_page_props)

        ai_respone = Client.create_completion("gpt4", prompt=prompt)
        
        self.editor_class.buttom_bar.new_ai_suggestion(text=str(ai_respone))