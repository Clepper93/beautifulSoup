import requests
import random
import re
import urllib.request
from bs4 import BeautifulSoup as bs4
yearlist = ['2018','2017','2016','2015','2014','2013','2012']
monthlist=['01','02','03','04','05','06','07','08','09','10','11','12']
daylist=['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31']
def makeurl():
    urlday = random.choice(daylist)
    urlmonth = random.choice(monthlist)
    urlyear = random.choice(yearlist)
    url = "http://theworstthingsforsale.com"+ '/' + urlyear + '/' + urlmonth + '/' + urlday + '/'
    try:
        urllib.request.urlopen(url).getcode()
        worstreq = requests.get(url)
        worstsoup = bs4(worstreq.text, 'html5lib')
        geth2 = worstsoup.select('h2')
        getp = worstsoup.select('p')
        ban1 = re.search(r'.*sex.* | \bbutt.* | \bass\b | .*fuck.* | \bpenis.* | .*dick.* | \bgenital.* | \bboob.* | \banus\b | .*flesh.* | \bvagina.*',getp[2].getText().lower())
        ban2 = re.search(r'.*sex.* | \bbutt.* | \bass\b | .*fuck.* | \bpenis.* | .*dick.* | \bgenital.* | \bboob.* | \banus\b | .*flesh.* | \bvagina.*',geth2[1].getText().lower())
        if ban1 or ban2:
            print("NSFW product listing generated. Oops! Trying again...")
            makeurl()
        else:
            print(url)
            print(geth2[1].getText())
            print(getp[2].getText())
    except:
        print("Invalid URL generated. Oops! Trying again...")
        makeurl()
    
makeurl()
def do_over():
    y=input("\nGenerate another terrible product? \n")
    y=y.lower()
    if y == 'y' or y == 'yes':
        makeurl()
        do_over()
    else:
        print('bye')
do_over()
