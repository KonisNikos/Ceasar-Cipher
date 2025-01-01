DEFAULT_RESOLUTION = (1424, 800)
BACKGROUND_COLOR = "#0f172a"
ACTIVE_BACKGROUND_COLOR = "#020617"
FOREGROUND_COLOR = "#ffffff"
FONT_NAME = "Helvetica"
FONT_SIZE = 16

def apply_text_styles(widget_function):
    """Applies styles for widgets which contain text"""
    def inner(*args, **kargs):
        kargs.setdefault("bg", BACKGROUND_COLOR)
        kargs.setdefault("fg", FOREGROUND_COLOR)
        kargs.setdefault("font", (FONT_NAME, FONT_SIZE))
        return widget_function(*args, **kargs)
    return inner