import flet as ft

def main(page: ft.Page):
    page.title = "avoe.dev ECO project"
    

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
                            [ft.ElevatedButton("Learn more",icon=ft.icons.INSERT_LINK_OUTLINED),ft.ElevatedButton("Report a bug",icon=ft.icons.BUG_REPORT), ft.ElevatedButton("Support project",icon=ft.icons.ATTACH_MONEY)],
                            alignment=ft.MainAxisAlignment.END,
                        ),
                    ]
                ),
                padding=10,
                bgcolor=ft.colors.PURPLE,
                border_radius=10,
                alignment=ft.alignment.top_center
            )
        ),
        ft.Row(
            
        )
    )


ft.app(main)