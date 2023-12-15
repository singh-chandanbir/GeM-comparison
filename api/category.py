import requests
from bs4 import BeautifulSoup as BS



def getCategory(search_query):

    search_query.replace(" ", "%20")

    url = "https://mkp.gem.gov.in/search?q="+search_query

    response = requests.get(url)
    
    category_dict = {}  # Initialize an empty dictionary to store categories and subcategories

    if response.status_code == 200:
        htmlcontent = response.text
        htmlsoup = BS(htmlcontent, 'html.parser') 
        relevant_categories_parent = htmlsoup.find('ul', class_="clearfix")
        
        relevant_categories = relevant_categories_parent.find_all('li', class_="bn-group")
        
        for cat in relevant_categories:
            category_name = cat.find('strong').text
            subcategories = [tag.text for tag in cat.find_all('li')]
            category_dict[category_name] = subcategories

    return category_dict