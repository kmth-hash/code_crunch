import requests 
from bs4 import BeautifulSoup 

class Pokemon:
    def __init__(self , ID , urlLink , name , type) :
        self.name = name 
        self.ID = ID 
        self.urlLink = urlLink 
        self.type_ : list = type

    def poke(self):
        print(f' Pokemon {self.ID} : {self.name } --> {self.type_} ')

    def pokeLink(self):
        print(f' {self.name} --> {self.urlLink}')
        


URL = "https://pokemondb.net/pokedex/game/black-white"
r = requests.get(URL) 

soup = BeautifulSoup(r.content , "html.parser")
# print(soup)
ls = soup.find_all("div" , class_='infocard')

pokemonList = []
for i in ls : 
    tempURL = (i.find('img' , class_='img-sprite')['src'])
    tempID = (i.find('span',class_='infocard-lg-data').small.text)
    tempName = (i.find('span',class_='infocard-lg-data').find('a',class_='ent-name').text)
    tempType = (i.find('span',class_='infocard-lg-data').select('small')[1].find_all('a'))
    tempTypeList = []
    for i in tempType:
        tempTypeList.append(str(i).split('>')[1].split('<')[0])
    # print(tempID , tempName , tempURL ,tempTypeList)
    p1 = Pokemon(tempID , tempURL , tempName , tempTypeList)
    pokemonList.append(p1)

for i in pokemonList : 
    i.poke()
# print(ls)