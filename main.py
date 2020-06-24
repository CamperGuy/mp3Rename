#!/usr/bin/env python
import os
import re
import sys
import ffmpeg
import webbrowser

def main(path=""):
    # Set path if it has been given as a cmd line argument
    if len(sys.argv) == 2:
        path = sys.argv[1]
    
    if os.path.isfile(path):
        # Ignore tags for mp4s
        ext = path[-4:]
        if ext != ".mp4":
            tags(filename(path, False), True)
        else:
            filename(path, False)

    elif os.path.isdir(path):
        for file in os.listdir(path):
            # Ignore tags for mp4s
            ext = path[-4:]
            if ext != ".mp4":
                tags(filename(path, False), True)
            else:
                filename(path, False)

    elif path == "":
        print("\n--- mp3 Rename")
        print("[0] Automatically tidy filenames")
        print("[1] Automatically set mp3 tags")
        print("[2] Manually set mp3 tags")
        print("[3] About")
        print("[4] Quit")
        menuloop = True
        while (menuloop):
            try: 
                option = int(input("> "))
            except:
                continue
            
            if option in range(0, 4):
                menuloop = False
                # Auto Filename
                if option == 0:
                    path = input("Path: ")
                    if os.path.isfile(path):
                        filename(path)
                    elif os.path.isdir(path):
                        for file in os.listdir(path):
                            filename(path + "/" + file)
                    else:
                        print("Path given is neither a file or directory \n")
                        main()

                # Auto Tags
                elif option == 1:
                    menuloop = False
                    path = input("Enter Path: ")
                    if os.path.isfile(path):
                        tags(path, True)
                    elif os.path.isdir(path):
                        for file in os.listdir(path):
                            tags(file, True)
                    else:
                        print("Path given is neither a file or directory \n")
                        main()

                # Manual Tags
                elif option == 2:
                    menuloop = False
                    path = input("Enter Path: ")
                    if os.path.isfile(path):
                        tags(path, False)
                    elif os.path.isdir(path):
                        for file in os.listdir(path):
                            tags(path, False)
                    else:
                        print("Path given is neither a file or directory \n")
                        main()
                # About
                elif option == 3:
                    webbrowser.open('https://github.com/CamperGuy/mp3Rename/blob/master/README.md', new=2)

                # Quit        
                elif option == 4:
                    exit()

def filename(path, output=True):
    if os.path.isfile(path) or os.path.isdir(path):
        ext = path[-4:]
        dir = path.split('/')
        edit = dir[len(dir)-1]
        dir.pop(len(dir)-1)
        dir = '/'.join(dir) + '/'
        og = edit
        edit = edit.replace(ext, '')
        edit = edit.replace("{ tagged }", '')

        regex = re.compile('\s?[\[\(]?((official|offiziell|musik|musikvideo|lyric|video|music|audio|monstercat|ncs|release|visualiser)\s?)+[\]\)]?\s?', re.IGNORECASE)
        edit = re.sub(regex, '', edit)
        
        edit = edit.strip()
        updated = edit + ext
        if output == True:
            print("☐ " + og)
            print("☑ " + edit + ext + "\n")
        
        try:
            os.rename(path, dir + updated)
        except:
            pass
        
        return dir + updated

def tags(file, automated=False):
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
        artist = ""
        title = editable
    
    if not automated:
        artist = input("Artist: ")
        title = input("Title: ")

    print("Recompiling Audio...")

    hidden = dir + "." + artist + " - " + title + ext
    os.rename(file, hidden)
    stream = ffmpeg.input(hidden)
    stream = ffmpeg.output(stream, dir+artist + " - " + title + ext, loglevel='quiet', ab='320k', **{ 'metadata':'title=' + title, 'metadata:':'artist=' + artist} )
    ffmpeg.run(stream)

    print("Completed: " + artist + " - " + title)
    os.remove(hidden)
    print("Deleted: " + hidden)

if __name__ == "__main__":
    main()
