from datetime import datetime
from data_load import data_list
from indexer import create_dictionary
import shelve

def search(db_file):
 #   dictionary = dictionary_DATA
    dictionary = shelve.open("dictionary_data",writeback=False)
    #print("\n\n",list(dictionary["something"]))
    list_or = []    
    query=input("query:")
    query = query.lower().strip(" ") #get rid of the front and rear spaces
    query = query.split(" ") #take every word into a list with a space being the delimiter
    query = list(set(query)) #removes repeated items from the list and converting back to list from set
    query.sort()#sorts the list in alphabetical order
    i=0
    if ("or" in query) and ("and" not in query):#if "and" is present, "and" operation should take place
        query.remove("or")#get rid of the "or" content from the list
        search_type = "or"
    #elif performs "and" operation search, user could just type "flower sheep" without boolean operator
    elif ("and" in query) or (len(query)>1 and ("and" not in query)and("or" not in query)):
        if "and" in query:
            query.remove("and")
        if "or" in query:
            query.remove("or")
        search_type = "and"
    else:
        search_type = " "#when user inputs only one string this no particular search type is used

    dt1 = datetime.now()#initial datetime record followed by main search program
    print ("Performing", search_type.upper(), "search for", query)

    for each_item in query:#looping to see if user's query is in search content, if not we print out search not found
        if each_item in dictionary.keys():
            positive_value = 1#if user's query is found, then set positive_value to 1
        else:
            positive_value = 0#if not then set it to 0 and break
            break

    if positive_value == 1:#we perform the search only if the positive_value is set to 1, else print search not found
        if search_type == "and":
            dict_list_1 =  dictionary[query[0]]#dict_list_1 is just a list and not a dictionary, it contains the "values" of dictionary[query[0]]
            for value1 in query[1:]:#basic logic here is: take all posibilites of query[0] and compare with everything beyond query[1:] to see if any index overlaps
                dict_list_2 = dictionary[value1]#dict_list_2 is also a list, and contains values of every query keys in dictionary
                dict_list_1 = list(set(dict_list_1).intersection(dict_list_2))#checks the common index and assigns to dict_list_1
                dict_list_1.sort()#sort the list useful during final printout
            for each_element in dict_list_1:#loop through all values in dict_list_1 and prinout. dict_list_1 now has all the "and" values of the query
                print("-->> Found at: ", each_element)

        elif search_type == "or":
            for each_value in query:
                list_or = list_or + dictionary[each_value]#list_or is a list and we add the indexes of every query key from dictionary
            list_or = list(set(list_or))#to get rid of duplicates/commons
            list_or.sort()#useful for printing out in order
            for every_value in list_or:
                print ("-->> Found at: ", every_value)
                
        else:#finally, if user enters just one string
            for value in dictionary[query[0]]:
                print ("-->> Found at: ", value)
    else:
        print ("\t\t*********No results found********* ")

    dt2 = datetime.now()
    print("Execution time:", dt2.microsecond-dt1.microsecond)
    dictionary.close()

