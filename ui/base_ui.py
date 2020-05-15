import os.path as path
from tkinter import Canvas, Toplevel, Text, NW, Button
from cv2 import cvtColor, imread, COLOR_BGR2RGB
import PIL.ImageTk
import urllib.request
import helpers.resource_helper as rh


class BaseUi:
    def __init__(self, caller, window):
        self.caller = caller
        self.window = window

    def setUp(self, nameOfImage, targetFunc, preloopFunc=None):
        cv_img = rh.get_image(nameOfImage)

        self.height, self.width, ne_channels = cv_img.shape

        self.canvas = Canvas(self.window, width=self.width, height=self.height)
        self.canvas.bind("<Button 1>", targetFunc)

        self.canvas.pack()

        photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img))
        self.canvas.create_image(0, 0, image=photo, anchor=NW)

        buttonText = "Back"
        if self.typeName == "AgentList":
            buttonText = "Exit"
        self.B = Button(self.window, text=buttonText, command=lambda: [
            self.B.destroy(), self.canvas.pack_forget(), self.caller.setUp()
        ])
        self.B.pack()

        if (preloopFunc):
            preloopFunc()

        self.window.mainloop()
