# Ikencanton-mpv-DVD-loader
This loader is intended to streamline the process of loading a DVD from mpv. It uses a system that ties each title number to an episode number and name, so that one does not need to actually remember the title number.

As of now this program is **Windows Only**. I would love to make a Linux version, but do not have a Linux computer to
properly test on.

# Installation
Download the provided .zip file. Unzip the .zip and place the folder wherever you feel it should go (I would reccomend putting it inside mpv's folder)
Then open the folder, open the folder within the folder that says 'Installer', and then open the .py file with the same name. Follow the instructions on that file, and then open the newly created desktop shortcut.

If you have a DVD inserted into your machine, it will prompt you if you want to write that DVD to the local database. This is the most manual and labor-intensive part of the installation.

Select 'y'

Fill out the prompts as specified until you are prompted to input the 'Title ID' of an episode. You will need to manually test the title ID's of the videos on the DVD to find them.
> If you are using the provided mpv command line to test the title IDs, keep in mind that the actual title ID is the title ID in the command line + 1.

Do the same thing for the extras.

You will be prompted to type in the default audio ID of all the tracks you want to play. This is for stuff like commentary tracks and anime discs where they may be stored as separate audio tracks.
If you do not know what to put here, just type 1.

Congratulations! If you did everything correctly, your settings have been saved, and the next time you open this loader with that DVD in your machine, the settings you saved will be opened again and you can easily load your disc from mpv!

# Handling External Subttiles
During the installation, you were prompted to specify the folder where your external subtitles were stored. Unfortunately, hooking up external subtitles takes a little (not too much!) setup.

The first step is to make sure that none of the folders that lead up to (and including) your subtitle folder have spaces in their names. This is because the command line that gets injected into PowerShell will read the directory as two separate commands separated by spaces.

Then, inside your external subtitle folder, create a new folder with the same name as the volume label of your DVD (that's the title of the DVD that File Explorer shows to you). If your volume label has spaces in it, replace all the spaces with underscores.

Put all the subtitles you would like to use into that folder. Then, replace the names of each of the files with the same number that you type into this program to load that epsiode. (If the subtitles were for a movie, just put 1 as the number) The subtitles also must be .srt
> Make sure to keep the language codes for each subtitle, as they are important for detirmining the subtitle language

> The result should look like this:
>
> Hercules disc is in drive (volume name is HERCULES)
> 
> .../Subtitles/HERCULES/1.en.srt

If you did everything correctly, when trying to load the DVD with this application, the subtitles will be detected and automatically imported

(You can have multiple subtitle languages for the same episode, by the way!)
