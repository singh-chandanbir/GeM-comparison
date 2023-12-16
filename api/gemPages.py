import requests
from bs4 import BeautifulSoup as BS

def getPages(search_query):

    search_query.replace(" ", "%20")

    url = "https://mkp.gem.gov.in/search?q="+search_query

    response = requests.get(url)
    
    productPages = []
    
    if response.status_code == 200:
        htmlcontent = response.text
        htmlsoup = BS(htmlcontent, 'html.parser') 
        link_tags = htmlsoup.find_all('li', class_="bn-link")
        
        for link in link_tags:
            href = link.a['href']
            productPages.append(href)
            
        return productPages