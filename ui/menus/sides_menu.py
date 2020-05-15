from tkinter import Canvas, NW, Button, Text, WORD, INSERT, Toplevel
from cv2 import cvtColor, imread, COLOR_BGR2RGB
import numpy as np
import PIL.Image
import PIL.ImageTk
from csv import *
import urllib.request
import helpers.resource_helper as rh
from ui.menus.base_menu import BaseMenu
from ui.map_ui import MapUi


class SidesMenu(BaseMenu):
    def __init__(self, caller, window, mapName, agent):
        self.mapName = mapName
        self.agentName = agent
        typeName = self.mapName + 'Sides'
        options = [
            "Attacker",
            "Both",
            "Defender"
        ]
        super().__init__(
            caller,
            window,
            options,
            typeName,
            MapUi,
            [self.agentName, self.mapName]
        )
