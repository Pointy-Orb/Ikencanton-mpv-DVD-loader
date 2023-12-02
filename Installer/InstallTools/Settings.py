import os
import json

sub_codes = {"ja": "Japanese", "en": "English", "es": "Spanish"}

class SettingsCon:
    sub_dir: str
    def GetSubtitleDirectory():
        old_dir = os.path.realpath(os.curdir)
        with open(os.path.join(os.getcwd(), 'Saves', 'settings.json'), 'r') as file:
            sub_dir = json.load(file)["sub_dir"]
        os.chdir(old_dir)
        return sub_dir
    def SetSubtitleDirectory():
        sub_dir = "null"
        while True:
            sub_dir = input("Enter the path to the folder containing external subtitles here: ")
            if not os.path.isdir(sub_dir):
                print("That is not a valid directory. Please try again.")
            else:
                break
        with open(os.path.join(os.getcwd(), 'Saves', 'settings.json'), 'r') as file:
            data = json.load(file)
        with open(os.path.join(os.getcwd(), 'Saves', 'settings.json'), 'w') as file:
            data['sub_dir'] = sub_dir
            json.dump(data, file)
    def GetFullscreen():
        with open(os.path.join(os.getcwd(), 'Saves', 'settings.json'), 'r') as file:
            data = json.load(file)['fullscreen']
            return data
    def Setting():
        DefineSettings()

def GetInput(ans: str, question: str, valid_ans: list):
    while True:
        ans = input(question)
        if not ans in valid_ans:
            print("That is not a valid response. Please try again.\n")
        else:
            break

def DefineSettings():
    choice = "null"
    valid_inputs = ['exit', 'sub', 'f']
    print("SETTINGS MENU\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n")
    while not choice == 'exit':
        while True:
            choice = input("What settings would you like to change?\n'exit': Exit settings\n'sub': Change subtitle directory\n'f': Automatically load in fullscreen (Current value: " + str(SettingsCon.GetFullscreen()) + ")\n")
            if not choice in valid_inputs:
                print("That is not a valid response. Please try again.\n")
            else:
                break
        if choice == 'sub':
            GetInput(choice, "The current subtitle folder is " + SettingsCon.GetSubtitleDirectory() + "\nWould you like to change it? (y/n)\n", ['y', 'n'])
            if choice == 'y':
                SettingsCon.SetSubtitleDirectory()
        if choice == 'f':
            #Toggle between fullscreen and not fullscreen
            with open(os.path.join(os.getcwd(), 'Saves', 'settings.json'), 'r') as file:
                data = json.load(file)
            with open(os.path.join(os.getcwd(), 'Saves', 'settings.json'), 'w') as file:
                data['fullscreen'] = not data['fullscreen']
                json.dump(data, file)
            print("Change saved.")
            