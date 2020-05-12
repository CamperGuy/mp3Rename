#!/usr/bin/env python
import os
import re
import sys

def main(path=""):
    if len(sys.argv) == 2:
        path = sys.argv[1]
    else:
        path = ""
    
    if os.path.isfile(path):
        tags(formatname(path))

    elif os.path.isdir(path):
        for filename in os.listdir(path):
            tags(formatname(filename))

    elif path == "":
        print("https://github.com/CamperGuy/mp3Rename\n")
        print("--- Main Menu")
        print("[0] Remove Trash from filename")
        print("[1] Set filename as mp3 tags")
        print("[2] Remove Trash and set MP3 Tags")
        proceed = False
        while not (proceed):
            try: 
                option = int(input("> "))
            except:
                continue
            if option in range(0, 3):
                proceed = True
                if option == 0:
                    path = input("Enter path or file: ")
                    if os.path.isfile(path):
                        formatname(path)
                    elif os.path.isdir(path):
                        for file in os.listdir(path):
                            formatname(path + "/" + file)
                elif option == 1:
                    proceed = True
                    path = input("Enter path or file: ")
                    if os.path.isfile(path):
                        tags(path)
                    elif os.path.isdir(path):
                        for file in os.listdir(path):
                            tags(file)
                elif option == 2:
                    proceed = True
                    path = input("Enter path or file: ")
                    if os.path.isfile(path):
                        tags(formatname(path))
                    elif os.path.isdir(path):
                        for file in os.listdir(path):
                            tags(formatname(path, file))

def formatname(path, output=True):
    ext = path[-4:]
    dir = path.split('/')
    edit = dir[len(dir)-1]
    dir.pop(len(dir)-1)
    dir = '/'.join(dir) + '/'
    edit = edit.replace(ext, '')
    edit = edit.replace("{ tagged }", '')

    regex = re.compile('\s?[\[\(]?((official|lyric|video|music|audio|monstercat|ncs|release|visualiser)\s?)+[\]\)]?\s?', re.IGNORECASE)
    edit = re.sub(regex, '', edit)
    
    edit = edit.strip()
    updated = edit + ext
    if output:
        print("Original: " + path)
        print("Edited:   " + dir + updated + "\n")
    
    try:
        os.rename(path, dir + updated)
    except:
        pass
    
    return dir + updated

def tags(file):
    ext = file[-4:]
    dir = file.split('/')
    dir.pop(len(dir)-1)
    dir = '/'.join(dir) + '/'
    
    editable = file.replace(dir, '')
    editable = editable.replace(ext, '')
    
    if len(editable.split("-")) == 2:
        artist = editable.split('-')[0].strip()
        title = editable.split('-')[1].strip()
    else:
        title = editable
        artist = ""
    print("Initialising FFMPEG...")
    format_list = [file, title, artist, dir+editable+"{ tagged }" + ext]
    command = "ffmpeg -i '{}' -c:a mp3 -ab 320k -metadata title='{}' -metadata artist='{}' '{}'".format(*format_list)
    print(command)
    os.system(command)
    formatname(dir+editable+"{ tagged }" + ext, True)
    print("Completed: " + editable)

if __name__ == "__main__":
    main()
