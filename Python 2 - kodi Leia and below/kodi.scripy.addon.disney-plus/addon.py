import xbmc
import subprocess
import os
child = subprocess.call([os.environ['programfiles(x86)'] + '\\Google\\Chrome\\Application\\Chrome.exe',"--kiosk","https://www.disneyplus.com/pl-pl/home"])