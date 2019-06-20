# Hervé Nyemeck
# This python file renames cover photos inside album folders based on folder name
# Format: 'Album Name Like This.suffix'
# Requires The folder name to be the album's name

import os, sys, imghdr, re

regex1 = '(.*)?(?=(\([A-Za-z]*\))|(?:[\s][-\(]))|(?<=\d\d\d\d\)\s)([a-zA-Z].*)|([a-zA-Z]*)(?=\-\d\d\d\d)'
#regex1 = '(.*)?(?=(\([A-Za-z]*\))|(?:[\s][-\(]))' # This grabs line upto and not including space followed by - or ( and accounts for words inside parantheses 
dash = '-'
paren = '('

ArtistsPath = os.getcwd()
Artists = os.listdir(ArtistsPath)
for direct in Artists:
    if direct != "Missing Albums.txt":
        os.chdir(direct)
        AlbumsPath = os.getcwd() # Stores album directory in folder this file was run in
        dirs = os.listdir(AlbumsPath)

        i = 0
        for directory in dirs:
            nL = len(directory)
            # print(directory[(nL-3):])
            # if directory[(nL-3):] != '.py' and directory[(nL-3):] != '.7z':  #Checking file extension vs file type, try type check
            if directory[(nL-3):] not in ('.py', 'txt', '.7z', '.log'):
                os.chdir(AlbumsPath + '\\' + directory)
                tempDir = os.listdir(os.getcwd())
                found = False
                count = 1
                for songFiles in tempDir:
                    sL = len(songFiles)
                    dot = songFiles.index('.')
                    #if songFiles[dot:sL] == '.png' or songFiles[dot:sL] == '.jpg':
                    if songFiles[dot:sL] in ('.png', '.jpg', '.jpeg'):
                        found = True
                        filext = songFiles[dot:sL]
                        if dash in directory or paren in directory:
                            matchObj = re.search(regex1, directory)
                            matchInd = matchObj.span()  #span creates tuple of indexes, 
                            match = directory[matchInd[0]:matchInd[1]]
                            newName = match + filext
                            if count > 1:
                                newName = match + ' ' + str(count-1) + filext
                            os.rename(songFiles, newName)
                        else:
                            newName = directory + filext
                            if count > 1:
                                newName = directory + ' ' + str(count-1) + filext
                            os.rename(songFiles, newName) # Add if statement that checks for spaces and other characters between dot and filext
                        i += 1
                        count += 1
                        
                if not found:
                    #Write to logfile
                    missing = os.getcwd()
                    os.chdir(ArtistsPath)
                    log = open("Missing Albums.txt", "a+")
                    #if missing not in log:
                    log.write(missing + " is missing an album cover\n")
                    log.close()
        
        if os.getcwd() != ArtistsPath:
            os.chdir(ArtistsPath)            

#Current corner cases 
# (Year) - Album Title
# Bakuretsu Tricot-san
# T H E
# Year - Album Title
# AlbumTitle [bitrate]