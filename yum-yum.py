from flask import Flask,render_template,request,redirect,url_for
import urllib
import urllib.request
from bs4 import BeautifulSoup
import os  
import json
 


app = Flask(__name__)
app.secret_key="flash message"

@app.route('/')
def yumyum(): 
    def table(url): 
        thepage=urllib.request.urlopen(url)
        soup=BeautifulSoup(thepage,"html.parser")
        return soup

    # pour recuperer tous les menus
    soup=table("https://www.yumyum.sn/menu.html")
    page=soup.findAll('div',{'class':'col-lg-3 col-sm-4 col-xs-6'})
    tab=[]
    
    tab3=[]
    tab6=[]
    tab7=[]
    tab8=[]
    tab9=[]
    tab5=[]
    tabo=[]
    nom_de_la_recette=[]
    par=[]
    playersave=""


    for i in page:
        recette=i.find('h2').text.lower()
        tab3.append(recette)
    # print(tab3)

    #pour recuperer tous les plats avec le menu selectionné
   
   
    for link1 in tab3[0:1]: 
        try:
            # print('type de produit:',link1,"\n--------------------------------------------------------------------------------")
            soup=table("https://www.yumyum.sn/menu/"+ link1 +".html")
            # print(soup.find('title').text)

            page1=soup.findAll('div',{'class':'col-lg-4 col-sm-6 col-xs-12 category-product'})    
            # page1=soup.findAll('h3')
            
            # print(page1)
            for i in page1:
                # print(type(i))
                if i.find('h3') != None: 
                    # print(i.find('h3'))
                    tab.append(i.find('h3').text.replace("ê","e").replace("Pizza","bis").replace("è","e").replace("é","e").replace("î","i").replace("ï","i").replace("'"," ")
                    .replace('.000','').replace('.500','').replace('0','').replace('1','').replace('2','').replace('3','')
                    .replace('4','').replace('6','').replace('7','').replace('8','').replace('9','').replace('Fcfa','').replace(" ","-")
                    .lower().strip())
            # print(tab)
            for link in tab[0:5]: 
                tab4=[]
                tab2=[]
                # print(link)
                soup=table("https://www.yumyum.sn/menu/"+ link1 +"/"+ link +".html")
                # print(soup.find('title').text)
                # ass=soup.findAll('section',{'class':'product'})
                # print(ass.findAll('h1'))
                nom =soup.findAll('h1')
                for i in nom:
                      
                    nom_de_la_recette.append(i.text.replace("Specials","").replace("Pizzas ›","").replace("'',",""))
                    
                # print('------nom_de_la_recette:',nom_de_la_recette[1:])

                par.append(soup.find('p').text.replace('ô','o').replace('œ','oe'))
                # print('-----composition:',par)

                
                
                niveau=soup.findAll('div',{'class':'col-md-7 col-sm-6'})
                # print(niveau)
                for i in niveau:
                    h3=i.findAll('h3')
                    # print(h3)
                    for j in h3:
                        # print(j.text)
                        tab2.append(j.text.replace('.000','').replace('.500','').replace('0','').replace('1','').replace('2','').replace('3','')
                        .replace('4','').replace('5','').replace('6','').replace('7','').replace('8','').replace('9','').replace('Fcfa','').strip())
                span=i.findAll('span')
                for j in span:
                    # print(j.text)
                    a=j.text.replace("Fcfa","").replace(".","").strip()
                    tab4.append(a)
                tab4= list(dict.fromkeys(tab4))
                # print(tab4)
                tabo.append(tab4)
                tab2= list(dict.fromkeys(tab2)) 
                # print('-------niveau_commande:',tab2,"\n",'-------prix:',tab4,"\n-------------------")
        
        except Exception:
            continue  

    
    tab= list(dict.fromkeys(tab))
    print(tabo[0])
    tab5 = [int(x) for x in tabo[0]]
    print(tab5)
    tab6 = [int(x) for x in tabo[1]]
    tab7 = [int(x) for x in tabo[2]] 
    tab8 = [int(x) for x in tabo[3]]
    tab9 = [int(x) for x in tabo[4]]   
    
    # print(nom_de_la_recette)           
    # print(tabo)   
    
    # outfile=open("/home/moussa/Documents/PROJET/projethtml/web&scrapping/test.json",'w+')
    # rows=json.dumps(({'le categorie de menu':tab3},{'les menus par categorie selectionne':tab},{'nom_de_la_recette':nom_rec}
    # ,{'comp':par[1:]}),indent=2)
    # outfile.write(rows)  

    for i,j,k,l in zip(nom_de_la_recette,par,tab2,tabo[2]):
        # print(i,j,k,l,"\n") 
        playersave=playersave+i+";"+j+";"+k+";"+l+"\n"
        # print(playersave[1:])  
    
    header="Player;From;To;Pos;Ht;Wt"+"\n"
    file=open(os.path.expanduser("YUMYUM.csv"),"wb")
    file.write(bytes(header,encoding='ascii',errors='ignore'))
    file.write(bytes(playersave[1:],encoding='ascii',errors='ignore')) 
    
    return render_template('index.html',tab=tab,tab2=tab2,tab3=tab3,tab5=tab5,tab6=tab6,tab7=tab7,tab8=tab8,tab9=tab9,nom_de_la_recette=nom_de_la_recette)
    
     
  
if __name__ == '__main__':
    app.run(debug=True)

        
    
    