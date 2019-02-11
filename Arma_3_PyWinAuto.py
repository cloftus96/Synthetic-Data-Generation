# How to Open Arma 3 in Python using pywinauto
# make sure that the path here is identical to your Arma executable on your PC

# necessary imports
from pywinauto.application import Application

app = Application(backend="uia").start("C:\Program Files (x86)\Steam\steamapps\common\Arma 3\Arma3_x64.exe")
app.Arma3_x64.print_control_identifiers()