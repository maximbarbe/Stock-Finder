import os
import shutil

# Check if folder exists, if not, it creates it. If it exists, it deletes everything in the folder and creates another one.
def create_folder():
    
    try:
        os.mkdir("./stock")
    except OSError:
        shutil.rmtree("./stock")
        os.mkdir("./stock")


