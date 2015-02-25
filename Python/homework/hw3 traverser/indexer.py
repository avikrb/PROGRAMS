#from data_load import data_list
#using i for index value. it loops along with quote, so data_list[5] would later on be equal as i = 5
import pickle
import shelve
import os
import stat
query = "sorry"
'''
def get_dictionary(data_list):
    i=0
    dictionary1={}
    for quote in data_list:
        words = (quote.split(" "))
        for each_word in words:
            each_word = each_word.lower().rstrip("\'\"-,.:;!?s")#get rid of the punctuations at the end of words and most importantly remove rightmost"s" ->> used for "sheep" "sheeps"
            dictionary1.setdefault(each_word,[]).append(i)#setdefault intializes the value for the key and if key exists it does nothing
            dictionary1[each_word] = list(set(dictionary1[each_word]))#get rid of duplicates and convert back to a list
            dictionary1[each_word].sort()#useful for sorted printout later on
        i = i+1
    return dictionary1
'''

def create_dictionary():
    dictionary1={}
    r = open("/users/avikrb/desktop/raw_data.pickle","rb")
    s = pickle.load(r)
    create_shelve = shelve.open("dictionary_data")
    for file_path, file_content,modtime,filesize in s:
        file_content = file_content.split(" ")
        for each_word in file_content:
            each_word = each_word.lower().rstrip("\'\"-\\,.:;!?")
            time_path_size_tuple = (file_path,modtime,filesize)
            dictionary1.setdefault(each_word,[]).append(time_path_size_tuple)
            dictionary1[each_word]=list(set(dictionary1[each_word]))#get rid of same multiple filepaths
    for key,value in dictionary1.items():
        create_shelve[key]=(value)
    r.close()
    create_shelve.close()
        



