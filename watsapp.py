from selenium import webdriver 
# from webdriver_manager.chrome import ChromeDriverManager

import urllib
import urllib.request
from bs4 import BeautifulSoup

driver= webdriver.Chrome('/home/moussa/Téléchargements/chromedriver_linux64/chromedriver')

# driver = webdriver.Chrome(ChromeDriverManager().install())
# driver.get('https://web.whatsapp.com/')

theurl='https://web.whatsapp.com/'
driver.get(theurl)
# print(theurl)
thepage=urllib.request.urlopen(theurl)
# print(thepage)
soup=BeautifulSoup(thepage,"html.parser")

# print(soup.prettify())

name = input('Enter the name of user or group : ')
input('enter anathing after scanning  QR code')

user = driver.find_element_by_xpath("//span[@title = '{}']".format(name))
user.click()
# print(user)

# msg = driver.find_element_by_class_name('_1QjgA color-1 _2q8oz')
msg=driver.find_element_by_css_selector('p.content')

print(msg)


# print(soup.findAll('div',{'class':'content'}))
    # for sms in soup.findAll('div',{'class':'FTBzM'}):
    #     print(sms)

 

 