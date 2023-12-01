class Key: 
    def __init__(self, title: str, ep_names: list, ex_names: list, ep_nos: list, ex_nos: list):  
        #Title ID is the specification of where a video is in a DVD playlist. It can be seen by going into VLC>Playback>Title>The highlighted title ID is the title ID of the current video
        #Write the title of the movie/show here:
        self.title = title

        #Names of each episode go here. If your DVD is a movie, or doesnt have episodes, change to "none"
        self.episode_names = ep_names
        #Respectively for each of the episodes specified above, input the title ID of that video. If(Title ID explained above)
        self.episode_title_no = ep_nos

        #Names of each of the extras videos go here. Works the same as episode_names
        self.extras_names = ex_names
        #Functions the same as episode_title_no, but now with the extras instead of the episodes.
        self.extras_title_no = ex_nos

    def printEpisodeNames(self):
        print("\n" + self.title + "\n")
        if not self.episode_names == "none":
            print("Episodes:")
            for i in self.episode_names:
                print("Episode (" + str(self.episode_names.index(i) + 1) + "): " + str(i))
        else: print("This DVD does not have an episodic format")
        if not self.extras_names == "none":
            print("\nExtras")
            for i in self.extras_names:
                print(i + ": x" + str(self.extras_names.index(i) + 1))
        else: print("\nThis DVD does not have extras")

    def printEpisodeNumbers(self):
        if not self.episode_names == "movie":
            print("Episodes:")
            for i in self.episode_title_no:
                print("Episode (" + str(self.episode_title_no.index(i) + 1) + "): " + str(i))
        else: print("Type '1' to play movie")
        if not self.extras_names == "none":
            print("\nExtras")
            for i in self.extras_title_no:
                print(i + ": x" + str(self.extras_title_no.index(i) + 1))
        else: print("\nThis DVD does not have extras")

def GetSubtitleDirectory():
    return "C:\\Users\\point\\Desktop\\DVD Key\\Subtitles\\"

key_names = {
	#DONTREMOVEME
}