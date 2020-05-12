# mp3Rename
A python script created to tidy up file names and apply mp3 tags where possible

## Dependencies
FFMPEG  
Python 2.x or newer

## Usage
The script can be opened in any CLI by ```python path-to-script ``` and from there on can be navigated via the built in menu. When asked to provide a path, this can either be a path to a folder containg unformatted audio files which will be batch processed, or just a singular file.  
  
When given a parameter in the commandline such as ```python path-to-script path-to-folder-or-file``` it will be assumed that the path provided shall be renamed and tags set (see option 2 in Main Menu)   

### Expected File Format
In order to write the mp3 tags properly, files have to follow a certain structure, which is  
[Artist]<b>-</b> [Title].[FileFormat]   
This tool is expected to be used in conjunction with some kind of Video downloader such as youtube-dl, where the generated file names would often contain additional, platform specific values in their title such as "Official Music Video". These get filtered out by the script, leaving tidy file names

### Output files
Target format of this script is mp3. Thanks to FFMPEG's versatility it should however be possible to input any audio format that FFMPEG supports.  
<b>Filename:</b>  
[Artist] - [Title].mp3  
  
<b>mp3 Tags:</b>  
Artist: [Beginning of file name until dash]  
Title : [Anything between dash and file extension]  

### Compatibility
I have developed this in Python 2.7 to ensure backwards compatibility ~~and totally not by accident~~
