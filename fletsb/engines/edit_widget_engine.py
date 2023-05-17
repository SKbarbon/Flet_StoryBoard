import flet

from ..widgets.All import all_widgets
from ..tools.color_picker import ColorPicker
from ..tools.list_picker import ListPopup


class EditWidgetsEngine:
    def __init__(self, main_class, section_view: flet.Column, widget_number) -> None:
        self.main_class = main_class
        self.section_view = section_view
        self.widget_number = widget_number

        self.current_page_name = self.main_class.current_page_name
        self.all_fields = {}

        self.show_edit_tools()

    def show_edit_tools(self):
        self.section_view.clean()
        content = self.main_class.dict_content
        class_name = content["pages"][self.current_page_name]["widgets"][self.widget_number]["widget_class_name"]
        widget_content = content["pages"][self.current_page_name]["widgets"][self.widget_number]

        if class_name not in all_widgets:
            # if widget not found.
            self.section_view.controls.append(
                flet.Row(
                    [flet.Text(f"There is no supported\nwidget named '{class_name}'.", color=flet.colors.WHITE)]
                )
            )
            return

        the_class = all_widgets[class_name]["class"]
        the_class = the_class(
            self.main_class,
            self.main_class.preview_section.main_view,
            widget_number=self.widget_number
        )
        default_args = the_class.args

        title = flet.Text(f"Edit {class_name}", size=25, weight=flet.FontWeight.BOLD, color=flet.colors.WHITE)
        self.section_view.controls.append(title)

        for t in widget_content["properties"]:
            prop_name = t
            prop_value = widget_content["properties"][t]
            if prop_name not in default_args:
                print("Error while load widget properties in edit engine.")
                self.section_view.clean()
                return
            prop_type = default_args[prop_name]["type"]

            # These statements below are for adding the fields for edit a widget.
            if isinstance(prop_type(), str):
                tf = flet.TextField(width=160, bgcolor=flet.colors.WHITE, color=flet.colors.BLACK, label=prop_name)
                tf.value = prop_value
                self.section_view.controls.append(flet.Row([tf], alignment=flet.MainAxisAlignment.CENTER))
                self.all_fields[prop_name] = tf
                if "multi_line" in default_args[prop_name]:
                    tf.multiline = True

            elif type(prop_type()) == type(int()):
                slid = flet.Slider(min=0, max=500, divisions=500, label="{value}", width=160)
                slid.value = int(prop_value)
                self.section_view.controls.append(
                    flet.Row(
                        [
                            flet.Text(
                                f"{prop_name}:",
                                color=flet.colors.WHITE,
                                width=150
                            )
                        ], alignment=flet.MainAxisAlignment.CENTER
                    )
                )
                self.section_view.controls.append(
                    flet.Row(
                        [slid],
                        alignment=flet.MainAxisAlignment.CENTER
                    )
                )
                self.all_fields[prop_name] = slid

            elif type(prop_type()) == type(bool()):
                tog = flet.Switch()
                tog.value = prop_value
                self.section_view.controls.append(
                    flet.Row([flet.Text(f"{prop_name}", color=flet.colors.WHITE, size=13), tog],
                             alignment=flet.MainAxisAlignment.CENTER, spacing=25))
                self.all_fields[prop_name] = tog

            elif type(prop_type()) == type(ColorPicker()):
                self.section_view.controls.append(flet.Text(""))
                colp = ColorPicker(self.section_view, selected_color=prop_value, add_it=False, title_name=prop_name,
                                   drop_width=120)
                self.section_view.controls.append(flet.Row([colp.v], alignment=flet.MainAxisAlignment.CENTER))
                self.all_fields[prop_name] = colp

            elif isinstance(prop_type(), list):
                dr = flet.Dropdown(width=160, label=prop_name)
                for i in default_args[prop_name]["options"]:
                    dr.options.append(flet.dropdown.Option(f"{i}"))
                dr.value = prop_value
                self.section_view.controls.append(flet.Row([dr], alignment=flet.MainAxisAlignment.CENTER))
                self.all_fields[prop_name] = dr

            elif type(prop_type()) == type(ListPopup()):
                lp = ListPopup(default_args[prop_name]["options"], self.main_class, prop_value, prop_name)
                self.section_view.controls.append(flet.Row([lp.self_ui], alignment=flet.MainAxisAlignment.CENTER))
                self.all_fields[prop_name] = lp

        # This button below for widgets that support sub-widgets.
        if hasattr(the_class, "support_sub_widgets"):
            add_sub_widget_button = flet.TextButton("Add sub-widget", on_click=the_class.widgets_to_add_in)
            self.section_view.controls.append(
                flet.Row(
                    [add_sub_widget_button],
                    alignment=flet.MainAxisAlignment.CENTER
                )
            )

        # This slider bellow is for rearrange the widget on the page.
        rearrange_slider = flet.Slider(
            min=0,
            max=len(content["pages"][self.current_page_name]["widgets"]),
            value=self.widget_number,
            label="{value}",
            width=160,
            divisions=len(content["pages"][self.current_page_name]["widgets"])
        )
        self.section_view.controls.append(
            flet.Row(
                [flet.Text(f"reArrange:", color=flet.colors.WHITE, width=150)],
                alignment=flet.MainAxisAlignment.CENTER
            )
        )
        self.section_view.controls.append(flet.Row([rearrange_slider], alignment=flet.MainAxisAlignment.CENTER))
        self.rearrange_slider = rearrange_slider

        self.section_view.controls.append(flet.Text("\n"))
        # Down bellow is for done_button and delete_btn.
        done_button = flet.ElevatedButton(
            "Done",
            bgcolor=flet.colors.WHITE,
            color=flet.colors.BLACK,
            width=150,
            height=40,
            on_click=self.done_edit
        )
        self.section_view.controls.append(
            flet.Row(
                [done_button],
                alignment=flet.MainAxisAlignment.CENTER
            )
        )

        delete_button = flet.TextButton(
            content=flet.Text("delete", color=flet.colors.RED, size=13),
            on_click=self.delete_widget
        )
        self.section_view.controls.append(
            flet.Row(
                [delete_button],
                alignment=flet.MainAxisAlignment.CENTER
            )
        )

    def done_edit(self, *args):
        new_widget_properties_dict = {}
        for P in self.all_fields:
            new_widget_properties_dict[P] = self.all_fields[P].value

        if int(self.widget_number) == int(self.rearrange_slider.value):
            # If the widget arrange is the same.
            self.main_class.dict_content["pages"][self.current_page_name]["widgets"][self.widget_number][
                "properties"].update(new_widget_properties_dict)
        else:
            # If the widget arrange is NOT the same.
            if int(self.rearrange_slider.value) >= int(
                    len(self.main_class.dict_content["pages"][self.main_class.current_page_name]["widgets"])):
                self.main_class.dict_content["pages"][self.current_page_name]["widgets"][self.widget_number][
                    "properties"].update(new_widget_properties_dict)
                copy_of_content = self.main_class.dict_content["pages"][self.current_page_name]["widgets"][
                    self.widget_number]
                del self.main_class.dict_content["pages"][self.current_page_name]["widgets"][self.widget_number]

                self.main_class.dict_content["pages"][self.current_page_name]["widgets"].append(copy_of_content)

                self.widget_number = int(
                    len(self.main_class.dict_content["pages"][self.current_page_name]["widgets"]) - 1)
            else:
                self.main_class.dict_content["pages"][self.current_page_name]["widgets"][self.widget_number][
                    "properties"].update(new_widget_properties_dict)
                copy_of_content = self.main_class.dict_content["pages"][self.current_page_name]["widgets"][
                    self.widget_number]

                self.main_class.dict_content["pages"][self.current_page_name]["widgets"][
                    int(self.rearrange_slider.value)] = copy_of_content
                del self.main_class.dict_content["pages"][self.current_page_name]["widgets"][self.widget_number]

                self.widget_number = int(self.rearrange_slider.value)

        # Update the viewer engine to see the edit changes.
        self.main_class.preview_section.update_preview(self.main_class.current_page_name)
        self.main_class.page.update()

        # ReOpen the editor again
        EditWidgetsEngine(
            main_class=self.main_class,
            section_view=self.section_view,
            widget_number=self.widget_number
        )
        self.main_class.page.update()

    def delete_widget(self, *args):
        del self.main_class.dict_content["pages"][self.current_page_name]["widgets"][self.widget_number]
        self.section_view.clean()

        # Update the viewer engine to see the edit changes.
        self.main_class.preview_section.update_preview(self.main_class.current_page_name)
        self.main_class.page.update()
