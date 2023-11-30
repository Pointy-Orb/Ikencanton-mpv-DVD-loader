
'''
original designer:
 Pointy Orb
 11/29/2023

Built off of Get_IMDb_Movie.py
   Ethan Miller
   3/13/2019
'''

language_codes = {
  ".en": "English", ".jp": "Japanese"
}

key_location = "no_directory"
question = "null"

try:
 from pyperclip import copy
 from win32api import GetVolumeInformation, GetLogicalDrives
 from win32file import GetDriveType
 import os 
 import subprocess
 import sys
 import shutil

except ModuleNotFoundError as e:
 print('Oops! Something went wrong.', e)
 count = 0
 while count <= 5:
   input('Please exit the application . . . ')
   count += 1
 input('Press enter to exit . . .')
 print('Exiting application . . .')
 exit()

try:
  import Keys
except:
  print("Keys file not found. Check to make sure that it is in the same directory as this script.")
  print("Location of file: " + os.path.curdir)
  exit()

def getVolumeLabel(drive):
 '''
 Reads in a disk drive ("D:\\") and returns its volume label.
 '''
 # Return name of movie from DVD Drive.
 volume_information = GetVolumeInformation(drive)
 volume_label = volume_information[0]
 return volume_label


def getDrives():
 '''
 Searches for local disk drives matching letters A-Z
 that are in use and returns a list of the results.
 '''
 # Create an empty list to hold the drives.
 drives = []
 bitmask = GetLogicalDrives()
 # Test for each possible drive letter.
 for letter in list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
   # If drive exists, append to list of drives.
   if bitmask & 1:
     drives.append(letter)
   bitmask >>= 1


 return drives


def getDriveTypes():
 '''
 Searches a list of disk drives and returns a
 dictionary of the same list as keys with
 drive type information as values.
 '''
 # Create an empty dictionary to hold the drive / drive types.
 types = {}
 # Create a list of drive types for typeIndex to match.
 driveTypes = ['DRIVE_UNKNOWN', 'DRIVE_NO_ROOT_DIR', 'DRIVE_REMOVABLE', 'DRIVE_FIXED', 'DRIVE_REMOTE', 'DRIVE_CDROM', 'DRIVE_RAMDISK']


 for drive in getDrives():
   try:
     # GetDriveType() will return a number that represents a drive type.
     typeIndex = GetDriveType(u"%s:\\"%drive)
     # Add new key / value pairs to the 'types' dictionary, where the drive letter is the key and the type is the value.
     types[f'{drive}:'] = driveTypes[typeIndex]
   except Exception as e:
     print('Error: ', e)
 return types


def getCdRoms():
 '''
 Searches a dictionary of drives and
 drive types and returns a list of
 drives that are CD ROMs.
 '''
 drives = getDriveTypes()
 cdroms = []
 for drive, drive_type in drives.items():
   if drive_type == 'DRIVE_CDROM':
     cdroms.append(drive)
 return cdroms


def selectCdRom():
 '''
 Tests how many CD ROMs are in the machine,
 and if more than 1, prompts the user to
 select which CD ROM to use.
 '''
 cdroms = getCdRoms()


 if len(cdroms) > 1:
   # Print the available drives.
   for letter in cdroms:
     print(f'{cdroms.index(letter)+1}. {letter}')
   # Input validation.
   while True:
     try:
       # Promt user to select drive.
       index = input('Please select which drive to search (by number): ')
       return cdroms[int(index)-1]
     except IndexError:
       print('Index error: That number doesn\'t appear to match any of the disk drives listed.')
       continue
     except ValueError:
       print('Value error: Value must be a numeric digit. Try again and God bless.')
       continue
     except Exception as e:
       print('Opps! Something went wrong. ', e)
       continue
 else:
   return cdroms[0]

def makeVariableSafe(string: str):
  for letter in string:
    if letter == " ":
      string = string.replace(letter, "_")
  return string

def getKeyValues():
  answer_title = input("What is the title of the movie/TV show on the DVD? : ")
  answer_episode_names = []
  answer_current_ep_name =  "null"
  answer_ep_no = []
  answer_current_ep_no = "null"
  answer_ex_names = []
  answer_current_ex_name =  "null"
  answer_ex_no = []
  answer_current_ex_no = "null"
  print("Now type the titles of all the episodes on the DVD, in sequential order, then type 'done'. If your DVD does not have episodes, just type 'done' instead of inputting anything")
  while not answer_current_ep_name == "done":
      answer_current_ep_name = input("Title of episode " + str(len(answer_episode_names) + 1) + ": ")
      if not answer_current_ep_name == "done":
        answer_episode_names.append(answer_current_ep_name)
  print("\nType the Title ID for each of the episodes. You can find an episodes's Title ID by manually testing 'mpv dvd://[title ID - 1]/[dvd volume] --dvd-device=PATH'")
  for i in answer_episode_names:
    while not str.isnumeric(answer_current_ep_no):
      if not answer_episode_names:
        answer_current_ep_no = input("Title ID of movie: ")
      else:
        answer_current_ep_no = input("Title ID of episode " + str(answer_episode_names.index(i) + 1) + " of " + str(len(answer_episode_names)) + ": ")
        if not str.isnumeric(answer_current_ep_no):
          print("The value you have entered is not a number. Try again:\n")
    answer_ep_no.append(answer_current_ep_no)
    answer_current_ep_no = "null"
  print("\nNow repeat the same thing for the extras:")
  while not answer_current_ex_name == "done":
      answer_current_ex_name = input("Title of extra video " + str(len(answer_ex_names) + 1) + ": ")
      if not answer_current_ex_name == "done":
        answer_ex_names.append(answer_current_ex_name)
  for why in answer_ex_names:
    while not str.isnumeric(answer_current_ex_no):
      answer_current_ex_no = input("Title ID of extra " + str(answer_ex_names.index(why) + 1) + " of " + str(len(answer_ex_names)) + ": ")
      if not str.isnumeric(answer_current_ex_no):
          print("The value you have entered is not a number. Try again:\n")
    answer_ex_no.append(answer_current_ex_no)
    answer_current_ex_no = "null"

  writeToKeys(answer_title, answer_episode_names, answer_ex_names, answer_ep_no, answer_ex_no)

