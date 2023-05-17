import flet

from ...tools.color_picker import ColorPicker


def page_settings_page(settings_class):
    def allow_scrolling(e):
        settings_class.main_class.dict_content["storyboard_settings"]["allow_scroll"] = e.control.value
        page: flet.Page = settings_class.page
        page.show_snack_bar(
            flet.SnackBar(
                flet.Text(f"Done! But this is not saved, you must go click 'Save' on the editor."),
                open=True
            )
        )
        settings_class.main_class.preview_section.update_preview()
        page.update()

    def on_change_bgcolor(color):
        settings_class.main_class.dict_content["pages"][current_page_name]["settings"]["bgcolor"] = color
        page: flet.Page = settings_class.page
        page.show_snack_bar(
            flet.SnackBar(
                flet.Text(f"Done! But this is not saved, you must go click 'Save' on the editor."),
                open=True
            )
        )
        settings_class.main_class.preview_section.update_preview()
        page.update()

    v = settings_class.page_viewing_section
    v.clean()

    current_page_name = settings_class.main_class.current_page_name
    title = flet.Text(
        f"\n   Pages - {current_page_name}",
        color=flet.colors.WHITE,
        weight=flet.FontWeight.BOLD,
        size=28
    )
    v.controls.append(title)

    if "allow_scroll" not in settings_class.main_class.dict_content["storyboard_settings"]:
        settings_class.main_class.dict_content["storyboard_settings"]["allow_scroll"] = False

    row_allow_scrolling = flet.Row(
        [
            flet.Text("Allow scrolling", color="white", width=300),
            flet.Switch(
                on_change=allow_scrolling,
                value=settings_class.main_class.dict_content["storyboard_settings"]["allow_scroll"]
            )
        ],
        alignment=flet.MainAxisAlignment.CENTER
    )
    v.controls.append(row_allow_scrolling)

    cp = ColorPicker(v, settings_class.main_class.dict_content["pages"][current_page_name]["settings"]["bgcolor"],
                     on_choose_color=on_change_bgcolor, add_it=False, title_name="bgcolor")
    v.controls.append(
        flet.Container(
            flet.Row(
                [cp.v],
                alignment=flet.MainAxisAlignment.CENTER
            ),
            bgcolor=flet.colors.BLACK
        )
    )

    v.update()
