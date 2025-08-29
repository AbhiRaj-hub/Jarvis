import os
import subprocess as sp

def open_camera():
    sp.run('start microsoft.windows.camera:', shell=True)

def open_cmd():
    os.system('start cmd')
