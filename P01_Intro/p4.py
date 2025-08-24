print('q4')
#program to print the contents of a directory using the os module. Search online for the function which does that. with comments
import os

# Specify the directory (use '.' for current directory)
directory = '/'

try:
    # Get the list of files and directories
    contents = os.listdir(directory)

    print(f"Contents of directory '{directory}':")
    for item in contents:
        print(item)

except FileNotFoundError:
    print(f"The directory '{directory}' does not exist.")
except PermissionError:
    print(f"Permission denied for accessing '{directory}'.")
