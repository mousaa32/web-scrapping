import urllib
import urllib.request
from bs4 import BeautifulSoup
import os

def table(url): 
    thepage=urllib.request.urlopen(url)
    soup=BeautifulSoup(thepage,"html.parser")
    return soup
 
# soup=table("https://www.marmiton.org/recettes/")
# page1=soup.findAll('h4',{'class':'recipe-card__title'})
# tab=[]
# for i in page1:
#     tab.append(i.text)
# print(tab)
 
link=['recette_brochettes-de-canard-aux-peches_30507.aspx','recette_clafoutis-aux-abricots-et-aux-amandes_71156.aspx']
 
for li in link: 
    soup=table("https://www.marmiton.org/recettes/"+ li +" ")
    nom_de_la_recette=soup.find('h1').text
    print(nom_de_la_recette)

    nombre_de_personnes=soup.find('span',{'class':'title-2 recipe-infos__quantity__value'}).text
    print(nombre_de_personnes)

    durée_de_préparation=soup.find('span',{'class':'recipe-infos__timmings__value'}).text.strip()
    print(durée_de_préparation)

    durée=soup.find('div',{'class':'recipe-infos__timmings__cooking'})
    durée_de_cuisson=durée.find('span',{'class':'recipe-infos__timmings__value'}).text.strip()
    print(durée_de_cuisson)

    liste_des_ustensiles=""
    for i in soup.findAll('span',{'class':'recipe-utensil__name'}):
        liste_des_ustensiles=liste_des_ustensiles+i.text.strip() +'\n'
    print(liste_des_ustensiles)

    liste_des_ingrédients=""
    # print(soup.find('ul',{'class':'recipe-ingredients__list'}).text)
    for i in soup.findAll('ul',{'class':'recipe-ingredients__list'}):
        print(i.text+'\n')
    #    liste_des_ingrédients= i.find('il').text
    # print(liste_des_ingrédients)

    étapes_de_préparations=soup.findAll('')

# étapes_de_préparations

