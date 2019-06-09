# Hervé Nyemeck
# This python file renames cover photos inside album folders based on folder name
# Format: 'Album Name Like This.suffix'
# Requires The folder name to be the album's name

import os, sys, imghdr
AlbumsPath = os.getcwd() # Stores album directory in folder this file was run in
dirs = os.listdir(AlbumsPath)
print(dirs)
for directory in dirs:
    os.chdir(directory)
    print(os.getcwd())
    os.listdir(os.getcwd())
    os.chdir('..')