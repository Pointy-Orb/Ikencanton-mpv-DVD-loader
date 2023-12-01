import importlib
shortcut_maker = importlib.import_module('.CreateShortcut', 'InstallTools').MakerShortcut
settings = importlib.import_module('.Settings', 'InstallTools').SettingsCon

choice: str

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