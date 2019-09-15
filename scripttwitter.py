import urllib
import urllib.request
from bs4 import BeautifulSoup

theurl="https://twitter.com/Macky_Sall"
print(theurl)
thepage=urllib.request.urlopen(theurl)
soup=BeautifulSoup(thepage,"html.parser")
# print(soup.prettify())

# liste=soup.findAll('a')
# print((liste[0]))
liste1=soup.find('a').prettify()

# print((liste1))
# print(soup.title.text)
# for link in soup.findAll('a'):
#     # print(link.get('href'))
#     print(link.text)

# c=""
# a=soup.findAll('div',{"class":"content"})
# for e in a:
#     if e !=None:
#         # print(e)
#         b=e.find('span').text
#         c=c+b
# print(c)   


i=1
for tweets in soup.findAll('div',{"class":"content"}):
    print(i)
    print(tweets.find('p').text)
    i+=1
# ab=soup.findAll('a')
# print(ab.find('span'))