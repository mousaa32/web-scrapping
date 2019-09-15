import urllib
import urllib.request
from bs4 import BeautifulSoup
import os
from string import ascii_lowercase,digits
print(digits)
def table(url): 
    thepage=urllib.request.urlopen(url)
    soup=BeautifulSoup(thepage,"html.parser")
    return soup
tab1=[]  
print(ascii_lowercase) 
for letter in ascii_lowercase[0:2]:
    url="https://www.basketball-reference.com/players/"+ letter + "/"
    # tab1.append(letter)
    print(url) 
#     soup=table("https://www.basketball-reference.com/players/"+ letter + "/") 
   

    print(letter)
    print(soup.find('title').text)
     

    tab=[]
    playersave=""

    for nom in soup.findAll('tr'):
        players=""
        name=""
        
        # print(nom.find('td'))
        for data in nom.findAll('td'):
            # print(data.text)
            players=players+";"+data.text
        play=players[1:]
        # print(play)
        for data in nom.findAll('th'):
            name=name+";"+data.text
        print(name)
        name1=name[1:]
        # print(name1)

        somme=name1+";"+play
        print(somme) 
        if len(playersave) !=None:
            playersave=playersave+somme+"\n"
           
# print(playersave)
# header="Player;From;To;Pos;Ht;Wt;Birth Date;Colleges"+"\n"
file=open(os.path.expanduser("tablebasket.csv"),"wb")
# file.write(bytes(header,encoding='ascii',errors='ignore'))
file.write(bytes(playersave,encoding='ascii',errors='ignore'))
    
    
     
    