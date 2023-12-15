import flet, time




class NotificationAlert (flet.Container):
    def __init__ (self, icon:str, icon_color:str, title:str, on_clicked=None, column_of_currently_presented_notifications=None):
        super().__init__()
        self.column_of_currently_presented_notifications = column_of_currently_presented_notifications
        self.title = title
        self.icon = icon
        self.icon_color = icon_color
        self.on_click_alert = on_clicked

        self.bgcolor = flet.colors.WHITE
        self.padding = 15
        self.width = 350
        self.height = 65
        self.border_radius = 18

        if on_clicked != None:
            self.on_click = self.on_alert_clicked

        self.content = flet.Row([
            flet.Icon(name=icon, color=icon_color),
            flet.Text(value=title, color="black", expand=True)
        ])
    

    def push(self):
        title = self.title
        icon = self.icon
        icon_color = self.icon_color
        on_click = self.on_click_alert

        def dismiss ():
            anim_switchr.content = flet.Text("")
            anim_switchr.update()
            time.sleep(1)
            self.column_of_currently_presented_notifications.controls.remove(anim_switchr)
            self.column_of_currently_presented_notifications.update()
        # --------
        alert_d = flet.Row([
            NotificationAlert(
                icon=icon,
                icon_color=icon_color,
                title=title
            )
        ], alignment=flet.MainAxisAlignment.CENTER)


        anim_switchr = flet.AnimatedSwitcher(content=flet.Text(""), duration=200, animate_opacity=200)
        self.column_of_currently_presented_notifications.controls.append(anim_switchr)
        self.column_of_currently_presented_notifications.update()

        time.sleep(0.5)
        anim_switchr.content = alert_d
        anim_switchr.update()

        if on_click == None:
            time.sleep(8)
            dismiss()
        else:
            time.sleep(20)
            dismiss()
    

    def on_alert_clicked (self, e):
        self.on_click_alert()