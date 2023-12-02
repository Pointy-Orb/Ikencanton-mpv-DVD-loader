language_codes = {
  ".en": "English", ".ja": "Japanese", ".es": "Spanish", ".it": "Italian"
}

question = "null"

try:
 import os 
 import subprocess
 import importlib
 import pickle
except ModuleNotFoundError as e:
 print('Oops! Something went wrong.', e)
 count = 0
 while count <= 5:
   input('Please exit the application . . . ')
   count += 1
 input('Press enter to exit . . .')
 print('Exiting application . . .')
 exit()

os.system('color 57')

root = os.path.dirname(os.path.abspath(__file__))

try:
  settings = importlib.import_module('.Settings', 'Installer.InstallTools').SettingsCon
  import GetDVDInfo
  Keys = importlib.import_module('.Keys', 'Saves')
except ModuleNotFoundError as e:
  print(str(e) + " file not found. Check to make sure that it is in the same directory as this script.")
  print("Location of file: " + os.path.curdir)
  exit()

def getAnswer(question: str, valid_answers: list, need_number: bool):
   while True:
      choice = input(question)
      if need_number:
        if not choice.isnumeric():
           print("You must input a number")
        else:
           return choice
      elif valid_answers != None:
        if not choice in valid_answers:
          print("That is not a valid answer. Please try again.")
        else:
          return choice
      else:
         if choice == '':
            print("You must input something.")
         else:
          return choice

def makeStringSafe(string: str):
   string.replace(' ', '_')
   return string

def getKeyValues():
  answer_title = getAnswer("What is the title of the movie/TV show on the DVD? : ", None, False)
  answer_episode_names = []
  answer_current_ep_name =  "null"
  answer_ep_no = []
  answer_current_ep_no = "null"
  answer_ex_names = []
  answer_current_ex_name =  "null"
  answer_ex_no = []
  answer_current_ex_no = "null"
  answer_aid = "null"
  print("Now type the titles of all the episodes on the DVD, in sequential order, then type 'done'. If your DVD does not have episodes, just type 'done' instead of inputting anything")
  while True:
      answer_current_ep_name = getAnswer("Title of episode " + str(len(answer_episode_names) + 1) + ": ", None, False)
      if not answer_current_ep_name == "done":
        answer_episode_names.append(answer_current_ep_name)
      else:
        break
  print("\nType the Title ID for each of the episodes. You can find an episodes's Title ID by manually testing 'mpv dvd://[title ID - 1]/[dvd volume] --dvd-device=PATH'")
  for i in answer_episode_names:
    answer_current_ep_no = getAnswer("Title ID of episode " + str(answer_episode_names.index(i) + 1) + " of " + str(len(answer_episode_names)) + ": ", None, True)
    answer_ep_no.append(answer_current_ep_no)
    answer_current_ep_no = "null"
  if not answer_episode_names:
    answer_current_ep_no = getAnswer("Title ID of movie: ", None, True)
    answer_ep_no.append(answer_current_ep_no)
  print("\nNow repeat the same thing for the extras:")
  while not answer_current_ex_name == "done":
      answer_current_ex_name = getAnswer("Title of extra video " + str(len(answer_ex_names) + 1) + ": ", None, False)
      if not answer_current_ex_name == "done":
        answer_ex_names.append(answer_current_ex_name)
  for why in answer_ex_names:
    while not str.isnumeric(answer_current_ex_no):
      answer_current_ex_no = input("Title ID of extra " + str(answer_ex_names.index(why) + 1) + " of " + str(len(answer_ex_names)) + ": ")
      if not str.isnumeric(answer_current_ex_no):
          print("The value you have entered is not a number. Try again:\n")
    answer_ex_no.append(answer_current_ex_no)
    answer_current_ex_no = "null"
  answer_aid = getAnswer("Enter the ID of the audio track you want to play by default for this disk\n(If you do not know what to put here, simply type '1')", None, True)
  writeToKeys(answer_title, answer_episode_names, answer_ex_names, answer_ep_no, answer_ex_no, answer_aid)

