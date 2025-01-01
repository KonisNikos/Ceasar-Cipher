from sys import platform
import ctypes
from ctypes import wintypes
from src.gui.geometry import Vector
def get_screen_dimentions(window):
    if platform != "win32":
        #If the os is not windows it assumes that no menu bar exists
        #Thus functions like centering are not gonna be exactly accurate
        #TODO make it accurate for different linux windows managers
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        return Vector(screen_width, screen_height)

    #0x30 = is the SPI_GETWORKAREA argument according to windows docs
    ui_action = wintypes.UINT(0x30)
    rect_object = wintypes.RECT()
    ctypes.windll.user32.SystemParametersInfoW(
        ui_action, None, ctypes.byref(rect_object), None
    )
    screen_width = rect_object.right - rect_object.left
    screen_height = rect_object.bottom - rect_object.top
    return Vector(screen_width, screen_height)
