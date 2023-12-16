import requests
from bs4 import BeautifulSoup as BS
from api.gemPages import getPages

def getProducts(query):
    productPages = getPages(query)
    
    completeList = []
    
    for link in productPages:
        url = "https://mkp.gem.gov.in" + link
        response = requests.get(url)
        if response.status_code == 200:
            htmlsoup = BS(response.text, 'html.parser')
            if htmlsoup.find('div', id='no-results-found'):
                continue
            else:
                productlist = htmlsoup.find_all('li', class_="clearfix")
                completeList.append(productlist)
        
    return completeList
