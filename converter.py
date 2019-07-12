# Undertale Game Save Converter (For PC and Switch)
# https://github.com/tomchapin/undertale-save-converter

#############################################################################################
# Imports
#############################################################################################

import msvcrt  # For getting user input on Windows (we use this on our main menu)
import subprocess  # For executing a shell command (we use this to clear the screen)


#############################################################################################
# Helper Methods
#############################################################################################

def clear_screen():
    """
    Clears the terminal screen.
    Only compatible with Windows.
    """
    return subprocess.call("cls", shell=True) == 0


#############################################################################################
# PC to Switch
#############################################################################################

def pc_file_to_switch_text(input_file):
    """
    Converts all of the PC file's lines to a single line of text meant for the Switch game save file
    """
    result = ''
    file_contents = input_file.read()

    for cnt, line in enumerate(file_contents):
        # Remove line break character from end of line
        new_line = line.replace("\n", '')

        # Strip spaces from the end of line
        new_line = new_line.rstrip()

        if cnt+1 < len(file_contents):
            # Add on line break characters (unless this is the very last line)
            new_line = new_line + "\\r\\n"

        result += new_line

    return result


def pc_undertale_ini_to_switch_text(input_file):
    """
    Converts all of the undertale.ini file's lines to a single line of text meant for the Switch game save file
    """
    result = ''
    file_contents = input_file.read()

    for cnt, line in enumerate(file_contents):
        # Remove line break character from end of line
        new_line = line.replace("\n", '')

        if not new_line.startswith("["):
            # Escape quotes on any non-header lines
            # For Example: Room="31.000000"
            #     Becomes: Room=\"31.000000\"
            r = new_line.split("=")
            p = r[1].split('"')
            p = p[1]
            new_line = r[0] + '=\\"' + p + '\\"'

        # Add on line break characters to end of the line
        new_line = new_line + "\\r\\n"

        result += new_line

    # Replace double line endings before section headers with a single carriage return
    result = result.replace("\\r\\n[", "\\r[")

    return result
    

def convert_from_pc_to_switch():
    clear_screen()
    print("Converting from PC to switch...")

    pc_file9 = open("file9", "r")
    pc_file0 = open("file0", "r")
    pc_undertale_ini = open("undertale.ini", "r")
    switch_undertale_sav = open("undertale.sav", "w")

    switch_undertale_sav.write('{ "default": "", "file9": "')
    switch_undertale_sav.write(pc_file_to_switch_text(pc_file9))
    switch_undertale_sav.write('", "config.ini": "", "undertale.ini": "')
    switch_undertale_sav.write(pc_undertale_ini_to_switch_text(pc_undertale_ini))
    switch_undertale_sav.write('", "file0": "')
    switch_undertale_sav.write(pc_file_to_switch_text(pc_file0))
    switch_undertale_sav.write('" }')
    switch_undertale_sav.write(chr(0))

    pc_file9.close()
    pc_undertale_ini.close()
    pc_file0.close()
    switch_undertale_sav.close()

    print("Done! Your new undertale.sav file is ready!")


#############################################################################################
# Switch to PC
#############################################################################################

def undertale_save_contents():
    switch_undertale_sav = open("undertale.sav", "r")

    # Load the single run-on line of text from the undertale.sav file
    contents = switch_undertale_sav.read()

    # Close the file handle
    switch_undertale_sav.close()

    return contents


def file9_content_from_switch_save():
    return undertale_save_contents().split('"file9": "')[1].split('", "config.ini"')[0]


def undertale_ini_content_from_switch_save():
    return undertale_save_contents().split('"undertale.ini": "')[1].split('", "file0"')[0]


def file0_content_from_switch_save():
    return undertale_save_contents().split('"file0": "')[1].split('" }')[0]


def switch_file_text_to_pc_file_lines(extracted_text):
    result = ''

    # Convert all the line endings to PC line endings
    lines = extracted_text.split("\\r\\n")

    for cnt, line in enumerate(lines):
        if cnt == 0:
            # First line doesn't have an extra space before the line ending
            result += line + "\n"
        elif cnt+1 == len(lines):
            # The last line has a space, but does not have a line ending
            result += line + " "
        else:
            # Every following line has an extra space right before the line ending
            result += line + " \n"

    return result


def switch_undertale_ini_to_pc_file_lines(extracted_text):
    return extracted_text.replace('\\r\\n', "\n").replace('\\r', "\n").replace('\\"', '"')


def convert_from_switch_to_pc():
    clear_screen()
    print("Converting from Switch to PC...")

    pc_file9 = open("file9", "w")
    pc_file9.write(switch_file_text_to_pc_file_lines(file9_content_from_switch_save()))
    pc_file9.close()

    pc_file0 = open("file0", "w")
    pc_file0.write(switch_file_text_to_pc_file_lines(file0_content_from_switch_save()))
    pc_file0.close()

    pc_undertale_ini = open("undertale.ini", "w")
    pc_undertale_ini.write(switch_undertale_ini_to_pc_file_lines(undertale_ini_content_from_switch_save()))
    pc_undertale_ini.close()

    print("Done! Your new PC game save files are ready!")


#############################################################################################
# Menu
#############################################################################################

def display_menu():
    clear_screen()
    print("")
    print("  -------------------------------------")
    print("  Undertale PC/Switch Save Converter")
    print("  -------------------------------------")
    print("")
    print("  1. Convert from PC to Switch")
    print("     Make sure you have copied your game's file0, file9, and undertale.ini files to this folder.")
    print("     (These files are typically located in your system's %LocalAppData%\\UNDERTALE\\ folder)")
    print("")
    print("  2. Convert from Switch to PC")
    print("     Make sure you have the undertale.sav file copied from your Nintendo Switch.")
    print("     This file can be obtained from a modded switch by using tools such as Checkpoint or JKSM.")
    print("     Checkpoint: https://gbatemp.net/threads/checkpoint-a-simple-and-fast-save-manager.485591")
    print("           JKSM: https://github.com/J-D-K/JKSM")
    print("")
    print("  Press (1) or (2) to select a menu option, or press (Escape) to exit:")

    user_input = msvcrt.getch()
    if user_input == b'1':
        # 1 was pressed
        convert_from_pc_to_switch()
    elif user_input == b'2':
        # 2 was pressed
        convert_from_switch_to_pc()
    elif user_input == b'\x1b':
        # Exit, because escape key was pressed
        return
    else:
        # An unrecognized key was pressed, so we clear the screen and display the menu again
        display_menu()


if __name__ == '__main__':
    display_menu()
