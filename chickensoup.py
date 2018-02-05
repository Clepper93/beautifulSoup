from bs4 import BeautifulSoup as bs4
import requests

chixreq = requests.get('http://ansi.okstate.edu/breeds/poultry/chickens/chickens.html')
chickensoup = bs4(chixreq.text, 'html5lib')

chickenbreeds = chickensoup.select('p a')

linklist = []

def gethref():
    i = 0
    for link in chickenbreeds:
        linklist.append(chickenbreeds[i].get('href'))
        i += 1

desclist = []

def getdesc():
    i = 0
    for link in chickenbreeds:
        while i < 73:
            url = linklist[i]
            breedreq = requests.get(url)
            breedsoup = bs4(breedreq.text, 'html5lib')
            breedP = breedsoup.select('p')
            desclist.append(breedP[3].getText())
            i += 1
namelist = []

def getnames():
    i = 0
    chickennames = chickensoup.select('p a')
    for name in chickennames:
        while i < 73:
            namelist.append(chickennames[i].getText())
            i += 1

gethref()
getdesc()
getnames()

chicktionary = dict((key, value) for (key, value) in zip(namelist, desclist))
print(chicktionary)
