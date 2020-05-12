#!/usr/bin/env python
import os
import sys

def main(path=""):
    if len(sys.argv) == 2:
        path = sys.argv[1]
    else:
        path = ""
    print("Path: " + path)
    if os.path.isfile(path):
        tags(remove(path))

    elif os.path.isdir(path):
        for filename in os.listdir(path):
            tags(remove(filename))

    elif path == "":
        print("[0] Remove Trash from filename")
        print("[1] Set filename as mp3 tags [Artist] - [Title].mp3")
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
                        remove(path)
                    elif os.path.isdir(path):
                        for file in os.listdir(path):
                            remove(path + "/" + file)
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
                        tags(remove(path))
                    elif os.path.isdir(path):
                        for file in os.listdir(path):
                            tags(remove(path, file))

def remove(path, output=True):
    ext = path[-4:]
    dir = path.split('/')
    edit = dir[len(dir)-1]
    dir.pop(len(dir)-1)
    dir = '/'.join(dir) + '/'
    edit = edit.replace(ext, '')
    trash = [   "{ tagged }",
                "(Official Music Video)", "(official music video)", "[Official Music Video]", "[official music video]", "Official Music Video", "official music video",
                "(Official Video)", "(official video)", "[Official Video]", "[official video]", "Official Video", "official video", 
                "(Official Audio)", "(official audio)", "[Official Audio]", "[official audio]",  "Official Audio", "official audio", 
                "(Official Lyric Video)", "(official lyric video)", "[Official Lyric Video]", "[official lyric video]", "(Official Lyrics)", "(official lyrics)", "Official Lyric Video", "official lyric video",  "Official Lyrics", "official lyrics", 
                "(Lyric Video)", "(lyric video)", "[Lyric Video]", "[lyric video]", "(Lyrics)", "(lyrics)", "Lyric Video", "lyric video", "Lyrics", "lyrics", 
                "(Audio)", "(audio)", "[Audio]", "[audio]", "Audio", "audio", 
                "(Video)", "(video)", "[Video]", "[video]", "Video", "video",
                "[Monstercat Release]",  "[NCS Release]",
                "Visualiser"
            ]
    for item in trash:
        if item in edit:
            edit = edit.replace(item, '')
    edit = edit.strip()
    updated = edit + ext
    if output:
        print("Original: " + path)
        print("Edited:   " + dir + updated + "\n")
    os.rename(path, dir + updated)
    return dir + updated

def tags(file):
    ext = file[-4:]
    dir = file.split('/')
    dir.pop(len(dir)-1)
    dir = '/'.join(dir) + '/'
    
    editable = file.replace(dir, '')
    editable = editable.replace(ext, '')
    
    artist = editable.split('-')[0].strip()
    title = editable.split('-')[1].strip()

    print("Initialising FFMPEG...")
    format_list = [file, title, artist, dir+editable+"{ tagged }" + ext]
    command = "ffmpeg -i '{}' -c:a mp3 -ab 320k -metadata title='{}' -metadata artist='{}' '{}'".format(*format_list)
    os.system(command)
    remove(dir+editable+"{ tagged }" + ext, False)
    print("Completed: " + editable)

if __name__ == "__main__":
    main()
