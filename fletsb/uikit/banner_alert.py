import flet



def error_banner_alert (title:str, text:str):
    def dismiss (e):
        ban.open = False
        if ban.page != None:
            ban.update()
    
    #----
    col = flet.Column()
    ban = flet.Banner(
        content=flet.Row([
            flet.Container(bgcolor="#FF7F7F", height=70, width=5, border_radius=18),
            col
        ]),
        content_padding=15,
        actions=[
            flet.IconButton("CLOSE_ROUNDED", icon_color="black", icon_size=18, on_click=dismiss)
        ],
        bgcolor="#D9FFFFFF"
    )


    col.controls.append(flet.Row([
        flet.Text(title, color="#FF7F7F", weight=flet.FontWeight.BOLD, size=16)
    ]))

    col.controls.append(flet.Container(content=flet.Text(f"{text}", size=13, weight=flet.FontWeight.W_400, color="black")))


    return ban




if __name__ == "__main__":
    def test (page:flet.Page):
        page.banner = error_banner_alert(
            title="Hi",
            text="GG"
        )
        page.banner.open = True
        page.update()
    
    flet.app(target=test)