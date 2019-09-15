import urllib
import urllib.request
from bs4 import BeautifulSoup
import os
def table(url): 
    thepage=urllib.request.urlopen(url)
    soup=BeautifulSoup(thepage,"html.parser")
    return soup

soup=table("https://www.amazon.fr/") 
i=1
a="amazon"
for img in soup.findAll('img'):
    temp=img.get('src')
    # print(temp)
    if temp==None:
        temp="https://images-eu.ssl-images-amazon.com/images/I/71+IZZprWML._AC_SY200_.jpg"
        image=temp
        # print(image)
    else:
        image=temp
    # print(image) 
    # print(temp)   
    #
    nametemp=img.get('alt')
    if nametemp==None:
        nametemp=a 
    print(nametemp)
    if len(nametemp)==0:
        filename=str(i)
        i+=1

    else:
        filename=nametemp 
           
    imagefile=open(filename+".jpeg","wb")
    imagefile.write(urllib.request.urlopen(image).read())
    imagefile.close()
