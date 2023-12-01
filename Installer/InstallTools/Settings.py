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
            sub_dir = input("Drag and drop the folder containing external subtitles here: ")
            if not os.path.isdir(sub_dir):
                print("That is not a valid directory. Please try again.")
            else:
                break
        file = open('settings.json', 'w+')
        data = { "set_dir": sub_dir}
        print("Saving settings...")
        json.dump(data, file)
        print("\nSettings saved.")