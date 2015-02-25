#!/usr/local/bin/python3

'''
AUTHOR: AVIK RANJAN BHATTARAI
PYTHON PROGRAM TO SHOW REPORTS FOR USERS IN THE PASSWD FILE AND GROUP FILE
DATE OF SUBMISSION: 03/17/2014
'''

'''
USER INPUTS THE FILE LOCATION FOR PASSWD AND GROUP FILE
'''
filepath1 = input ("enter passwd filepath: ")
filepath2 = input ("enter group filepath: ")
pwdfile = open (filepath1)
grpfile = open (filepath2)


#pwdfile = open('/users/avikrb/downloads/passwd(2)')
#grpfile = open('/users/avikrb/downloads/group(2)')

while True:
#INFINITE LOOP TO READ CONTENTS OF PASSWD FILE

    print ("\n")
    pwdline = pwdfile.readline()
    #EXTRACT SINGLE LINE FROM PASSWD FILE

    username = pwdline.split(":")[0]
    #EXTRACT THE USERNAME FIELD'''
    if not pwdline:
    #IF END OF FILE FOR PASSWD FILE THEN BREAK LOOP
        break
    grpfile.seek(0)
    #GROUP FILE POINTER RESET TO 0
    print (username, ":","  ", end="")
    while True:
    #INFINITE LOOP TO READ CONTENTS OF GROUP FILE
        grpline = grpfile.readline()
        #EXTRACT SINGLE LINE FROM GROUP FILE
        if not grpline:
        #IF END OF FILE FOR GROUP FILE THEN BREAK LOOP
                break
        a = grpline.split(":")[3]
        #SPLIT THE MEMBERS OF THE GROUP AND ASSIGN TO a

        #CONDITION TESTS
        if (pwdline.split(":")[3] == grpline.split(":")[2]) and a.find(username) >= 0:
            print (grpline.split(":")[0], ":", "  ", end="")
        elif (a.find(username) >= 0):
            print (grpline.split(":")[0], end="")
            print (", ", end="")
        continue
