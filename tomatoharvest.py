from bs4 import BeautifulSoup as bs4
import requests
import re

def tomatoharvest():
        pages = ['1','2']
        for page in pages:
                url = 'https://www.seedsavers.org/category/tomato?page=' + page + '&show=48'
                tomatoreq = requests.get(url)
                tomatosoup = bs4(tomatoreq.text, "html5lib")
                tomatospan = tomatosoup.select('span')
                harvestlist = []
                i = 0
                for item in tomatospan:
                        harvestlist.append(tomatospan[i].getText())
                        i += 1
                for item in harvestlist:
                        if "Tomato" in item:
                                print(item.replace("Tomato, ", ""))
                                

tomatoharvest()
