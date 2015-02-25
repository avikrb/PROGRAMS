from datetime import datetime
import shelve

def search(query,search_type,*file1):
    dt1 = datetime.now()#initial datetime record followed by main search program
    print ("Performing", search_type.upper(), "search for", query)


    for file in list(file1):
        dictionary = shelve.open(file,writeback=False)
        list_or = []    
        if search_type == "and":
            try:
                dict_list_1 =  dictionary[query[0]]#dict_list_1 is just a list and not a dictionary, it contains the "values" of dictionary[query[0]]
                for value1 in query[1:]:#basic logic here is: take all posibilites of query[0] and compare with everything beyond query[1:] to see if any index overlaps
                    dict_list_2 = dictionary[value1]#dict_list_2 is also a list, and contains values of every query keys in dictionary
                    dict_list_1 = list(set(dict_list_1).intersection(dict_list_2))#checks the common index and assigns to dict_list_1
                    dict_list_1.sort()#sort the list useful during final printout
                for each_element in dict_list_1:#loop through all values in dict_list_1 and prinout. dict_list_1 now has all the "and" values of the query
                    print("-->> Found at: ", each_element)
            except:
                print("not found!!")
        elif search_type == "or":
            for each_value in query:
                try:
                    list_or = list_or + dictionary[each_value]#list_or is a list and we add the indexes of every query key from dictionary
                    list_or = list(set(list_or))#to get rid of duplicates/commons
                    list_or.sort()#useful for printing out in order
                    for every_value in list_or:
                        print ("-->> Found at: ", every_value)
                except:
                    print ("No search result for ", each_value)
        else:#finally, if user enters just one string
            try:
                for value in dictionary[query[0]]:
                    print ("-->> Found at: ", value)
            except:
                print("Not found")
    dt2 = datetime.now()
    print("Execution time:", dt2.microsecond-dt1.microsecond, "\n\n")
    dictionary.close()

