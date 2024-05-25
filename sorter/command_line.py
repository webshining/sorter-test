import json
import os
import shutil
from os.path import exists, isfile, join

SORTER_DIR = os.path.dirname(os.path.abspath(__file__))
CURRENT_DIR = os.getcwd()


def get_path(*paths: str):
    return join(CURRENT_DIR, *paths)


def sort():
    filegroups = dict(json.load(open(join(SORTER_DIR, 'filegroups.json')))).items()
    if exists(get_path("filegroups.json")):
        try:
            filegroups = dict(json.load(open(get_path("filegroups.json")))).items()
        except:
            pass
    for file in [f for f in os.listdir(get_path()) if isfile(get_path(f))]:
        for group, exts in filegroups:
            if file.split('.')[-1] in exts:
                if not exists(get_path(group)):
                    os.mkdir(get_path(group))
                shutil.move(get_path(file), get_path(group, file))
                break
