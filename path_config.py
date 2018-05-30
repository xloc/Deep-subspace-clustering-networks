import os

PROJECT_FOLDER = os.path.abspath(os.path.dirname(__file__))

def join(*args):
    return os.path.join(PROJECT_FOLDER, *args)
