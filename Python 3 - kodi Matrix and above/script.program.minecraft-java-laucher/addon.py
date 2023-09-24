import xbmc
import xbmcaddon
import xbmcgui
import os
import subprocess
 
addon       = xbmcaddon.Addon()
addonname   = addon.getAddonInfo('name')

child = subprocess.call(["C:\Program Files (x86)\Minecraft Launcher\MinecraftLauncher.exe","-k"])
