from tkinter import Canvas, Toplevel, Text, NW
from cv2 import cvtColor, imread, COLOR_BGR2RGB
import PIL.ImageTk
import urllib.request
import helpers.resource_helper as rh
from ui.menus.base_menu import BaseMenu
from ui.menus.map_menu import MapMenu


class AgentMenu(BaseMenu):
    def __init__(self, caller, window):
        options = [
            "Sova",
            "Viper",
            "Cypher",
            "Brimstone"
        ]
        typeName = 'AgentList'
        super().__init__(
            caller,
            window,
            options,
            typeName,
            MapMenu,
            []
        )
