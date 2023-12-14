import requests
from bs4 import BeautifulSoup as BS



def getCategory(search_query):

    search_query.replace(" ", "%20")

    url = "https://mkp.gem.gov.in/search?q="+search_query

    response = requests.get(url)
    category = []
    subcategory = []
    if response.status_code == 200:
        htmlcontent = response.text
        htmlsoup = BS(htmlcontent, 'html.parser') 
        relevant_categories_parent = htmlsoup.find('ul', class_="clearfix")
        # print(relevant_categories)
        counter = 0
        relevant_categories = relevant_categories_parent.find_all('li', class_ = "bn-group")
        for cat in relevant_categories:
            category.append(cat.find('strong').text) 
            subcategory.append([tag.text for tag in cat.find_all('li')])
        
        return (category,subcategory)
