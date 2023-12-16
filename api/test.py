import requests
from bs4 import BeautifulSoup

def result(query):
    result = []
    query.replace(" ", "%20")
    url = "https://mkp.gem.gov.in/search?q="
    
    search_query = url+query
    
    content = requests.get(search_query)
    html_content = content.text
    
    soup = BeautifulSoup(html_content, 'html.parser')
    links = soup.find_all('li', class_='bn-link')
    
    for link in links:
        href = link.a['href']
        result.append(href)
        
    return result

query = input("Enter the search query: ")

links = result(query)
for link in links:
    print(link)