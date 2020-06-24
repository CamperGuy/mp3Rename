import os
import platform

if platform.system() == "Windows":
    print("Windows virtualenv setup and ffmpeg install")
    os.system("python -m pip install --user virtualenv")
    os.system("python -m venv mp3rename")
    os.system(".\\mp3rename\\Scripts\\activate")
    os.system("pip install ffmpeg-python")
    os.system(".\\mp3rename\\Scripts\\deactivate")
else:
    print("Unix virtualenv setup and ffmpeg install")
    os.system("python -m pip install --user virtualenv")
    os.system("python -m venv mp3rename")
    os.system("source /mp3rename/bin/activate")
    os.system("pip install ffmpeg-python")
    os.system("deactivate")

os.system("python rename.py")
os.remove("setup.py")
