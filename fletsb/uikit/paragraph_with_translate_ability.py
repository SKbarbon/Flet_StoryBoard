from deep_translator import GoogleTranslator
import flet



class ParagraphWithTranslateAbility (flet.Column):
    def __init__ (self, text:str):
        super().__init__()
        self.text : str = text

        # Properties
        self.scroll = flet.ScrollMode.ADAPTIVE

        # Languages
        languages_row = flet.Row(scroll=flet.ScrollMode.ADAPTIVE)
        self.controls.append(languages_row)

        original_language_btn = flet.ElevatedButton("Original", on_click=self.return_original_text)
        languages_row.controls.append(original_language_btn)

        for l in self.availble_languages:
            languages_row.controls.append(flet.TextButton(l, on_click=self.translate_to_language))

        # The README file
        self.the_markdown = flet.Markdown(value=text)
        self.controls.append(self.the_markdown)

    
    def translate_to_language (self, e):
        target_language = self.availble_languages[str(e.control.text)]
        translated = GoogleTranslator(source='en', target=target_language).translate(self.text)

        self.the_markdown.value = translated
        self.the_markdown.update()
    

    def return_original_text (self, e):
        self.the_markdown.value = self.text
        self.the_markdown.update()


    @property
    def availble_languages (self):
        return {
            "German": "german",
            "French": "french",
            "Arabic": "ar",
            "Russian": "ru"
        }