def writeToKeys(an_title: str, an_ep_names: list, an_ex_names: list, an_ep_no: list, an_ex_no: list, an_aid: str):
    with open(os.path.join(root, 'Saves', 'Keys', '{lv}.pkl').format(lv=label_volume), 'wb') as file:
      data = Keys.Key(an_title, an_ep_names, an_ex_names, an_ep_no, an_ex_no, an_aid)
      pickle.dump(data, file)
    print("File saved to local database")
    input("\nPress Enter to exit")
    exit()

# Get the volume label of your CD ROM.
drive = GetDVDInfo.selectCdRom()

def CloneList(copy_from: list, copy_to: list):
  copy_to.clear()
  for i in copy_from:
     copy_to.append(i)

label_volume = GetDVDInfo.getVolumeLabel(drive)


title = "null"

global values
try:
  with open(os.path.join(root, 'Saves', 'Keys', label_volume + '.pkl'), 'rb') as file:
      values = pickle.load(file)
except:
   print(label_volume)
   while not question == "y" and not question == "n":
      question = input("The entry for that disc does not exist in the local database. Would you like to create it? (y/n)\n")
      if not question == "y" and not question == "n":
         print("Invalid response")
   if question == "y":
      getKeyValues()
   if question == "n":
      exit()
   
extras_not_episodes = False

values.printEpisodeNames()

selected_title = "value"

print("\nType 'exit' to close program and type 'settings' to open settings\n")
while True:
    selected_title = input("Type the episode number of the title you want to play. For extras, put an 'x' in front of your number: ")
    if "x" in selected_title:
      extras_not_episodes = True
    if not str.isnumeric(selected_title) and not selected_title == "exit" and not str.isnumeric(selected_title.replace('x', '')) and not str.isnumeric(selected_title.replace('raw-', '')) and not selected_title == "settings":
        print("Input is not valid. Try again:\n")
    else:
       break

if selected_title == "exit":
    exit()

if selected_title == "settings":
    settings.Setting()
    exit()

subtitle_dir = settings.GetSubtitleDirectory()
print (subtitle_dir)
avalible_sub_list: list = []
chose_sub_dir = "null"

print("\nAvalible subtitle languages:")
for i in language_codes.keys():
  cani_sub = selected_title + i + ".srt"
  if os.path.exists(os.path.join(subtitle_dir, makeStringSafe(label_volume), cani_sub)):
    print(language_codes[i])
    avalible_sub_list.append(i)

if not avalible_sub_list:
  print("\nNo external subtitles were detected\n")
elif len(avalible_sub_list) == 1:
  chose_sub = selected_title + avalible_sub_list[0] + ".srt"
  chose_sub_dir = os.path.join(subtitle_dir, makeStringSafe(label_volume), chose_sub)
  print("\nImporting " + language_codes[avalible_sub_list[0]] + " subtitles\n")
else:
  print("Multiple subtitles were detected, please select one to import.")
  for i in avalible_sub_list:
    print(language_codes[i] + "subtitles: " + str(avalible_sub_list.index(i)))
  while True:
    chose_sub_dir = input("\n")
    if int(chose_sub_dir) <= len(avalible_sub_list) - 1 or int(chose_sub_dir) < 0:
      print("That is not a valid answer. Please try again.")
    else:
       break

if settings.GetFullscreen():
   fs = ' --fullscreen'
else:
   fs = ''

if "x" in selected_title:
  title_no = str(int(values.extras_title_no[int(selected_title.replace('x', '')) - 1]) - 1)
else:
  title_no = str(int(values.episode_title_no[int(selected_title) - 1]) - 1)

if "raw-" in selected_title:
    subprocess.run("mpv dvd://" + selected_title.replace('raw-', '') + "/" + drive + " --dvd-device=PATH")
else:
    subprocess.run("mpv --sub-file={sub_file_dir} dvd://{t}/{D} --dvd-device=PATH --aid={aid}{full}".format(sub_file_dir=str(chose_sub_dir), t=title_no, D=drive, aid=values.default_title_id, full=fs))
    exit()