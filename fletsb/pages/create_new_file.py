import flet
import time
import os
import json
import requests

from ..tools.create_storyboard import Create_StoryBoard


class CreateNewFile:
    def __init__(self, page: flet.Page, manage_class):
        page.window_resizable = False
        page.update()
        page.window_center()

        # Set page prop
        page.bgcolor = flet.colors.BLACK

        # Setup Content's mother.
        self.manage_class = manage_class
        self.page = page
        self.mother = flet.AnimatedSwitcher(
            expand=True,
            content=flet.Text(""),
            transition=flet.AnimatedSwitcherTransition.FADE,
            duration=500,
            reverse_duration=250,
            switch_in_curve=flet.AnimationCurve.EASE_IN
        )
        page.add(self.mother)

        time.sleep(0.3)
        # Run the first page.
        self.page_one()

    def page_one(self):
        page = self.page
        mother = self.mother
        main_column = flet.Column()
        mother.content = main_column

        main_column.controls.append(flet.Text("\n\n"))

        title_1 = flet.Text(
            "\n        Let's imagine 😃,\n        What if there is a ...",
            color=flet.colors.WHITE,
            size=36,
            weight=flet.FontWeight.BOLD
        )
        describe = flet.Text(
            "                  Everything start from the imagine skill.\n                  With Flet_StoryBoard you will make the impossible ✨.\n",
            color=flet.colors.WHITE60,
            size=15
        )
        next_button = flet.Container(
            flet.Row(
                [flet.Text("Start", color=flet.colors.BLACK)],
                alignment=flet.MainAxisAlignment.CENTER
            ),
            bgcolor=flet.colors.WHITE,
            width=100,
            height=35,
            border_radius=11,
            on_click=self.page_two
        )

        main_column.controls.append(title_1)
        main_column.controls.append(describe)
        main_column.controls.append(
            flet.Column(
                [
                    flet.Row(
                        [next_button],
                        alignment=flet.MainAxisAlignment.END
                    )
                ],
                alignment=flet.MainAxisAlignment.END,
                expand=True
            )
        )

        page.update()

    def page_two(self, *args):
        def on_type(event):
            if event.control.value == "":
                next_button.tooltip = "You must pick a name."
                next_button.disabled = True
                next_button.update()
            else:
                next_button.tooltip = "Click to generate the file."
                next_button.disabled = False
                page.title = "Flet StoryBoard - " + str(event.control.value)
                if os.path.isfile(f"{page.title}.fletsb"):
                    page.title = page.title + " | Warning: File name exist"
                page.update()
                self.file_name = str(event.control.value)

        page = self.page
        mother = self.mother
        main_column = flet.Column()
        mother.content = main_column

        main_column.controls.append(flet.Text("\n\n"))

        Title1 = flet.Text("\n        Hey sir 🎩,\n        What is the name ?", color=flet.colors.WHITE, size=36, weight="bold")
        main_column.controls.append(Title1)

        describe = flet.Text(
            "                  Lets choose a name of our UI.\n                  This name is the same as StoryBoad file name!.\n",
            color=flet.colors.WHITE60, size=15)
        main_column.controls.append(describe)

        StoryBoard_Name = flet.TextField(label="UI name", border_color=flet.colors.BLACK, cursor_color=flet.colors.BLACK,
                                         bgcolor=flet.colors.WHITE, border_radius=19, width=350, height=60, on_change=on_type,
                                         color=flet.colors.BLACK, on_submit=self.page_three)
        main_column.controls.append(flet.Row([StoryBoard_Name], alignment="center"))

        next_button = flet.Container(flet.Row([flet.Text("Generate", color=flet.colors.BLACK)], alignment="center"),
                                     bgcolor=flet.colors.WHITE, width=100, height=35, border_radius=11, on_click=self.page_three,
                                     disabled=True)
        main_column.controls.append(
            flet.Column([flet.Row([next_button], alignment="END")], alignment="END", expand=True))

        mother.update()
        page.update()

    def page_three(self, *args):
        page = self.page
        page.title = page.title
        mother = self.mother
        main_column = flet.Column()
        mother.content = main_column

        main_column.controls.append(flet.Text("\n\n"))

        Title1 = flet.Text("\n        Now🪄,\n        Just choose a template!!", color=flet.colors.WHITE, size=36, weight="bold")
        main_column.controls.append(Title1)

        describe = flet.Text(
            "                  Ok, what is a template ?.\n                  A template is a theme and pre-set page that make it quick to start.\n",
            color=flet.colors.WHITE60, size=15)
        main_column.controls.append(describe)

        r = flet.Row([
            self.make_a_template_button(flet.colors.WHITE24, "Blank new - default", "ADD_ROUNDED"),
            self.make_a_template_button(flet.colors.WHITE24, "Import template - soon", "GET_APP_OUTLINED", disable=True)
        ], alignment="center", spacing=15)
        main_column.controls.append(r)

        mother.update()
        page.update()

    def page_four(self, *args):
        page = self.page
        page.title = page.title
        mother = self.mother
        main_column = flet.Column()
        mother.content = main_column

        main_column.controls.append(flet.Text("\n\n"))

        Title1 = flet.Text("\n        Wait😄,\n        Building things for you.", color=flet.colors.WHITE, size=36, weight="bold")
        main_column.controls.append(Title1)

        mother.update()
        page.update()
        time.sleep(1)
        self.apply_suggestion_page()

    def apply_suggestion_page(self, *a):
        def dont_apply(e):
            Create_StoryBoard(self.file_name, "default", False)
            self.manage_class.file_name = self.file_name
            self.page.window_close()

        def apply_it(e):
            self.final_page_with_storyboard_suggest()

        page = self.page
        page.vertical_alignment = flet.MainAxisAlignment.CENTER
        page.title = page.title
        mother = self.mother
        main_column = flet.Column()
        mother.content = main_column
        col = main_column

        col.controls.append(flet.Row([flet.Text("", height=15)], alignment="center"))

        image = flet.Image(src="https://raw.githubusercontent.com/SKbarbon/Flet_StoryBoard/main/assets/IMG_3260.PNG",
                           width=250, height=250)
        col.controls.append(flet.Row([image], alignment="center"))

        title = flet.Text("Apply StoryBoard suggestions", size=20, weight="bold", color=flet.colors.WHITE)
        col.controls.append(flet.Row([title], alignment="center"))

        describe = flet.Text("""
        These are suggestions based on smart rules that help 
        you build your interface by suggesting 
        widgets based on your goal.
        """, size=13, color=flet.colors.WHITE)
        col.controls.append(flet.Row([describe], alignment="center"))

        apply_button = flet.ElevatedButton("Apply", bgcolor=flet.colors.WHITE, color=flet.colors.BLACK, width=250, on_click=apply_it)
        col.controls.append(flet.Row([apply_button], alignment="center"))

        no_btn = flet.TextButton(content=flet.Text("no thanks", color="red"), on_click=dont_apply)
        col.controls.append(flet.Row([no_btn], alignment="center"))

        mother.update()
        page.update()

    def final_page_with_storyboard_suggest(self):
        def apply_and_start(rule_name, rule_install_url):
            rules_file_content = requests.get(rule_install_url).text
            if not os.path.isdir("rules"):
                os.mkdir("rules")
            open(f"rules/{rule_name}.json", "w+", encoding="utf-8").write(str(rules_file_content))
            Create_StoryBoard(self.file_name, "default", True, rule_name)
            self.manage_class.file_name = self.file_name
            self.page.window_close()

        # ------
        page = self.page
        page.title = page.title
        mother = self.mother
        main_column = flet.Column()
        mother.content = main_column
        col = main_column
        col.scroll = True

        main_column.controls.append(flet.Text("\n\n"))

        Title1 = flet.Text("Choose your case.", color=flet.colors.WHITE, size=36, weight="bold")
        main_column.controls.append(flet.Row([Title1], alignment="center"))
        mother.update()
        describe = flet.Text("""
Choose your 'main' page goal from the 
options down bellow. This will install the right suggestions rules
for your main page case.
        """, size=13, color=flet.colors.WHITE)
        col.controls.append(flet.Row([describe], alignment="center"))
        mother.update()

        all_rules = requests.get("https://raw.githubusercontent.com/SKbarbon/Flet_StoryBoard/main/rules/all.json").text
        all_rules = json.loads(all_rules)

        for rule_option in all_rules["all_rules"]:
            col.controls.append(
                self.make_a_rule_button_option(rule_option, all_rules["all_rules"][rule_option], apply_and_start))

        col.scroll = True
        mother.update()

    def make_a_template_button(self, bgcolor, name, icon, disable=False):
        def on_hov(event):
            if event.data == "true":
                event.control.bgcolor = flet.colors.WHITE12
            elif event.data == "false":
                event.control.bgcolor = flet.colors.WHITE24
                event.control.update()
            event.control.update()

        cc = flet.Column(alignment="center", disabled=disable)
        c = flet.Container(width=220, height=140, bgcolor=bgcolor, border_radius=10, on_click=self.page_four,
                           on_hover=on_hov)
        cc.controls.append(c)

        Icon = flet.Icon(icon, size=20, color=flet.colors.WHITE)
        c.content = flet.Row([Icon], alignment="center")

        name_it = flet.Text(name, color=flet.colors.WHITE, size=13, text_align="center")
        cc.controls.append(flet.Row([name_it], alignment="center"))

        return cc

    def make_a_rule_button_option(self, name, url, on_click):
        def on_choose(e):
            on_click(name, url)

        b = flet.ElevatedButton(f"{name}", on_click=on_choose, bgcolor=flet.colors.WHITE, color=flet.colors.BLACK, width=150, height=45)

        return flet.Row([b], alignment="center")
