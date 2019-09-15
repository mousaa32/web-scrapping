from flask import Flask,render_template,request,redirect,url_for
import urllib
import urllib.request
from bs4 import BeautifulSoup
import os
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')

app = Flask(__name__)
app.secret_key="flash message"

@app.route('/')
def expatcoinAfrique(): 
    grand=[]
#**********************************************coin-afrique**********************************************#
    def table(url): 
        thepage=urllib.request.urlopen(url)
        soup=BeautifulSoup(thepage,"html.parser")
        return soup
    tab=[]
    tabprix=[]
    tabimages=[]
    tabsources=[]
    tablocation=[]
    tablieu=[]
    tab3=[]
    playersave=""
    playersave1=""
    for link in range(0,10):
        tabimag=[]
        tabsource=[]
        tabp=[]
        tablo=[]
        tabli=[]
        
        soup=table("https://sn.coinafrique.com/categorie/appartements/51?page="+str(link)+"")
    
        div=soup.find('div',{'class':'column four-fifth'})
        prix=div.findAll('p',{'class':'card-title activator orange-text'})
        for i in prix:
            tabp.append(i.text)
        tabprix.append(tabp)
        location=div.findAll('p',{'class':'card-desc'})
        for i in location:
            tablo.append(i.text.replace('\xa0',''))
        tablocation.append(tablo)
        lieu=div.findAll('p',{'class':'card-location'})
        for i in lieu:
            tabli.append(i.text.replace(' location_on\xa0\xa0','').replace(", Dakar","").replace("'","").replace(" ","").replace("-",""))
        tablieu.append(tabli) 

        
        imgexp=soup.findAll('div',{'class':'card-image waves-effect waves-block waves-light'})
        # print(imgexp)
        for i in imgexp:
            http="https://sn.coinafrique.com"
            tabimag.append(i.find('img').get('src'))
            a=http+i.find('a').get('href')
            tabsource.append(a)
        tabsources.append(tabsource)
        tabimages.append(tabimag)
    # print(tabimages)
    # print(tabsources)
    for i,j,k,l,m in zip(tablocation[0],tabprix[0],tablieu[0],tabsources[0],tabimages[0]): 
        dic = {'location':i,'prix':j, 'lieu':k,'source':l,'image':m}
        grand.append(dic)
    for i,j,k,l,m in zip(tablocation[1],tabprix[1],tablieu[1],tabsources[1],tabimages[1]): 
        dic = {'location':i,'prix':j,'lieu':k,'source':l,'image':m}
        grand.append(dic)
    for i,j,k,l,m in zip(tablocation[2],tabprix[2],tablieu[2],tabsources[2],tabimages[2]): 
        dic = {'location':i,'prix':j,'lieu':k,'source':l,'image':m}
        grand.append(dic) 
    for i,j,k,l,m in zip(tablocation[3],tabprix[3],tablieu[3],tabsources[3],tabimages[3]): 
        dic = {'location':i,'prix':j,'lieu':k,'source':l,'image':m}
        grand.append(dic)   
    for i,j,k,l,m in zip(tablocation[4],tabprix[4],tablieu[4],tabsources[4],tabimages[4]): 
        dic = {'location':i,'prix':j,'lieu':k,'source':l,'image':m}
        grand.append(dic)
    for i,j,k,l,m in zip(tablocation[5],tabprix[5],tablieu[5],tabsources[5],tabimages[5]): 
        dic = {'location':i,'prix':j,'lieu':k,'source':l,'image':m}
        grand.append(dic)  
    for i,j,k,l,m in zip(tablocation[6],tabprix[6],tablieu[6],tabsources[6],tabimages[6]): 
        dic = {'location':i,'prix':j,'lieu':k,'source':l,'image':m}
        grand.append(dic) 
    for i,j,k,l,m in zip(tablocation[7],tabprix[7],tablieu[7],tabsources[7],tabimages[7]): 
        dic = {'location':i,'prix':j,'lieu':k,'source':l,'image':m}
        grand.append(dic) 
    for i,j,k,l,m in zip(tablocation[8],tabprix[8],tablieu[8],tabsources[8],tabimages[8]): 
        dic = {'location':i,'prix':j,'lieu':k,'source':l,'image':m}
        grand.append(dic) 
    for i,j,k,l,m in zip(tablocation[9],tabprix[9],tablieu[9],tabsources[9],tabimages[9]): 
        dic = {'location':i,'prix':j,'lieu':k,'source':l,'image':m}
        grand.append(dic)                                      
    # playersave2=playersave+playersave1
    # print(playersave2) 

    # # header="location;prix;lieu"+"\n"
    # # file=open(os.path.expanduser("coinafri.csv"),"wb")
    # # file.write(bytes(header,encoding='ascii',errors='ignore'))
    # # file.write(bytes(playersave2,encoding='ascii',errors='ignore'))


    #**********************************************expat-dakar**********************************************#
    def table1(url): 
        thepage=urllib.request.urlopen(url)
        soup1=BeautifulSoup(thepage,"html.parser")
        return soup1   
    prixexpt=[]
    locationexpat=[]
    lieuexpat=[]
    playersave=""
    playersave1=""
    tabimages=[]
    tabsources=[]
   
    for link in range(0,10):    
        soup1=table1("https://www.expat-dakar.com/appartements-a-louer?type=1&page="+str(link)+"")
        tabp=[]
        tablo=[]
        tabli=[]
        tabimag=[]
        tabsource=[]
        
        nomexpt=soup1.findAll('div',{'class':'listing-details-row'})
        for i in nomexpt:
            tablo.append(i.find('h2').text.strip()+i.find('span').text.strip().replace('Nombre de chambres',' Nombre de chambres'))
        locationexpat.append(tablo)
        for i in nomexpt:
            tabli.append(i.find('span',{'class':'picto picto-place ed-icon-before icon-location'}).text.replace("-","").replace(" ","").replace("-",""))
        lieuexpat.append(tabli)
        for i in nomexpt:
            tabp.append(i.find('span',{'class':'prix'}).text.replace('\n\t\t\t\t\t\t\t\t\t\t','').replace('\t\t\t\t\t\t\t\t\t','').replace('\xa0',' '))
        prixexpt.append(tabp)

        imgexp=soup1.findAll('div',{'class':'listing-card-inner'})
        # print(imgexp)
        for i in imgexp:
            v=i.find('a')
            if v !=None:
                http="https://www.expat-dakar.com"
                a=http+v.get('href')
                tabsource.append(a)
            tabsources.append(tabsource)
        for i in imgexp:    
            try:
                http = "https://www.expat-dakar.com"
                image = i.a.find('img')['data-src']
                # print(image)
                product_image = http + image
                tabimag.append(product_image)
            
            
            except Exception:   
               continue 
            tabimages.append(tabimag)     
        # tabimages.append("https://www.expat-dakar.com")
    # print(len(tabimages[0]))
    # print(len(tabsources[0]) )                     
    for i,j,k,l,m in zip(locationexpat[0],prixexpt[0],lieuexpat[0],tabsources[0],tabimages[0]): 
        playersave1=playersave1+i+";"+j+";"+k+";"+l+";"+m+"\n"
        dic = {'location':i,'prix':j,'lieu':k,'source':l,'image':m}
        grand.append(dic)
    for i,j,k,l,m in zip(locationexpat[1],prixexpt[1],lieuexpat[1],tabsources[1],tabimages[1]): 
        playersave1=playersave1+i+";"+j+";"+k+";"+l+";"+m+"\n"
        dic = {'location':i,'prix':j,'lieu':k,'source':l,'image':m}
        grand.append(dic)
    for i,j,k,l,m in zip(locationexpat[2],prixexpt[2],lieuexpat[2],tabsources[2],tabimages[2]): 
        playersave1=playersave1+i+";"+j+";"+k+";"+l+";"+m+"\n"
        dic = {'location':i,'prix':j,'lieu':k,'source':l,'image':m}
        grand.append(dic)
    for i,j,k,l,m in zip(locationexpat[3],prixexpt[3],lieuexpat[3],tabsources[3],tabimages[3]): 
        dic = {'location':i,'prix':j,'lieu':k,'source':l,'image':m}
        grand.append(dic)
    for i,j,k,l,m in zip(locationexpat[4],prixexpt[4],lieuexpat[4],tabsources[4],tabimages[4]): 
        dic = {'location':i,'prix':j,'lieu':k,'source':l,'image':m}
        grand.append(dic)
    for i,j,k,l,m in zip(locationexpat[5],prixexpt[5],lieuexpat[5],tabsources[5],tabimages[5]): 
        dic = {'location':i,'prix':j,'lieu':k,'source':l,'image':m}
        grand.append(dic)
    for i,j,k,l,m in zip(locationexpat[6],prixexpt[6],lieuexpat[6],tabsources[6],tabimages[6]): 
        dic = {'location':i,'prix':j,'lieu':k,'source':l,'image':m}
        grand.append(dic)
    for i,j,k,l,m in zip(locationexpat[7],prixexpt[7],lieuexpat[7],tabsources[7],tabimages[7]): 
        dic = {'location':i,'prix':j,'lieu':k,'source':l,'image':m}
        grand.append(dic)   
    for i,j,k,l,m in zip(locationexpat[8],prixexpt[8],lieuexpat[8],tabsources[8],tabimages[8]): 
        dic = {'location':i,'prix':j,'lieu':k,'source':l,'image':m}
        grand.append(dic)
    for i,j,k,l,m in zip(locationexpat[9],prixexpt[9],lieuexpat[9],tabsources[9],tabimages[9]): 
        dic = {'location':i,'prix':j,'lieu':k,'source':l,'image':m}
        grand.append(dic)
      
 

    df = pd.DataFrame(data=grand) 
    prix=df['prix']
    labels=df['location']
    lieu=df['lieu']
    fntion=df.groupby('lieu')['location'].count()
    prixn=df.groupby('location')['prix'].count()
    indexe=fntion.index.tolist()
    # print(fntion.nlargest('15'))
    nombre=[]
    for i in fntion:
        nombre.append(i)
        # print(i) 
    # print(prixn)
    # for i in prixn:
    #     print(i) 
    # print("Statistical Summary\n",df.describe())
     
    outfile=open("/home/moussa/Documents/PROJET/projethtml/web&scrapping/expat-coinafriq.json",'w+')
    rows=json.dumps(grand,indent=2)
    outfile.write(rows)
    return render_template('test1.html',grand=grand,indexe=indexe,nombre=nombre)

if __name__ == '__main__':
    app.run(debug=True)

    
    