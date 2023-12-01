import os
import json

class SettingsCon:
    sub_dir: str
    def GetSubtitleDirectory():
        with open('settings.json', 'r') as file:
            sub_dir = json.load(file)["set_dir"]
        return sub_dir
    def SetSubtitleDirectory():
        sub_dir = "null"
        while True:
            sub_dir = input("Enter the path to the folder containing external subtitles here: ")
            if not os.path.isdir(sub_dir):
                print("That is not a valid directory. Please try again.")
            else:
                break
        file = open('settings.json', 'w+')
        data = { "set_dir": sub_dir}
        print("Saving settings...")
        json.dump(data, file)
        print("\nSettings saved.")

def GetInput(ans: str, question: str, valid_ans: list):
    while True:
        ans = input("Current subtitle folder is " + SettingsCon.GetSubtitleDirectory() + "\nWould you like to change it? (y/n)\n")
        if not ans in valid_ans:
            print("That is not a valid response. Please try again.\n")
        else:
            break

def DefineSettings():
    choice: str
    valid_inputs = ['exit', 'sub']
    print("SETTINGS MENU\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n")
    while not choice == 'exit':
        while True:
            choice = input("What settings would you like to change?\n'exit': Exit settings\n'sub': Change subtitle directory\n")
            if not choice in valid_inputs:
                print("That is not a valid response. Please try again.\n")
            else:
                break
        if choice == 'sub':
            GetInput(choice, "The current subtitle folder is " + SettingsCon.GetSubtitleDirectory() + "\nWould you like to change it? (y/n)\n", ['y', 'n'])
            if choice == 'y':
                SettingsCon.SetSubtitleDirectory()
            