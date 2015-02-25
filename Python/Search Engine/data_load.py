import os
import fnmatch
import pickle
import time

def traverser():
    main_list = []
    path = "/users/avikrb/desktop/fortune1" #folder destination
    for dir_path, folders, files in os.walk(path):#walk goes over each file and subfolder
        for single_file in files:
            if (fnmatch.fnmatch(single_file,"*txt")) or (fnmatch.fnmatch(single_file,"*log")):
                #print ("Reading..",single_file)
                file_path=(os.path.join(dir_path,single_file))
                f = open(file_path)
                filestats = os.stat(file_path)
                filesize= (filestats.st_size)
                filesize="File size= "+str(filesize)+" bytes"
                modtime = (time.strftime("%m/%d/%Y %I:%M:%S %p",time.localtime(os.path.getmtime(file_path))))
                #FORMATING THE TIME TO READABLE FORMAT..eg: 03/25/2014 04:50:49 PM
                modtime = "Modified Time= "+str(modtime)
                temp_tuple = (os.path.join(dir_path,single_file)+modtime+filesize,f.read())
                #print (temp_tuple)
                main_list.append(temp_tuple)
                f.close()
        
    path_write = os.getcwd() + "/raw_data.pickle"
    write_to_file= open (path_write,"wb")
    pickle.dump(main_list,write_to_file)
    #print(main_list)

