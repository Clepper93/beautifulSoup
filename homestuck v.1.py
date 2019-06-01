from bs4 import BeautifulSoup as bs4
import requests
import re
import random
def homestuckget():
        def getpage():
                page = random.randint(1,8128)
                url = 'https://www.homestuck.com/story/' + str(page)
                hsreq = requests.get(url)
                hsSoup = bs4(hsreq.text, 'lxml')
                hsText = hsSoup.find('p',attrs={'class':'o-story_text'})
                hsChat = hsSoup.find('p',attrs={'class':'o_chat-log'})
                print(url)
                if hsText == None and hsChat == None:
                        print('no words :(')
                        getpage()
                elif hsText == None and hsChat != None:
                        print(hsChat.text)
                elif hsText!= None and hsChat == None:
                        print(hsText.text)
                else:
                        print('not sure what just happened?')
                        getpage()
        getpage()
#homestuckget()
def getword():
        #word = str(input('Search for word:\n'))
        count = 0
        i = 1
        while i < 150:
                url ='https://www.homestuck.com/story/' + str(i)
                print(url)
                hsreq = requests.get(url)
                hsSoup = bs4(hsreq.text, 'lxml')
                hsText = hsSoup.find('p',attrs={'class':'o-story_text'})
                hsChat = hsSoup.find('p',attrs={'class':'o_chat-log'})
                if hsText == None and hsChat == None:
                        i +=1
                elif hsText == None and hsChat != None:
                        count += 1
                        i +=1
                elif hsText!= None and hsChat == None:
                        count +=1
                        i +=1
                else:
                        i +=1
        print(count)
        print(i)
getword()
