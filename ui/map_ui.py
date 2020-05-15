from tkinter import Canvas, NW, Button, Text, WORD, INSERT, Toplevel
from cv2 import cvtColor, imread, COLOR_BGR2RGB
import numpy as np
import PIL.Image
import PIL.ImageTk
from csv import *
import urllib.request
import helpers.resource_helper as rh
from ui.base_ui import BaseUi


class MapUi(BaseUi):
    def __init__(self, caller, window, side, agent, mapName):
        self.mapName = mapName
        self.agentName = agent
        self.sideName = side
        self.typeName = None
        super().__init__(caller, window)
        self.setUp()

    def setUp(self):
        self.window.title(self.mapName + self.sideName)

        cv_img = rh.get_image(self.mapName)

        if (self.sideName == "Both"):
            attack_locs = rh.get_csv(self.agentName, self.mapName, "Attacker")
            defend_locs = rh.get_csv(self.agentName, self.mapName, "Defender")
            self.locs = np.concatenate((attack_locs, defend_locs))
        else:
            self.locs = rh.get_csv(self.agentName, self.mapName, self.sideName)

        self.locCount = self.locs.shape[0]

        super().setUp(self.mapName, self.posCheck, self.preloopFunc)

    def preloopFunc(self):
        for x in range(0, self.locCount):
            if (int(self.locs[x, 0]) % 2) == 0:
                self.canvas.create_rectangle(int(self.locs[x, 1]), int(self.locs[x, 2]), (int(
                    self.locs[x, 1])+12), (int(self.locs[x, 2])+12), fill='blue')
            else:
                self.canvas.create_rectangle(int(self.locs[x, 1]), int(self.locs[x, 2]), (int(
                    self.locs[x, 1])+12), (int(self.locs[x, 2])+12), fill='red')

    def posCheck(self, event):
        print(str(event.x) + ', ' + str(event.y))
        for x in range(0, self.locCount):
            if int(self.locs[x, 1]) < event.x < (int(self.locs[x, 1]) + 12):
                if int(self.locs[x, 2]) < event.y < (int(self.locs[x, 2]) + 12):
                    locWindow = Toplevel(self.window)
                    locWindow.title(str(int(self.locs[x, 0])))

                    locMessage = str(self.locs[x, 3])[1:]
                    message = Text(locWindow, height=6, width=75, wrap=WORD)
                    message.insert(INSERT, locMessage)
                    message.pack()

                    cv_img = rh.get_location_image(
                        self.agentName,
                        self.mapName,
                        str(int(self.locs[x, 0]))
                    )
                    height, width, ne_channels = cv_img.shape

                    canvas = Canvas(locWindow, width=width, height=height)
                    canvas.pack()

                    photo = PIL.ImageTk.PhotoImage(
                        image=PIL.Image.fromarray(cv_img))
                    canvas.create_image(0, 0, image=photo, anchor=NW)
                    self.window.mainloop()
