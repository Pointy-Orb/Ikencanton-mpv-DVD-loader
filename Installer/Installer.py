import importlib
import os
import json
shortcut_maker = importlib.import_module('.CreateShortcut', 'InstallTools').MakerShortcut
settings = importlib.import_module('.Settings', 'InstallTools').SettingsCon

choice: str

with open(os.path.join(os.getcwd(), 'Saves', 'settings.json'), 'w') as file:
    data = {'i_exist': "now you do"}
    json.dump(data, file)

#Creating desktop shortcut so that file can easily be opened.
print("Creating desktop shortcut...")
shortcut_maker.MakeShortcut()
print("Shortcut created. Remember that you can move it somewhere else if you like.\n")

#Asking if the user has a directory for external subtitles and if they would like to link to it
while True:
    choice = input("Would you like to link to a folder where your external subtitles are kept? (y/n)\n")
    if not choice == "y" and not choice == "n":
        print("That is not a valid answer. Please try again:")
    else:
        break

if choice == "y":
    settings.SetSubtitleDirectory()
else:
    print("OK then. This can be changed later.")

#C:\Users\point\Desktop\DVDKey\Subtitles
with open(os.path.join(os.getcwd(), 'Saves', 'settings.json'), 'r') as file:
    data = json.load(file)
with open(os.path.join(os.getcwd(), 'Saves', 'settings.json'), 'w') as file:
    entry = {'fullscreen': False}
    data['fullscreen'] = False
    json.dump(data, file)