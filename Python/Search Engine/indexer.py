import pickle
import shelve
import os
import re
import stat

def create_shelve(*file1):
    dictionary1={}
    for file in file1:
        PATH = os.path.join(os.getcwd(),file)
        r = open(PATH,"rb")
        s = pickle.load(r)
        create_shelve = shelve.open("dictionary_data")
        for file_path, file_content in s:
            file_content = file_content.split(" ")
            for each_word in file_content:
                each_word = each_word.lower().rstrip(" \'\"-\\,.:;!?")
                dictionary1.setdefault(each_word,[]).append(file_path)
                dictionary1[each_word]=list(set(dictionary1[each_word]))#get rid of same multiple filepaths
    for key,value in dictionary1.items():
        create_shelve[key]=(value)
    r.close()
    create_shelve.close()        
