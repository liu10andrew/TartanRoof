from bs4 import BeautifulSoup
import sys
import urllib2

def URLtoTitle(url):
    if url == '':
        return ''
    else:
        response = soup = None
        assert(url.startswith("http"))
        try:
            response = urllib2.urlopen(url)
            page_source = response.read()
            soup = BeautifulSoup(page_source)
        finally:
            if (response != None): 
                response.close()
        if (soup.title == None):
            return ''
        else:
            return soup.title.string

def readFile(filename, mode="rt"):
    # rt stands for "read text"
    fin = contents = None
    try:
        fin = open(filename, mode)
        contents = fin.read()
    finally:
        if (fin != None): fin.close()
    return contents

def removeSource(raw_text):
    data_arr = raw_text.split()
    len_d = len(data_arr)
    if (len_d > 1):
        return data_arr[1]
    elif (len_d == 0):
        return ''
    else:
        return ''

def raw_to_tuple(raw_text):
    scores = []
    titles = []
    for line in raw_text:
        data_arr = line.split()
        if (len(data_arr) > 1):
            scores.append(data_arr[0])
            titles.append(data_arr[1])
    return (scores, titles)

def writeFile(filename, contents, mode="wt"):
    # wt stands for "write text"
    fout = None
    try:
        fout = open(filename, mode)
        fout.write(contents)
    finally:
        if (fout != None): fout.close()
    return True

def getTitles(textfile):
    raw_file = readFile(textfile).split('\n')
    (scores, URL_list) = (raw_to_tuple(raw_file))
    result = filter(None, map(URLtoTitle, URL_list))
    writeFile('titles.txt',unicode(result))
    return (scores,result)

#print getTitles(sys.argv[1])
