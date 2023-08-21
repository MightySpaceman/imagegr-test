import os
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'dst/a32.exe')
os.startfile(filename)

def do_cvr():
    os.startfile(filename)