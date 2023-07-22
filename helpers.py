import os

def check_folder_existing():
    try:
        os.mkdir("./stock")
    except OSError:
        return