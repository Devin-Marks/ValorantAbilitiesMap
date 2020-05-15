import os.path as path
from os.path import join, abspath
import sys
import numpy as np
import urllib.request
from cv2 import cvtColor, imread, COLOR_BGR2RGB


def get_resource_path(relative_path: str) -> str:
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = abspath(".")

    return join(base_path, relative_path)


def get_image(name: str):
    imgName = 'Images\\' + name + '.png'
    imgPath = get_resource_path(imgName)

    if (path.exists(imgPath) == False):
        url = f'https://valmap.s3.amazonaws.com/{name}.png'

        with urllib.request.urlopen(url) as response, open(imgPath, 'wb') as out_file:
            data = response.read()
            out_file.write(data)

    return cvtColor(imread(imgPath), COLOR_BGR2RGB)


def get_location_image(agent, mapName, loc):
    picName = 'LocationImages\\' + agent + mapName + loc + '.png'
    picPath = get_resource_path(picName)
    if (path.exists(picPath) == False):
        url = 'https://valmap.s3.amazonaws.com/' + \
            agent + '/' + agent + mapName + loc + '.png'

        with urllib.request.urlopen(url) as response, open(picPath, 'wb') as out_file:
            data = response.read()
            out_file.write(data)

    return cvtColor(imread(picPath), COLOR_BGR2RGB)


def get_csv(agent: str, mapName: str, side: str):
    fileName = 'Locations\\' + agent + mapName + side + '.csv'
    filePath = get_resource_path(fileName)

    if (path.exists(filePath) == False):
        url = 'https://valmap.s3.amazonaws.com/' + self.agentName + \
            '/' + self.agentName + self.mapName + 'Attacker.csv'

        with urllib.request.urlopen(url) as response, open(filePath, 'wb') as out_file:
            data = response.read()
            out_file.write(data)

    return np.genfromtxt(filePath, delimiter='|', dtype='S400')
