import requests
import urllib.request
from bs4 import BeautifulSoup
import csv
import os
import psycopg2

# with open('/home/cire/Documents/scraping/resultats/trucks4.csv', 'a') as csv_file:
#         csv_writer = csv.writer(csv_file)
#         headers = "voitures, prix"+ "\n"
#         csv_writer.writerow(headers)
tabtoal=[]
tabprix=[]
for page in range(1,3):#ça va afficher la page 1 et 2 seulement prck le 3 est exclu
    url = "https://www.skillter.com/fr/annonces/voitures/ford/?page="

    response = requests.get(url + str(page))

    soupe = BeautifulSoup(response.text, 'html.parser')
    data = soupe.findAll("span", {"class" : "make_mdl"})
    tab = []
    
            
    for i in data:
        tab.append(i.text)
    tabtoal.append(tab)
    # print(tabtoal)
    data1 = soupe.findAll("span", {"class" : "new-price"})
    tab1 = []
    for j in data1:
        tab1.append(j.text)
    tabprix.append(tab1)   
    
        
antiquaire1 = ""
antiquaire2 = ""
antiquaire = ""
#pour la  1ere page trouvee
for i,j in zip(tabtoal[0], tabprix[0]):
    antiquaire1 = antiquaire1+i+","+j+'\n'
#pour la  2eme page trouvee 
for i,j in zip(tabtoal[1], tabprix[1]):
    antiquaire2 = antiquaire2+i+","+j+'\n' 

#a chaque fois que tu ajoute le range ,il faut reparcourir a nouveau c comme le precedent tu va ajouter par exemple puis l'ajpouter a la variable antiquere:
                   
                    # antiquaire3 = ""
                    # for i,j in zip(tabtoal[2], tabprix[2]):
                    #     antiquaire3 = antiquaire3+i+","+j+'\n'


#pour la somme des  pages  obtenues   
antiquaire=antiquaire1+antiquaire2  

header = "voitures, prix"+ "\n"
file = open(os.path.expanduser('khadim.csv'), 'wb')
file.write(bytes(header, encoding="utf-8", errors = 'ignore'))
file.write(bytes(antiquaire, encoding="utf-8", errors='ignore'))
 
             
    