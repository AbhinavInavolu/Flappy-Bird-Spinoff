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
    Icon = resource_path("icon.xcf")
    Progress = resource_path("Progress.json")

    Main(Icon, Progress)
    
