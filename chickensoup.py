from bs4 import BeautifulSoup as bs4
import requests

chixreq = requests.get('http://ansi.okstate.edu/breeds/poultry/chickens/chickens.html')
chickensoup = bs4(chixreq.text, 'html5lib')

chickenbreeds = chickensoup.select('p a')

linklist = []

e = 0
for link in chickenbreeds:
    linklist.append(chickenbreeds[e].get('href'))
    e += 1

i = 0
for link in chickenbreeds:
    while i < 73:
        url = linklist[i]
        breedreq = requests.get(url)
        breedsoup = bs4(breedreq.text, 'html5lib')
        breedP = breedsoup.select('p')
        breedTitle = breedsoup.select('title')
        print(breedTitle[0].getText(),breedP[3].getText())
        i += 1
