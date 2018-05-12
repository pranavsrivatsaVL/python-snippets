from os import path
from os import walk
from tkinter.filedialog import askdirectory, Tk
from random import choice
from tkinter import messagebox
from os import startfile

# remove that annoying window in the background in Tkinter
root = Tk()
root.withdraw()


def isVideo(file):
    videoFormats = (".avi", ".asf", ".mp4", ".mov", ".flv", ".3gp", ".mkv", ".mpg", ".mpv", ".wmv")
    if file.endswith(videoFormats):
        return True
    else:
        return False


# Ask the user to enter the directory of thier choice (Point to a TV Series)
folder = askdirectory()
# Proceed only when user says ok
if folder:
    folder = path._getfullpathname(folder)
    ListOfEpisode = []
    # Now Ask the machine to walk through all directories and view all files in each folder and sub folders
    for pathOfFile, folders, allfiles in walk(folder):
        for file in allfiles:
            # We need a list of all video files along with the path of the file
            if (isVideo(file)):
                ListOfEpisode.append(path.join(pathOfFile, file))

    # Hope you did not point me to an Empty folder !
    if ListOfEpisode.__len__() == 0:
        messagebox.showinfo("Pay Attention !",
                            "It's an EMPTY FOLDER or does not contain Video files\nSelect Carefully Human!")
    else:
        # Dear Machine , Pick an episode for me !
        randomFile = choice(ListOfEpisode)
        folderPath = path._getfullpathname(randomFile)
        startfile(folderPath, 'open')

else:
    messagebox.showinfo("Cancelled ? Seriously ?",
                        "If you didnt want me to select a file why did you run the program ?\n-Machine")
