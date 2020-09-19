# iggupdater
Downloads and extracts .rar files from IGG-Games to the folder where the .py file is located in.

# Requirements
Before you download the repository, please note that you would need the following

- Python 3.5.2
(This program is only tested to work with Python 3.5.2, other versions of Python are not currently tested. However, you are free to use another version of Python if it works.)
- Pip (When going through the Python setup, please be sure to add it to PATH.)
- Python Modules (For more information, please read requirements.txt)

# How does the update.py file work?
Firstly, this file obtains the Google Drive download link from the IGG-GAMES link that you have specified in the file.
Afterwards, it would attempt to download the .rar file from Google Drive and extract it to the folder where update.py is located.

# Why does the update.py file only attempt to download .rar files?
As IGG-GAMES mostly uses .rar files for their Uploads, this file only supports .rar (WINRAR) downloads as of now.

If the game you are trying to download is not uploaded in .rar (WINRAR), it would not be downloaded.

# How do you specify the IGG-GAMES link that you would like to download?
Right click update.py, and click Edit with IDLE. 32-bit and 64-bit are both fine.
Find this line: url = "https://igg-games.com/among-us-free-download.html"
Replace it with: url = "Your Link Here"

# Installation
1. Download Python 3.5.2 from https://www.python.org/ftp/python/3.5.2/python-3.5.2-amd64-webinstall.exe
2. During the setup, please MAKE SURE to TICK the box that says "Add to PATH"
3. Download this repository
4. Move all the files in this repository into the folder where you would like to download the game to
5. Specify the game you would like to download by specifying the IGG-Games link. Read more : # How do you specify the IGG-GAMES link that you would like to download?
6. Run UPDATE.bat

# Additional information
NOTE: 
- This does not work with games that are split into different Parts.
e.g. Microsoft Flight Simulator, https://igg-games.com/microsoft-flight-120415897-simulator-2020-free-download.html
Microsoft Flight Simulator has been split into 15 different Parts. The program does not currently support downloading more than 1 Part.

- The file would not be able to be downloaded if too many people has downloaded it recently from IGG-GAMES. This is because Google limits the Download Quota.

# DISCLAIMER: Only use this repository if you know what you are doing. I am not responsible for anything that happens to your PC.
