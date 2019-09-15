import urllib
import urllib.request
from bs4 import BeautifulSoup
import os
from string import digits
print(digits[1:])
def table(url): 
    thepage=urllib.request.urlopen(url)
    soup=BeautifulSoup(thepage,"html.parser")
    return soup
tab1=[]  
for number in digits[1:3]:
    soup=table("https://www.expat-dakar.com/voitures?page="+ number + "/") 
    print(number) 
    # print(soup.find('title').text)
    noms=""

    h2=soup.findAll('h2')
    for nom in h2:
        noms=nom.text
    #     noms=noms+";"+nom.text
    # # print(' '.join(noms[1:].split())+"\n")
    # no=noms[1:]
        print(noms)