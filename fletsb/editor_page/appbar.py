from ..pages.settings.settings import SettingsPage
import flet
import flet_multi_page


class AppBar (object):
    def __init__(self, main_class) -> None:
        self.main_class = main_class
        self.page : flet.Page = main_class.page

        self.main_bar = flet.Container(
            width=self.page.width - 25, 
            height=50, 
            bgcolor="white", 
            border_radius=12
        )
        self.main_row = flet.Row(expand=True)
        self.main_bar.content = self.main_row

        self.title = flet.Text(
            "   Flet_StoryBoard", 
            size=16, 
            weight="bold", 
            color="black", 
            expand=True,
            semantics_label="Flet StoryBoard logo"
        )
        self.main_row.controls.append(flet.Column([
            self.title
        ]))

        self.appbar_tabs = ["Tutorials", "Lab", "Settings"]
        self.refresh()

    def phone_mode (self):
        self.main_row.controls.append(
            flet.IconButton(content=flet.Icon(
            name=flet.icons.MENU_ROUNDED, color="black", 
            size=20
            ), on_click=self.menu_sheet)
        )

    def pad_mode (self):
        # push tabs
        for item in self.appbar_tabs:
            self.main_row.controls.append(flet.TextButton(
                content=flet.Text(f"{item}", size=12, color="black"),
                on_click=self.tabs_manager,
                tooltip=f"The {item} tab"
            ))
        
        # preview btn
        preview_btn = flet.IconButton(content=flet.Icon(
            name=flet.icons.PREVIEW_ROUNDED,
            color="white",
            size=18
        ), width=35, height=35, tooltip="Start a preview in a new window")
        self.main_row.controls.append(flet.Container(content=preview_btn, bgcolor="blue", border_radius=preview_btn.width/4))

        # save btn
        save_btn = flet.TextButton(content=flet.Text("Save", color="white", size=14))
        self.main_row.controls.append(flet.Container(
            content=save_btn, 
            bgcolor="black", 
            border_radius=8, 
            width=100, 
            height=35,
            tooltip="Save | ctrl + S"
        ))

        # padding
        self.main_row.controls.append(flet.Text("  "))


    def menu_sheet (self, e=None):
        def close_sheet (e):
            if isinstance(e.control, flet.IconButton):
                remove_function()
                return
            if str(e.data).lower() == "false":
                remove_function()
                return
        
        c = flet.Container(
            bgcolor="white",
            width=self.page.width - 30,
            height=self.page.height - 60,
            border_radius=12,
            on_hover=close_sheet,
        )

        cc = flet.Column(alignment=flet.MainAxisAlignment.START, expand=True)
        c.content = cc

        r = flet.Row([
            flet.IconButton(content=flet.Icon(
                name=flet.icons.CLOSE_SHARP,
                color="black"
            ), on_click=close_sheet)
        ], alignment=flet.MainAxisAlignment.END)
        cc.controls.append(r)

        cc.controls.append(flet.Text("    Menu", size=20, weight=flet.FontWeight.BOLD, color=flet.colors.BLACK))

        for item in self.appbar_tabs:
            cc.controls.append(flet.Row([flet.TextButton(
                content=flet.Text(f"{item}", size=14, color="black", weight=flet.FontWeight.BOLD),
                on_click=self.tabs_manager,
                tooltip=f"The {item} tab"
            )], alignment="center"))

        remove_function = self.main_class.push_on_stack(flet.Column(controls=[
            flet.Row([
                c
            ], alignment=flet.MainAxisAlignment.CENTER, expand=True)
        ], alignment=flet.MainAxisAlignment.CENTER), with_bg_cover=True)
    
    
    def tabs_manager (self, e:flet.TapEvent):
        tab_name = str(e.control.content.value)
        if tab_name.lower() == "settings":
            sp = SettingsPage(main_class=self.main_class)
            remove_function = self.main_class.push_on_stack(sp.navigationview.view, with_bg_cover=True)
            sp.remove_the_bgcover = remove_function
        elif tab_name.lower() == "lab":
            pass
        elif tab_name.lower() == "tutorials":
            pass

    def refresh (self):
        self.main_row.controls.clear()
        self.main_row.controls.append(self.title)


        if self.page.width < 500:
            # if phone
            self.phone_mode()
        else:
            # if desktop, iPad or tablet
            self.pad_mode()