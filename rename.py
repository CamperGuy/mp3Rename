#!/usr/bin/env python

import os

path = input("Enter directory path\n")

for filename in os.listdir(path):
    print("Original: " + filename)
    if filename[-4:].lower() == ".mp3" :
        ID = filename.split(".")
        ID = ID[len(ID) - 2]
        ID = ID[-12:]
        editName = filename.replace(ID, '')
        editName = editName.replace(".mp3", '')
        trash = [   "(Official Music Video)", "(official music video)", "[Official Music Video]", "[official music video]", "Official Music Video", "official music video",
                    "(Official Video)", "(official video)", "[Official Video]", "[official video]", "Official Video", "official video", 
                    "(Official Audio)", "(official audio)", "[Official Audio]", "[official audio]",  "Official Audio", "official audio", 
                    "(Official Lyric Video)", "(official lyric video)", "[Official Lyric Video]", "[official lyric video]", "Official Lyrics", "official lyrics", "(Official Lyrics)", "(official lyrics)", "Official Lyric Video", "official lyric video",
                    "(Lyric Video)", "(lyric video)", "[Lyric Video]", "[lyric video]", "Lyrics", "lyrics", "(Lyrics)", "(lyrics)", "Lyric Video", "lyric video", 
                    "(Audio)", "(audio)", "[Audio]", "[audio]", "Audio", "audio", 
                    "(Video)", "(video)", "[Video]", "[video]", "Video", "video",
                    "[Monstercat Release]",  "[NCS Release]",
                    "Visualiser"
                ]
        for item in trash:
            if item in editName:
                editName = editName.replace(item, '')
        editName = editName.strip()
        newName = editName + ".mp3"
        print("Edited:   " + newName + "\n")
        os.rename(path + "/" + filename, path + "/" + newName)
