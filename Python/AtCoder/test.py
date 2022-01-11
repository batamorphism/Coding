import os
import subprocess

print(os.environ.get("APPDATA"))
# open appdata
subprocess.Popen(r'explorer ' + os.environ.get("APPDATA"))

