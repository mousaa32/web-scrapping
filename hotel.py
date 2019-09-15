import urllib
import urllib.request
from bs4 import BeautifulSoup
import os
def table(url): 
    thepage=urllib.request.urlopen(url)
    soup=BeautifulSoup(thepage,"html.parser")
    return soup

soup=table("https://www.booking.com/searchresults.fr.html?aid=318615;label=New_French_FR_5226376105-GcX90m7DFHULc6Lk63FTkQS73336353265%3Apl%3Ata%3Ap1%3Ap2%3Aac%3Aap1t2%3Aneg;sid=666328e74175f123400b6019ddd529a4;city=-2266494&") 
# print(soup.prettify())

nom_hotel=""
des_hotel=""
somme=""
 
for i in soup.findAll('span',{'class':'sr-hotel__name'}):
    nom_hotel=nom_hotel+";"+i.text
nom_hotels=nom_hotel[1:]    
# print(nom_hotels) 
for i in soup.findAll('div',{'class':'hotel_desc'}):  
    des_hotel=des_hotel+";"+i.text
des_hotels=des_hotel[1:]    
# print(des_hotels)
somme=somme+nom_hotels+des_hotels 
# print(somme[1:])
# for j,k in zip(nom_hotels,des_hotels):
#     print(nom_hotels)
#     print(des_hotels)
print(somme)    

