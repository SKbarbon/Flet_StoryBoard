import flet
import time
import random
import os
import threading
import random

# local imports
from .built_in_widgets.color_picker import colorPicker
from .tools.create_storyboard_file import createStoryboardFile

class CreateStoryBoard :

    def __init__ (self):
        def run (page:flet.Page):
            self.page = page
            page.title = "Create new StoryBoard!"
            page.window_resizable = False
            page.window_center()
            page.bgcolor = "white"
            page.theme = flet.Theme(color_scheme_seed="white")
            page.vertical_alignment = flet.MainAxisAlignment.CENTER
            page.update()
            
            self.__page_one()

            page.window_center()
            page.update()
        flet.app(run)
    
    def create_the_storyboard (self, *args):
        anm = self.animated_view
        main = flet.Container()
        mainc = flet.Column()
        main.content = mainc

        mainc.controls.append(flet.Text("\n\n"))

        Teas_Title = flet.Text("          Building things,\n          Just for you.", weight="bold", size=45, color="white")
        mainc.controls.append(Teas_Title)

        mainc.controls.append(flet.Text("\n\n\n\n"))

        Loading = flet.Text("🏃‍♀️.", color="white", size=20)
        mainc.controls.append(flet.Row([Loading], alignment="center"))

        hints = ["you can click settings tab to edit the page settings", "you can set the page to make it auto full screen!",
        f"Flet website: https://flet.dev"]
        hint_text = flet.Text(f"short info: {random.choice(hints)}", color="white", size=10)
        mainc.controls.append(flet.Row([hint_text], alignment="center"))

        anm.content = main
        anm.update()

        Loading.value = Loading.value + "."
        Loading.update()
        time.sleep(1.5)
        createStoryboardFile(self.PAGE_NAME, self.page_bg_color_selected.selected_color)
        Loading.value = Loading.value + "."
        Loading.update()
        time.sleep(0.5)
        Loading.value = Loading.value + "."
        Loading.update()
        if os.path.isfile(f"{self.PAGE_NAME}.fletsb"):
            Loading.value = Loading.value + "✅"
            Loading.update()
        else:
            Loading.value = "There is error wile creating the file!"
            Loading.color = "red"
            Loading.update()
        time.sleep(1.5)
        self.page.window_close()
        

    def __page_one (self):
        # To set page's title.
        page : flet.Page = self.page
        page.clean()

        m = flet.Row(alignment="center", expand=True)
        page.add(m)

        dt = flet.Text("Create a StoryBoard!", color="white")
        ShowCaseBtn = flet.Container(content=flet.Row(alignment="center", controls=[dt])
        , width=220, height=50, border_radius=10, bgcolor="black")
        m.controls.append(ShowCaseBtn)
        page.update()

        time.sleep(0.3)

        current_wid = ShowCaseBtn.width
        current_hei = ShowCaseBtn.height

        for i in range(30):
            ShowCaseBtn.width = ShowCaseBtn.width - 0.5
            ShowCaseBtn.height = ShowCaseBtn.height - 0.2
            ShowCaseBtn.update()
            # time.sleep(0.001)
            time.sleep(i/450)

        page.bgcolor = "black"
        dt.color = "black"
        ShowCaseBtn.bgcolor = "white"
        page.update()
        
        while ShowCaseBtn.width != current_wid and ShowCaseBtn.height != current_hei:
            if ShowCaseBtn.width != current_wid: ShowCaseBtn.width = ShowCaseBtn.width + 0.1
            if ShowCaseBtn.height != current_hei: ShowCaseBtn.height = ShowCaseBtn.height + 0.1
            ShowCaseBtn.update()
            time.sleep(0.002)
        
        for i in range(10):
            ShowCaseBtn.opacity = ShowCaseBtn.opacity - 0.1
            ShowCaseBtn.update()
            time.sleep(0.001)
        m.controls.remove(ShowCaseBtn)
        m.update()
        
        page.clean()
        page.update()

        
        main = flet.Container(expand=True, opacity=0.0)
        mainc = flet.Column()
        main.content = mainc

        animated = flet.AnimatedSwitcher(content=main, expand=True,
        transition=flet.AnimatedSwitcherTransition.FADE, duration=3000,
        reverse_duration=100, switch_in_curve=flet.AnimationCurve.EASE,
        switch_out_curve=flet.AnimationCurve.EASE)
        self.animated_view = animated
        page.add(animated)


        mainc.controls.append(flet.Text("\n\n"))

        Teas_Title = flet.Text("          Your imagine.\n          With ease.", weight="bold", size=45, color="white")
        mainc.controls.append(Teas_Title)

        mainc.controls.append(flet.Text(
        "                             Its so easy to build your UI\n                             using your imagine and Flet Storyboard."
        , color="white"))

        mainc.controls.append(flet.Text("\n\n\n\n\n"))

        NextButton = flet.Container(content=flet.Row([flet.Text("Build your's!", color="black", weight="bold")], alignment="center")
        , bgcolor="white", width=page.width/2, height=50,
        border_radius=10, on_click=self.__page_two)
        mainc.controls.append(flet.Row([NextButton], alignment="center"))


        for i in range(10):
            main.opacity = main.opacity + 0.1
            main.update()
            time.sleep(0.02)

        page.update()
    

    def __page_two (self, *args):
        def on_change_app_name (tf):
            text = InputStoryboardName.value
            win_theme[0].value = text
            self.PAGE_NAME = text
            if os.path.isfile (f"{text}.fletsb"):
                InputStoryboardName.focused_color = flet.colors.AMBER
                InputStoryboardName.label = "There is a file with same name"
            else:
                InputStoryboardName.focused_color = flet.colors.BLUE
                InputStoryboardName.label = "App title"
            self.page.update()
    
        page : flet.Page = self.page

        self.done_page_two = False
        main = flet.Container(expand=True)
        mainc = flet.Column()
        main.content = mainc
        animated = self.animated_view
        animated.content = main

        mainc.controls.append(flet.Text("\n\n"))

        Teas_Title = flet.Text("          Your App.\n          Your title.", weight="bold", size=45, color="white")
        mainc.controls.append(Teas_Title)

        mainc.controls.append(flet.Text(
        "                             Set your app name that will be displayed\n                             on the top bar of the app"
        , color="white"))

        mainc.controls.append(flet.Text("\n"))

        InputStoryboardName = flet.TextField(bgcolor="white", width=250, text_size=18, color="black", 
        border_radius=12, on_change=on_change_app_name, on_submit=self.__page_three, label="App title", 
        focused_border_color=flet.colors.BLACK45)
        mainc.controls.append(flet.Row([InputStoryboardName], alignment="center"))

        mainc.controls.append(flet.Text("\n\n"))
        win_theme = window_theme (mainc)

        page.update()

        def after_a_while ():
            time.sleep(10)
            if self.done_page_two == False:
                page.title = str(page.title) + " - Click enter on the textfield after the end."
                page.update()
        threading.Thread(target=after_a_while, daemon=True).start()
    
    def __page_three (self, *args):
        def on_change_bgcolor (color):
            wn[1].bgcolor = color
            wn[1].update()

        self.done_page_two = True
        page = self.page
        page.title = str(page.title).replace(" - Click enter on the textfield after the end.", "")
        page.update()
        animated = self.animated_view
        main = flet.Container(expand=True)
        mainc = flet.Column()
        main.content = mainc

        mainc.controls.append(flet.Text("\n\n"))

        Teas_Title = flet.Text("          Customize.\n          The bgcolor.", weight="bold", size=45, color="white")
        mainc.controls.append(Teas_Title)

        mainc.controls.append(flet.Text(
        "                             Set your app background color.\n                             It always good.",
        color="white"))

        mainc.controls.append(flet.Text("\n"))

        cp = colorPicker(mainc, add_it=False, on_choose_color=on_change_bgcolor)
        self.page_bg_color_selected = cp
        mainc.controls.append(flet.Row([cp.v], alignment="center"))

        next_button = flet.Container(content=flet.Row([flet.Text("Done!", color="black", size=13)], alignment="center"), bgcolor="white", width=85,
        height=30, border_radius=8, on_click=self.create_the_storyboard)
        mainc.controls.append(flet.Row([next_button], alignment="center"))
        
        mainc.controls.append(flet.Text("\n\n"))
        wn = window_theme (mainc, self.PAGE_NAME)

        animated.content = main
        animated.update()
        cp.mainDropdown.focus()





# tools
def none(*args):
    pass
def window_theme (view:flet.Column, app_title="App"):

    App_Title = flet.Text(app_title, color="black", expand=True)

    top_bar = flet.Row(controls=[
        flet.Text(" "),
        flet.Icon(flet.icons.EMOJI_EMOTIONS, color="black", size=20),
        App_Title,
        flet.Row(controls=[
            flet.Container(width=15, height=15, bgcolor="red", border_radius=7.5, on_hover=none),
            flet.Container(width=15, height=15, bgcolor="yellow", border_radius=7.5, on_hover=none),
            flet.Container(width=15, height=15, bgcolor="green", border_radius=7.5, on_hover=none),
            flet.Text("  ")
        ],alignment="left")
    ])
    mv = flet.Column(controls=[
        flet.Text("", height=5),
        flet.Container(top_bar, border=flet.border.only(bottom=flet.border.BorderSide(0.3, "black")), bgcolor="white"),
        flet.Text("", height=5)
    ])

    main_cont = flet.Container(mv, width=450, height=300, bgcolor="white", border_radius=10)

    view.controls.append(flet.Row([main_cont], alignment="center"))
    return App_Title, main_cont