

from _app_imp import Application

_application = None

def get_application():
    global _application
    if not _application:
        _application = Application()
    return _application


def add_settings(settings):
    app = get_application()
    return app.add_settings(settings)


def show_settings():
    app = get_application()
    app.show_settings()
