# mp3Rename
A python script created to tidy up file names and apply mp3 tags where possible

## Usage
### Automated Usage
Calling the script with a path to either a Directory or a File will remove typical junk from the filename such as "Official Music Video" and attempt to set mp3 tags. It will determine these by the dash in the filename. Currently only Artist and Title are supported, but more support might be added in a future release. This makes it ideal in combined use with something like https://github.com/ytdl-org/youtube-dl </br>
Example:</br>
```youtube-dl "https://www.youtube.com/watch?v=rZgeF5SrCAg"```</br>
```python mp3rename.py "X Ambassadors, K.Flay and grandson - Zen (Official Video).mp3"```</br>
Which will leave you with `X Ambassadors, K.Flay and grandson - Zen.mp3` with mp3 Artist Tag "X Ambassadors, K.Flay and grandson" and mp3 Title Tag "Zen".

### Manual Usage
Opening the script will offer a CLI where several options can be used </br></br>
<b>Automatically tidy filenames</b>: Will remove any (Offical Music Video) junk from the filename. This is best used on a directory where mp3 Tags are already present. </br></br>
<b>Automatically set mp3 tags</b>: Will set mp3 Artist and Title tags via the format given in the file name, separated by a dash `-`. This is best used on a directory where the filenames have already been cleaned. </br></br>
<b>Manually set mp3 tags</b>: Will allow setting mp3 Tags regardless of the filename. The input file given will lose its original name and output as "[Artist] - [Title].mp3"

### Notes
.mp4 files can be provided, but will be ignored in any mp3 tag operations, in both automated and manual usecases. Filenames will still be cleaned up where possible. </br>
With automated tags, if a dash is not present in the file name, the filename will be used for the Title mp3 tag

## Dependencies
You are expected to have some version of python already installed on your system. Running `setup.py` will set up a virtual environment and install the FFMPEG-Python library to that environment. The installer will then self destruct.</br>
Alternatively you can also install FFMPEG-Python to your system via `pip install ffmpeg-python` which will allow you to bypass the use of setup.py.

### Compatibility
If you experience issues using this script, try manually setting up the dependencies (of which there is only one) and make sure you have an up-to-date python installation. Any further problems, please open an issue and provide as much information as possible.
