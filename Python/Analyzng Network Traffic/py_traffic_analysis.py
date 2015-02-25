#!/usr/local/bin/python3

import sys
import os
import stat
import time

''' =======AUTHOR - AVIK RANJAN BHATTARAI =====
    |      SCRIPT ASSIGNMENT - PYTHON         |
    |   DATE OF SUBMISSION: 04/14/14          |
    |            TRAFFIC ANALYSIS             |
    ===========================================
'''

while True: #continuous loop
    path = "/users/avikrb/desktop/py_hw_3/log_files"#this is the destination for the log files I used as samples

    #initializing dictionaries, lists and strings that I will be using later on
    src_ip = {}
    dest_ip = {}
    time_dict = {}
    syn_flood = {}
    list_1 = []
    list_2 = []
    list_3 = []
    key = None
    value = None


    for file in os.listdir(path):#processing a single file at a time
        #print (file)
        fullfile = os.path.join (path, file)#merging the full path name
        filestats = os.stat(fullfile)
        created_time = (filestats.st_ctime) # file created time
        current_time = (time.time()) #current time in seconds
        total_time = current_time - created_time #this determines whether the file was created within a certain mentioned time, in this case past 5secs
        #print ("STEP 1 DONE ======")
        if total_time < 5:#if file was created in the past 5 seconds, move on
            #print ("STEP 2 DONE ======")
            file_open = open(fullfile)
            
            while True:#enter loop
                lines = file_open.readline()#read one line of entry at a time
                lines = lines.strip() #removes the \n, which usually is added to the list 
                if not lines:
                    file_open.close()#if no lines were read, close file and break
                    break

                else:
                    #print (lines)
                    packet_split = lines.split(":")#splits the entire packet into different fields
                    srcIP = packet_split[1] #assigning the source IP address
                    src_ip.setdefault(srcIP,[]).append(lines) #setdefault intializes the value for the key and if key exists it does nothing
                    #print (srcIP)
                    destIP = packet_split[3]
                    dest_ip.setdefault(destIP,[]).append(lines) #assigning dictionary dest_ip with key "destIP" and value "lines"
                    dictTime = int(int(packet_split[0]) / 60) # time mod 60 gives us only the minute as an interger
                    time_dict.setdefault(dictTime,[]).append(lines) #assigning dictionary time_dict with key "dictTime" and value "lines"
                    
                           

    for i in range (1,2):#print empty lines...just so that output is easy to read. You will find this in multiple places
        print ("\n")

    #print ("======= BRACE YOURSELF ---- TIME FOR TEST ======")

    #Ping attack test
    print ("*****>>>>>>>>PING ATTACK<<<<<<<*****")
    for key,value in src_ip.items():#source IP ping attack test. Multiple nested for loops so that each "value" for any key is processed
        count = 0 # count is created to keep records
        check_time = int(value[0].split(":")[0]) #check_time is later used to compare if other ping packets were sent within 1 minute.
        
        for one_value in value: #considering one "value" at a time
            if (one_value.split(":")[5] == "ICMP") & (((int(one_value.split(":")[0])) - (check_time))<=60): #checking the type field and the time packet was sent
                count = count + 1
                if not (one_value.split(":")[3]) in list_1: #if the entry does not already exists then append it to the list
                    list_1.append(one_value.split(":")[3])
            
        if count >= 5:
            print ("SOURCE-", key, "\t", "Attacked Destinations- ", sorted(list_1)) #print the result

    for key,value in dest_ip.items():#destination IP ping attack test - same as previous one
        count = 0
        check_time = int(value[0].split(":")[0])
        
        for one_value in value:
            if (one_value.split(":")[5] == "ICMP") & (((int(one_value.split(":")[0])) - (check_time))<=60):
                count = count + 1
                if not (one_value.split(":")[1]) in list_2:
                    list_2.append(one_value.split(":")[1])
            
        if count >= 5:
            print ("Attacked Destination-", key, "\t", "Sources- ", sorted(list_2))



    for i in range (1,2):
        print ("\n")

    #Christmas tree attack test
    print ("*****>>>>>>>>CHRISTMAS TREE ATTACK<<<<<<<*****")
    all_flags_on = ["ACK","FIN","RST","SYN"] #creating a list which is used to compare to check if all the flag are turned on or not
    for key,value in src_ip.items():#looping through one key and one value at a time from the source IP dictionary
        count = 0
        for one_value in value:
            type_list_1 = one_value.split(":")[6] #creating a list out of the last field which is the flag field originally inside "[ ]"
            type_list_2 = type_list_1.strip("[]") #getting rid of the "[]"
            type_list_3 = type_list_2.split(",")#finally the list is created with the flags
            #print (sorted(type_list_3))
            if sorted(type_list_3) == all_flags_on: #comparing the packet flags with the all_flags_on list to see if all the flag are turned on
                list_3.append(key)
    print ("Christmas attack IPs- \t",sorted(list_3))

    for i in range (1,2):
        print ("\n")


    ''' =======AUTHOR - AVIK RANJAN BHATTARAI =====
        |      SCRIPT ASSIGNMENT - PYTHON         |
        |   DATE OF SUBMISSION: 04/14/14          |
        |            TRAFFIC ANALYSIS             |
        ===========================================
    '''

    #SYN FLOOD test
    print ("*****>>>>>>>SYN FLOOD ATTACK<<<<<<*****")
    for key, value in src_ip.items():#looping over one key and one value at a time for both source and destination dictionaries
        for k,v in dest_ip.items():
            if key == k:
                for value_1 in value:
                    for ONE_VALUE in v:
                        if (value_1.split(":")[3] == ONE_VALUE.split(":")[1]) & (value_1.split(":")[4] == ONE_VALUE.split(":")[2]):#checking destination ip & dest port fields
                            type_list_11 = value_1.split(":")[6] #creating a list out of the last field which is the flag field originally inside "[ ]"
                            type_list_22 = type_list_11.strip("[]")#getting rid of the "[]"
                            type_list_33 = type_list_22.split(",")#finally the list is created with the flags
                            type_list_111 = ONE_VALUE.split(":")[6]#same as above but for the data in destination dictionary
                            type_list_222 = type_list_111.strip("[]")
                            type_list_333 = type_list_222.split(",")
                            
                            if ((type_list_33 == ["SYN"]) & (type_list_333 == ["SYN","ACK"])) | (type_list_33 == ["ACK"]):#check to see if syn and syn,ack OR ack flags are turned on
                                
                                for value_again in value:#loop again
                                    syn_flood.setdefault(key,[]).append(value_again)#append only those with that met the condition 

    for key,value in syn_flood.items():#looping through the syn_flood dictionary that as speicific keys and values
        for check_value in value:
            type_list_a = check_value.split(":")[6]#logic same as illustrated above
            type_list_b = type_list_a.strip("[]")
            type_list_c = type_list_b.split(",")
            if type_list_c == ["SYN"]:#if the flag field is only syn, then count =1 meaning there is no ack packet
                count = 1
            elif type_list_c == ["ACK"]:#if flag field is only ack, then count =0
                count = 0
        if count == 1:#if count is 1 then it simply means there was no ack packet. Indicating that a syn flood was present
            print ("SYN FLOOD source IP- ", key, "\n" "SYN FLOOD Destination IP - ", check_value.split(":")[3], "\n")

    for i in range (1,2):
        print ("\n")

    #UDP attack
    count = 0
    print ("*****>>>>>>>>UDP ATTACK<<<<<<<*****")
    for key, value in src_ip.items():#looping over source and destination dictionaries
        for k,v in dest_ip.items():
            if key == k:
                count = 0
                for value_1 in value:
                    
                    for ONE_VALUE in v:
                        #condition test below compares time (eg, packet 2 is acknowledgement for packet 1, and if we do not check time field then the loop checks packet 2 with may be other packets)
                        #condition further checks destination and source IPs, destination port numbers and protocols
                        if (int(value_1.split(":")[0]) < (int(ONE_VALUE.split(":")[0]))) & (value_1.split(":")[3] == ONE_VALUE.split(":")[1]) & (value_1.split(":")[4] == ONE_VALUE.split(":")[2]) & (value_1.split(":")[5] == "UDP") & (ONE_VALUE.split(":")[5] == "ICMP"):
                            count = count + 1
                            
                if count >= 2:
                    print ( "SOURCE- ", key, "***UDP ATTACK*** DESTINATION- ", value_1.split(":")[3])
                
    time.sleep(5) #delay by 5 seconds, effect similar to program running every 5seconds.                       
''' =======AUTHOR - AVIK RANJAN BHATTARAI =====
    |      SCRIPT ASSIGNMENT - PYTHON         |
    |   DATE OF SUBMISSION: 04/14/14          |
    |            TRAFFIC ANALYSIS             |
    ===========================================
'''




                            
            





