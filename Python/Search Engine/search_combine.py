from data_load import traverser
import indexer
from searcher import search
from web_crawler import visit_url
from web_crawler import web_crawler
from weather import get_weather

#uncomment traverser, web_crawler and indexer when needed, they all work

#traverser()
#web_crawler()
#indexer.create_shelve("raw_data.pickle","url_data.pickle")

#I am asking my query in the combine_search.py because I would need it for other modules as well, eg. weather

print("\n\n"+"===>>> Welcome to Avik's Search Engine <<<===")
query = input("Query: ")
query = query.lower().strip(" ") #get rid of the front and rear spaces
query = query.split(" ") #take every word into a list with a space being the delimiter
query = list(set(query)) #removes repeated items from the list and converting back to list from set
if ("or" in query) and ("and" not in query):#if "and" is present, "and" operation should take place
    query.remove("or")#get rid of the "or" content from the list
    search_type = "or"
#elif performs "and" operation search, user could just type "flower sheep" without operator
elif ("and" in query) or (len(query)>1 and ("and" not in query)and("or" not in query)):
    if "and" in query:
        query.remove("and")
    if "or" in query:
        query.remove("or")
    search_type = "and"
else:
    search_type = ""#when user inputs only one string this no particular search type is used



get_weather(query)
search(query,search_type,"dictionary_data")

#so far working with only title and metadata. 
