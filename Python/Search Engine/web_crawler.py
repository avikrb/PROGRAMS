import urllib.request
from urllib.error import  URLError
import re
import os
import pickle


def visit_url(url, domain):
    global crawler_backlog
    global MainList
    if(len(crawler_backlog)>100):
    	return
    if(url in crawler_backlog and crawler_backlog[url] == 1):
        return
    else:
        crawler_backlog[url] = 1
        #print("Processing:", url)

    try:
        page = urllib.request.urlopen(url)
        code=page.getcode()
        if(code == 200):
            content=page.read()
            content_string = content.decode("utf-8")
            #print (content_string)
            regexp_title = re.compile('<title>(?P<title>(.*))</title>')
            regexp_keywords = re.compile('<meta name="keywords" content="(?P<keywords>(.*))" />')
            regexp_url = re.compile("http://"+domain+"[/\w+]*")
            result = regexp_title.search(content_string, re.IGNORECASE)
            if result:
                title = result.group("title")
                #print(title)
                TempTuple = (url,title)
                MainList.append(TempTuple)
            result = regexp_keywords.search(content_string, re.IGNORECASE)
            if result:
                keywords = result.group("keywords")
                #print(keywords)
                TempTuple1 = (url,keywords)
                MainList.append(TempTuple)
            for (urls) in re.findall(regexp_url, content_string):
                if(urls  not in crawler_backlog or crawler_backlog[urls] != 1):
                    crawler_backlog[urls] = 0
                    visit_url(urls, domain)
    except URLError as e:
        print("error")
    PathWrite = os.getcwd() + "/url_data.pickle"
    WriteToFile = open(PathWrite, "wb")
    pickle.dump(MainList,WriteToFile)
    #print ("Main list========================",MainList)
    

def web_crawler():
    global crawler_backlog
    crawler_backlog = {}
    global MainList
    MainList = []
    seed = "http://www.newhaven.edu/"
    crawler_backlog[seed]=0
    visit_url(seed, "www.newhaven.edu")

#web_crawler()
