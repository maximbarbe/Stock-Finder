import os
import shutil
def create_folder():
    
    try:
        os.mkdir("./stock")
    except OSError:
        shutil.rmtree("./stock")
        os.mkdir("./stock")


