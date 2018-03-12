import os

PATH=os.path.dirname(os.path.abspath(__file__))

if "JUPYTER_PATH" in os.environ:
    os.environ["JUPYTER_PATH"] = PATH + os.pathsep + os.environ["JUPYTER_PATH"]
else:
    os.environ["JUPYTER_PATH"] = PATH

import webbrowser

class Private(webbrowser.Mozilla):
    remote_action = "--private-window"

webbrowser.register("private", None, Private("firefox"))

c.NotebookApp.browser = 'private'
c.NotebookApp.webbrowser_open_new = 0
