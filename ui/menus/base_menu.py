from tkinter import Canvas, Toplevel, Text, NW, Button
from cv2 import cvtColor, imread, COLOR_BGR2RGB
import PIL.ImageTk
import urllib.request
from ui.base_ui import BaseUi
import helpers.resource_helper as rh


class BaseMenu(BaseUi):
    def __init__(self, caller, window, options, typeName, targetFunc, targetParams):
        self.options = options
        self.maxY = 600
        self.yModifier = self.maxY / len(options)
        self.typeName = typeName
        self.targetFunc = targetFunc
        self.targetParams = targetParams
        super().__init__(caller, window)
        self.setUp()

    def setUp(self):
        super().setUp(self.typeName, self.makeChoice)

    def makeChoice(self, event):
        self.canvas.pack_forget()

        for i in range(len(self.options)):
            minRange = i * self.yModifier
            maxRange = minRange + self.yModifier

            if minRange <= event.y < maxRange:
                self.B.destroy()
                newWindow = self.targetFunc(
                    self, self.window, self.options[i], *self.targetParams
                )

        if event.y > self.maxY:
            updateWindow = Toplevel(self.window)
            message = Text(updateWindow, height=6, width=75, wrap=WORD)
            message.insert(
                INSERT, 'Please update your application to include new resources')
            message.pack()
