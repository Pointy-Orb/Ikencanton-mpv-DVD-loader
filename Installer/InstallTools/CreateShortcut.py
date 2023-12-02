'''
Code taken from bitsgalore on Github:
https://gist.github.com/bitsgalore

Link to Github repo:
https://gist.github.com/bitsgalore/7579ab3fecbd4a143feacd1fb44a5858
'''

#! /usr/bin/env python
import os
import winreg
from win32com.client import Dispatch
class MakerShortcut:
    def MakeShortcut():
        os.path.curdir = os.path.realpath(__file__.replace('\\Installer\\InstallTools\\CreateShortcut.py', ''))
        print(os.path.curdir)

        def get_reg(name,path):
            # Read variable from Windows Registry
            # From http://stackoverflow.com/a/35286642
            try:
                registry_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, path, 0, winreg.KEY_READ)
                value, regtype = winreg.QueryValueEx(registry_key, name)
                winreg.CloseKey(registry_key)
                return value
            except WindowsError:
                return None

        # Package name
        packageName = 'mpv-open-dvd.py'

        # Scripts directory (location of launcher script)
        scriptsDir = os.path.curdir
        print(scriptsDir)

        # Target of shortcut
        target = os.path.join(scriptsDir, packageName)
        ico_target = os.path.join(scriptsDir, 'iken canton.ico')

        # Read location of Windows desktop folder from registry
        regName = 'Desktop'
        regPath = r'Software\Microsoft\Windows\CurrentVersion\Explorer\User Shell Folders'
        desktopFolder = os.path.normpath(get_reg(regName,regPath))

        # Path to location of link file
        pathLink = os.path.join(desktopFolder, "Ikencanton mVD loader.lnk")
        shell = Dispatch('WScript.Shell')
        shortcut = shell.CreateShortCut(pathLink)
        shortcut.Targetpath = target
        shortcut.WorkingDirectory = scriptsDir
        shortcut.IconLocation = ico_target
        
        shortcut.save()