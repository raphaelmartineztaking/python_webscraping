from bs4 import BeautifulSoup
import requests

# fazer url input do usuário
#append no arquivo

def salva_dados(info):
    with open (f'{biografia}.txt', 'w') as file :
        file.write(f'{info}')

def request(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text,'html.parser')
    return soup

def get_info(soup):
    #print((soup.title.get_text()))
    info = soup.find('table', {'class': 'infobox infobox_v2'}).text
    return info

def main ():
    global biografia
    biografia = 'Elon_Musk'
    url = f'https://pt.wikipedia.org/wiki/{biografia}'
    #get_info(request(url))
    salva_dados(get_info(request(url)))

if __name__ == '__main__':
    main()