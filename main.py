import requests
from bs4 import BeautifulSoup
from selenium import webdriver

from selenium.webdriver.common.by import By

url ='https://www.djbuzz.com/mycharts/index.asp'

response = requests.get(url)
# récuperer le code html de la page
#on vas le passer dans la fonction Beautifulsoup
if response.ok:
    #print(response.text)
    #ne pas oublier de le parser en 2nd argument
    soup = BeautifulSoup(response.text,"html.parser")

    #je recupère un tableau
    alltitle = soup.findAll(class_="title")

    spotify = webdriver.Chrome(executable_path="chromedriver.exe")

    for title in alltitle:
        print(title.text)
        spotify.get("https://open.spotify.com/search/"+str(title.text)).send_keys(Keys.COMMAND + 't')


















