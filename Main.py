from Logic import Main
import os
import sys


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


if __name__ == "__main__":
    icon = resource_path(r"images\icon.xcf")
    progress = resource_path(r"data\Progress.json")
    back = resource_path(r"images\back.png")

    Main(icon, progress, back)

    