from selenium import webdriver
driver = webdriver.Chrome(executable_path='/home/moussa/Téléchargements/chromedriver_linux64/chromedriver')
driver.get("https://fr-fr.facebook.com/")

print(driver.title)
print(driver.current_url)
