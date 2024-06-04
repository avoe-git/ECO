import flet as ft

def main(page: ft.Page):
    page.window_height=640
    page.window_width=360
    page.title = "avoe.dev ECO project"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    def isbannertrue_fun(isbannertrue):
        isbannertrue=True
        return isbannertrue
    

    page.add(
        ft.Card(
            content=ft.Container(
                content=ft.Column(
                    [
                        ft.ListTile(
                            leading=ft.Icon(ft.icons.DANGEROUS_OUTLINED),
                            title=ft.Text("Project is under development! There may be many errors and bugs, please report a bug if you found any. Thank you!")
                        ),
                        ft.Row(
                            [ft.ElevatedButton("Learn more",icon=ft.icons.INSERT_LINK_OUTLINED),ft.ElevatedButton("Report a bug",icon=ft.icons.BUG_REPORT,on_click=isbannertrue_fun), ft.ElevatedButton("Support project",icon=ft.icons.ATTACH_MONEY)],
                            alignment=ft.MainAxisAlignment.END,
                        ),
                    ]
                ),
                padding=10,
                border_radius=10,
                alignment=ft.alignment.top_center
            )
        ),
        ft.Banner(
            ft.Row([
                ft.Text("Development mode"),
                ft.ElevatedButton("Learn more"),
                ft.ElevatedButton("Dismiss"),
            ]),
            bgcolor="gray",
            open=True
        ),
    )


ft.app(main)