import flet


class ListPopup:
    def __init__(self, the_list=None, main_class=None, default_choice=None, title=None):
        if the_list is None:
            return

        self.title = title
        self.page: flet.Page = main_class.page
        self.main_class = main_class
        self.self_ui = flet.TextButton(f"{title}: f{default_choice}", on_click=self.show_popup)
        self.the_list = the_list
        self.__selected = default_choice

    def show_popup(self, *args):
        def on_search(e):
            for i in self.all_list_choices:
                col.controls.remove(i)

            self.all_list_choices = []

            if search_field.value == "":
                for icon in self.the_list:
                    name = str(icon)
                    if name.startswith("__"):
                        pass
                    else:
                        self.all_list_choices.append(self.generate_new(name, col))
                col.update()
                return

            self.all_list_choices = []
            self.all_list_choices.clear()
            s = str(search_field.value).lower()

            for i in self.the_list:
                name = str(i)
                if str(i).lower().startswith(s):
                    self.all_list_choices.append(self.generate_new(name, col))
            col.update()

        page: flet.Page = self.main_class.page

        cont = flet.Container(bgcolor="#333333", border_radius=12)
        loading_text = flet.Text("Loading..", color=flet.colors.WHITE)
        cont.content = flet.Row([loading_text], alignment=flet.MainAxisAlignment.CENTER, height=100)

        page.dialog = flet.AlertDialog()
        page.dialog.content = cont
        page.dialog.open = True
        page.update()

        col = flet.ListView(width=450, height=500)
        col.controls.append(flet.Text("Choose one:", color="white", size=28, weight=flet.FontWeight.BOLD))

        search_field = flet.TextField(label="Search", on_change=on_search)
        col.controls.append(search_field)

        self.all_list_choices = []
        for icon in self.the_list:
            name = str(icon)
            if name.startswith("__"):
                pass
            else:
                self.all_list_choices.append(self.generate_new(name, col))

        cont.content = col
        page.update()

    def generate_new(self, value_name, col):
        def on_choose(e):
            self.self_ui.text = f"{self.title}: f{value_name}"
            self.__selected = value_name
            self.page.dialog.open = False
            self.page.update()

        r = flet.Row(
            [
                flet.Icon(value_name, size=22, color=flet.colors.WHITE),
                flet.Text(f"{value_name}", color=flet.colors.WHITE)
            ]
        )
        cc = flet.Container(content=r, on_click=on_choose)
        col.controls.append(cc)
        return cc

    @property
    def value(self):
        return self.__selected