'''
  if answer_ex_names:
    for i in answer_ex_names:
      while not str.isnumeric(answer_current_ex_no):
        answer_current_ex_no = input("Title ID of extra " + str(answer_ex_names.index(i) + 1) + " of " + str(len(answer_ex_names)) + ": ")
        if not str.isnumeric(answer_current_ex_no):
            print("The value you have entered is not a number. Try again:\n")
      answer_ex_no.append(answer_current_ex_no)
'''

'''
  for i in answer_episode_names:
    while not str.isnumeric(answer_current_ep_no):
      if not answer_episode_names:
        answer_current_ep_no = input("Title ID of movie: ")
      else:
        answer_current_ep_no = input("Title ID of episode " + str(answer_episode_names.index(i) + 1) + " of " + str(len(answer_episode_names)) + ": ")
        if not str.isnumeric(answer_current_ep_no):
          print("The value you have entered is not a number. Try again:\n")
'''

def writeToKeys(an_title: str, an_ep_names: list, an_ex_names: list, an_ep_no: list, an_ex_no: list):
    list_names = [an_ep_names, an_ex_names, an_ep_no, an_ex_no]
    temp = open('temp', 'w')
    with open('.\\Keys.py', 'r') as file:
      for line in file:
        if line.startswith('    #DONTREMOVEME') or line.startswith('\t#DONTREMOVEME'):
          line = '\t"' + label_volume + '": Key("' + an_title + '", [' 
          for j in list_names:
            for i in j:
              line = line + '"' + i + '", '
            line = line[:-2] + "], ["
          line = line[:-3] + "),\n\t#DONTREMOVEME\n"
        temp.write(line)
    temp.close()
    shutil.move('temp', '.\\Keys.py')
    print("Written to local database.")

# Get the volume label of your CD ROM.
drive = selectCdRom()

key_location = os.path.abspath("C:\\Program Files (x86)\\mpv")

def CloneList(copy_from: list, copy_to: list):
  copy_to.clear()
  for i in copy_from:
     copy_to.append(i)

label_volume = getVolumeLabel(drive)


title = "null"

global values
try:
  values = Keys.key_names[label_volume]
except:
   print(label_volume)
   while not question == "y" and not question == "n":
      question = input("The entry for that disc does not exist in the local database. Would you like to create it? (y/n)\n")
      if not question == "y" and not question == "n":
         print("Invalid response")
   if question == "y":
      getKeyValues()
      exit()
   if question == "n":
      exit()
   
extras_not_episodes = False

values.printEpisodeNames()

selected_title = "value"

print("\nType 'exit' to close program\n")
while not str.isnumeric(selected_title) and not selected_title == "exit" and not str.isnumeric(selected_title.replace('x', '')) and not str.isnumeric(selected_title.replace('raw-', '')):
    selected_title = input("Type the episode number of the title you want to play. For extras, put an 'x' in front of your number: ")
    if not str.isnumeric(selected_title) and not selected_title == "exit" and not str.isnumeric(selected_title.replace('x', '')) and not str.isnumeric(selected_title.replace('raw-', '')):
        print("Input is not valid. Try again:\n")
    if "x" in selected_title:
      extras_not_episodes = True

subtitle_dir = Keys.GetSubtitleDirectory()
avalible_sub_list: list = []
chose_sub_dir = "null"

print("\nAvalible subtitle languages:")
for i in language_codes.keys():
  if os.path.exists(subtitle_dir + label_volume + '\\' + selected_title + i + ".srt"):
    print(language_codes[i])
    avalible_sub_list.append(i)

if not avalible_sub_list:
  print("\nNo external subtitles were detected\n")
elif len(avalible_sub_list) == 1:
  chose_sub_dir = subtitle_dir + label_volume + '\\' + selected_title + avalible_sub_list[0] + ".srt"
  print("\nImporting " + language_codes[avalible_sub_list[0]] + " subtitles\n")
else:
  print("Multiple subtitles were detected, please select one to import.")
  for i in avalible_sub_list:
    print(language_codes[i] + "subtitles: " + str(avalible_sub_list.index(i)))
  while not int(chose_sub_dir) <= len(avalible_sub_list) - 1 or int(chose_sub_dir) < 0:
    chose_sub_dir = input("\n")
    if not int(chose_sub_dir) <= len(avalible_sub_list) - 1 or int(chose_sub_dir) < 0:
      print("That is not a valid answer. Please try again.")

if selected_title == "exit":
    exit()
elif selected_title == "settings":
   pass
elif "raw-" in selected_title:
    subprocess.run("mpv dvd://" + selected_title.replace('raw-', '') + "/" + drive + " --dvd-device=PATH")
elif "x" in selected_title:
    subprocess.run("mpv dvd://" + str(int(values.extras_title_no[int(selected_title.replace('x', '')) - 1]) - 1) + "/" + drive + " --dvd-device=PATH")
    exit() 
else:
    subprocess.run("mpv dvd://" + str(int(values.episode_title_no[int(selected_title) - 1]) - 1) + "/" + drive + " --dvd-device=PATH")
    exit()
