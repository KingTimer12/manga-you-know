import flet as ft
from screen.user_control.app_bar import NavBar
from screen.router_manager import Router


__version__ = '0.9.2b'


def __main__(page: ft.Page) -> ft.FletApp:
    page.title = f'MangaYouKnow {__version__}'
    page.theme_mode = 'dark'
    page.window_min_width = 770
    page.window_min_height = 600
    page.vertical_alignment = ft.CrossAxisAlignment.CENTER
    router = Router(page)
    page.on_route_change = router.route_change
    page.banner = NavBar(page)
    page.scroll = ft.ScrollMode.ADAPTIVE
    page.add(
        ft.Stack([
            ft.Column([
                router.body
            ],
            left=90,
            top=0
            ),
            router.reader
        ])
    )
    page.data = {} 
    page.data['reader_container'] = router.reader
    page.data['version'] = __version__
    page.go('/')
    page.update()
    