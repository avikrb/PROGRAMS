#! /usr/local/bin/python3

''' =======AUTHOR - AVIK RANJAN BHATTARAI =====
    |      SCRIPT ASSIGNMENT - PYTHON         |
    |   DATE OF SUBMISSION: 03/26/14          |
    ===========================================
'''

#IMPORTING BASIC AND FEW ADDITIONAL MODULES
import sys
import os
import stat
import pwd
import collections
import time


print ("Do checks related to path variable  --> Press '1' ") #OPTIONS FOR USERS
print ("Do checks related to /etc directory --> Press '2' ")
option = str(input("What do you want to check today??"))

if option == "1": #OPTION 1 IS TO PERFORM CHECKS WITH PATH VARIABLE
    
    path = sys.path #SPECIFYING path AS sys.path
    #path = ["/users/avikrb/desktop/trialfolder"]

    case1 = []#INITIALIZING LISTS, EACH CASE IS TO SIGNIFY ONE OF THE 3 REQUIREMENTS OF THE QUESTION
    case2 = []
    case3 = []

    print ("==================================================")
    for current in path:

        if current.find("./") < 0:
            for info in os.walk(current):
       
                for file in info[2]:#GET INFO ON EACH DIRECTORY
                    fullfile = os.path.join(info[0], file)#CREATE FULL PATH NAME
                    filestats = os.stat(fullfile)#GET STAT INFO OBJECT
                    #print (filestats)
                    if filestats.st_mode & (stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH):  # checking for execute bits set
                        
                        if filestats.st_mode & stat.S_ISUID:
                            if filestats.st_mode & stat.S_IWOTH: #check if suid is set and check if write permission for non owner
                                case1.append(fullfile)
                                
                            if filestats.st_mode & stat.S_IWUSR: #check if write permission for owner and set uid on
                                case2.append(fullfile)
                                
                        if not (filestats.st_mode & stat.S_ISUID):
                            if filestats.st_mode & stat.S_IWOTH: #check if suid is not set and write permission for non owner
                                case3.append(fullfile)
           

        else:
            print ("===ERROR=== Path variable includes current directoy '.' ")
            break

    for i in range (1,4): #LOOPING TO PRINT "=======" FOR EASILY DISTINGUISHING SECTIONS OF DATA
        print ("===========================================================================================")
   
    print("Final list of all executable files with SUID set and WRITE permission for NON OWNER:")

    for file in sorted(case1, key=str.lower) :          #LOOP THROUGH various "LISTS" AND PRINT in aplhabetical order
        print(file)

    for i in range (1,4):
        print ("===========================================================================================")
        
    print("Final list of all executable files with SUID set and WRITE permission for OWNER:")
    for file in sorted(case2, key=str.lower) :          
        print(file)


    for i in range (1,4):
        print ("===========================================================================================")
        
    print("Final list of all executable files with SUID NOT set and WRITE permission for NON OWNER:")
    for file in sorted(case3, key=str.lower) :          
        print(file)





    ''' =======AUTHOR - AVIK RANJAN BHATTARAI =====
        |      SCRIPT ASSIGNMENT - PYTHON         |
        |   DATE OF SUBMISSION: 03/26/14          |
        ===========================================
    '''
    
elif option == "2": #OPTION 2 IS TO PERFORM CHECKS WITH /etc DIRECTORY
    
    etc = "/etc" #SPECIFYING PATH FOR EASE OF USE

    case1 = [] #case1 IS A LIST USED TO STORE INFO FOR PART 1 OF THE REQUIREMENT
    time_change_dict = {} #I USED DICTIONARY FOR THE 2 nd and 3rd parts OF THE REQUIREMENT
    time_mod_dict = {} #I GLUED THE TIME AND FILENAMES IN A DICTIONARY [KEY:VALUE]..SO I COULD LATER PRINT IN ORDER OF THE "KEY" WHICH WOULD BE TIME IN THIS SCRIPT 

    for file in os.listdir(etc):
        
        fullfile = os.path.join (etc, file) #CREATING FULL FILE PATH
        filestats = os.stat(fullfile) #STAT INFO OBJECT FOR FILE
        
        
        if filestats.st_mode & stat.S_IWOTH: #DOING CHECKS FOR WRITE PERMISSION FOR OTHERS
            ownername = pwd.getpwuid(filestats.st_uid).pw_name #GETTING THE OWNER NAME
            case1.append("Filename: "+ file + str("  ")+ "Owner: " + ownername +str("  ")+ "Permission: "+str(oct(filestats.st_mode)))
            #MERGING REQUIRED INFO AND APPENDING TO LIST NAMED AS case1
            
        modtime = filestats.st_mtime #GETTING THE MODIFIED TIME FOR THE FILE
        current_time = time.time() # GETTING THE CURRENT TIME
        totaltime = ((current_time - modtime)/3600) #CALCULATING THE TIME DIFFERENCE AND GETTING IN HOUR FORMAT
        

        if totaltime < 24: #IF THE TIME CHANGE IS LESS THAN 24 HOURS DO THE FOLLOWING
            format_mod_time = (time.strftime("%m/%d/%Y %I:%M:%S %p",time.localtime(os.path.getmtime(fullfile))))
            #FORMATING THE TIME TO READABLE FORMAT..eg: 03/25/2014 04:50:49 PM
            
            time_mod_dict [format_mod_time] = file #ADDING KEY AND VALUE IN A DICTIONARY, KEY IS THE MODIFIED TIME and VALUE IS THE REST OF THE INFORMATION
            

        changetime= filestats.st_ctime#CHECKS FOR THE CHANGE IN PROPERTIES OF THE FILE..STEPS ARE SAME AS ABOVE
        totaltime2=((current_time - changetime)/3600)
        if totaltime2 < 24:
            file_permission = file + str("   ") + "Permission- "+str(oct(filestats.st_mode))
            format_change_time = (time.strftime("%m/%d/%Y %I:%M:%S %p",time.localtime(os.path.getctime(fullfile))))
            time_change_dict [format_change_time] = file_permission

    for i in range (1,4):
        print ("===========================================================================================")           

    print ("Files that have write access other than root are: ")
    for file in sorted(case1, key=str.lower) :# LOOPING THROUGH LISTS AND DICTIONARY TO PRINT FILES IN A SORTED WAY
        print(file)

    for i in range (1,4):
        print ("===========================================================================================")

    print ("Files that were modified within the past 24 hours are: ")
    order = collections.OrderedDict(sorted(time_mod_dict.items()))
    for key,value in order.items():
        print (value, "last modified on ", key)

    for i in range (1,4):
        print ("===========================================================================================")

    print ("Files whose properties were changed within the past 24 hours are: ")
    order2 = collections.OrderedDict(sorted(time_change_dict.items()))
    for key,value in order2.items():
        print (value, "changed properties on", key)

    
else:
    print ("===INVALID ENTRY===")

print ("===============================================================")



''' =======AUTHOR - AVIK RANJAN BHATTARAI =====
    |      SCRIPT ASSIGNMENT - PYTHON         |
    |   DATE OF SUBMISSION: 03/26/14          |
    ===========================================
'''
