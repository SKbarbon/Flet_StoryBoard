import json
import flet
import random
import os
import requests

class SuggestingEngine:
    def __init__(self, main_class):
        self.main_class = main_class

        self.main_col = flet.Column(width=self.main_class.left_section.main_container.width, 
        height=self.main_class.left_section.main_container.height, scroll=True)

    def push_new_suggestion(self):
        settings = self.main_class.dict_content["storyboard_settings"]
        applied = settings["storyboard_suggestions"]
        if applied == False: return # if `storyboard suggestions` is off.
        # -----------------------------------------------------------------------
        suggestions_rules_name = self.main_class.dict_content["pages"][self.main_class.current_page_name]["settings"]["suggestions_rules"]
        if suggestions_rules_name == "none": return
        #? Get the rules file
        if not os.path.isdir("rules"):
            os.mkdir("rules")
        
        if not os.path.isfile(f"rules/{suggestions_rules_name}.json"):
            all_rules = requests.get("https://raw.githubusercontent.com/SKbarbon/Flet_StoryBoard/main/rules/all.json").text
            all_rules = json.loads(all_rules)
            if suggestions_rules_name not in all_rules["all_rules"]: return
            else:
                rf = requests.get(all_rules["all_rules"][suggestions_rules_name]).text
                open(f"rules/{suggestions_rules_name}.json", "w+", encoding="utf-8").write(rf)
        
        rules_file = json.loads(open(f"rules/{suggestions_rules_name}.json", encoding="utf-8").read())

        #? step1: Get current widgets.
        current_widgets = list(self.main_class.dict_content["pages"][self.main_class.current_page_name]["widgets"])

        #? step2: Count classes on widgets.
        classes_in_widgets = {}
        for c in current_widgets:
            if c["widget_class_name"] not in classes_in_widgets:
                classes_in_widgets[c["widget_class_name"]] = 1
            else:
                classes_in_widgets[c["widget_class_name"]] = classes_in_widgets[c["widget_class_name"]] + 1
        

        #? step3: Search for the correct case on the rules file.
        for rule in rules_file["rules"]:
            if rule["case"] == classes_in_widgets:
                self.change_left_section_into_suggestion(rule["sugs"])
                break
    

    def change_left_section_into_suggestion (self, suggestions):
        def go_back (e):
            if last_on_section == self.main_col:
                self.main_class.left_section.show_all_widgets()
            else:
                self.main_class.left_section.show_new_content(last_on_section)
        
        main_clo = self.main_col
        main_clo.controls.clear()
        
        back_btn = flet.TextButton("< Back", on_click=go_back)
        main_clo.controls.append(back_btn)

        title = flet.Text("Suggestions ✨", weight="bold", size=22, color="white")
        main_clo.controls.append(title)

        main_clo.controls.append(flet.Row([flet.Text("", color="white", size=13)], alignment="center"))

        for sug in suggestions:
            sc = self.suggestion_card(sug, go_back)
            main_clo.controls.append(flet.Row([sc], alignment="center"))

        last_on_section = self.main_class.left_section.main_container
        self.main_class.left_section.show_new_content(self.main_col)

    def suggestion_card (self, suggestion_dict, go_back_function):
        def add_widget (e):
            go_back_function(e)
            w = self.main_class.add_new_widget(suggestion_dict["class"])
            w.update(suggestion_dict["props"])
            self.main_class.preview_section.update_preview(self.main_class.current_page_name)
            self.main_class.edit_a_widget(len(self.main_class.dict_content["pages"][self.main_class.current_page_name]["widgets"])-1)
            self.main_class.page.update()
        # -----
        colors = ["white", "#F5DEE5", "yellow"]
        card_container = flet.Container(bgcolor=random.choice(colors), width=170, height=225, border_radius=13)
        collumn = flet.Column()
        card_container.content = collumn

        class_name = suggestion_dict["class"]
        why_to_add = suggestion_dict["about"]

        title = flet.Text(value=f"\n   {class_name}", size=23, weight="bold", color="black", width=card_container.width)
        collumn.controls.append(title)

        about = flet.Text(value=f"{why_to_add}", size=13, color="black", width=card_container.width-37, height=90)
        collumn.controls.append(flet.Row([about], alignment="center"))

        apply_button = flet.Container(flet.Row([
            flet.Text("Add", color="white")
        ], alignment="center"), bgcolor="black", width=card_container.width-15, height=40, border_radius=13, on_click=add_widget)
        collumn.controls.append(flet.Row([apply_button], alignment="center"))

        return card_container