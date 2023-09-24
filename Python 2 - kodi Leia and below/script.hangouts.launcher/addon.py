import xbmc
import subprocess
import os 
child = subprocess.call([os.environ['localappdata'] + '\\Google\\Chrome\\Application\\Chrome.exe',"--kiosk","hangouts.google.com"])
