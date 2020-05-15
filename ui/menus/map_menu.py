from tkinter import Canvas, Toplevel, Text, NW, Button
from cv2 import cvtColor, imread, COLOR_BGR2RGB
import PIL.ImageTk
import urllib.request
import helpers.resource_helper as rh
from ui.menus.base_menu import BaseMenu
from ui.menus.sides_menu import SidesMenu


class MapMenu(BaseMenu):
    def __init__(self, caller, window, agent):
        options = [
            "Bind",
            "Haven",
            "Split"
        ]
        typeName = 'MapList'
        super().__init__(
            caller,
            window,
            options,
            typeName,
            SidesMenu,
            [agent]
        )
