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
        trash = ["(Official Video)", "(Official Audio)", "[Audio]", "(Audio)", "[Monstercat Release]", 
                    "(Lyric Video)", "(lyrics)", "(Lyric Video)", "(official audio)",
                    "(official video)", "[NCS Release]", "(Official Music Video)", 
                    "[Official Lyric Video]", "Visualiser", "(Official Lyric Video)",
                ]
        for item in trash:
            if item in editName:
                editName = editName.replace(item, '')
        editName = editName.strip()
        newName = editName + ".mp3"
        print("Edited:   " + newName + "\n")
        os.rename(path + "/" + filename, path + "/" + newName)