from tkinter import Tk
from pathlib import Path
from ui.menus.agent_menu import AgentMenu
import helpers.resource_helper as rh


class Main():
    def run(self):
        imgDirPath = rh.get_resource_path('Images')
        Path(imgDirPath).mkdir(exist_ok=True)

        locDirPath = rh.get_resource_path('Locations')
        Path(locDirPath).mkdir(exist_ok=True)

        locImgDirPath = rh.get_resource_path('LocationImages')
        Path(locImgDirPath).mkdir(exist_ok=True)

        window = Tk()
        window.title('Map Choice')

        start = AgentMenu(self, window)

    def setUp(self):
        exit()


if __name__ == "__main__":
    main = Main()
    main.run()
