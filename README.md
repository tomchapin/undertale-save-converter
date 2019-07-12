# Undertale PC/Switch Save File Converter V2.1
Inspired by JonyLuke's Undertale Save Converter (https://github.com/jonyluke/Undertale-save-converter).
This version is a complete re-write, and features full bi-directional conversion functionality.

[Project page on the GBATemp Forum](https://gbatemp.net/threads/undertale-save-game-converter-v2-with-full-bi-directional-pc-switch-conversion-ability.542897/)


## Requirements 
- Undertale
- A Modded Nintendo Switch
- Python3.4 (https://www.python.org/downloads/) - Optional
  (Note: This is only required if you want to compile the undertale_save_converter.exe file yourself, or if you want to run undertale_save_converter.py directly)


## Installation and Usage
1. Download the latest release from https://github.com/tomchapin/undertale-save-converter/releases
2. Save it to a folder on your local computer.
3. Copy your game save files to the same folder.


### Converting from PC to Switch
1. Make sure you have copied your game's file0, file9, and undertale.ini files into the folder with the undertale_save_converter.exe file.
   (These files are typically located in your system's %LocalAppData%\UNDERTALE\ folder)
2. Use your command prompt to browse to the folder, then execute `undertale_save_converter.exe` and select the first menu option.
3. Alternately (if you want to run the script via python), execute `python undertale_save_converter.py` (requires Python 3 to be installed).


### Converting from Switch to PC
1. Make sure you have the undertale.sav file copied from your Nintendo Switch placed in the folder with the undertale_save_converter.exe file.
   This file can be obtained from a modded switch by using tools such as Checkpoint or JKSM.
   - Checkpoint: https://gbatemp.net/threads/checkpoint-a-simple-and-fast-save-manager.485591
   - JKSM: https://github.com/J-D-K/JKSM
2. Use your command prompt to browse to the folder, then execute `undertale_save_converter.exe` and select the second menu option.
3. Alternately (if you want to run the script via python), execute `python undertale_save_converter.py` (requires Python 3 to be installed).


### Compiling the executable (if you don't want to download and use the supplied undertale_save_converter.exe file)
1. Install Python 3.4 (x86) on a Windows computer, making sure you select the option to add Python to your path.
2. Install the Py2Exe utility (`py -3.4 -m pip install py2exe`) - https://pypi.org/project/py2exe/
3. Install pywin32-221.win32-py3.4.exe from https://sourceforge.net/projects/pywin32/files/pywin32/Build%20221/
4. Check out this git repo to a folder on your local computer.
5. Browse to the folder and execute `pip install -r requirements.txt` (to install dependencies).
6. Execute `py -3.4 -m py2exe.build_exe undertale_save_converter.py` to compile the undertale_save_converter.py file to an .exe file.
7. Look inside the `dist` folder for your newly created `undertale_save_converter.exe` file!
