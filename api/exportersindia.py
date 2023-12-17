import requests
import pandas as pd
from bs4 import BeautifulSoup

def exporters_products(query):
    query.replace(" ", "%20")
    url = f"https://www.exportersindia.com/search.php?srch_catg_ty=prod&term={query}&cont=IN&ss_status=N"

    # Fetch the HTML content from the URL
    details_list = []
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        # Find all <script> tags
        script_tags = soup.find_all("div", class_='class_box_sec')
        # Iterate through each script tag to find the desired data
        for i, script in enumerate(script_tags):
            title_element = script.find('a', class_='prdclk')
            title = title_element.text.strip() if title_element else "No Title"
            
            price_element = script.find('span', class_='black fw6 large')
            price = price_element.text.strip() if price_element else "Contact"
            
            brand_element = script.find('a', class_='blue fw6 com_nam')
            brand = brand_element.text.strip() if brand_element else "No Brand"
            
            image_element = script.find('img', class_='utmlazy')
            image_url = image_element['src'] if image_element else "No Image URL"
            
            # product_link = title_element['href']
            
            if price != "Contact":
                data = {"index": i, "title": title, "price": price, "brand": brand, "image_link":image_url}
                details_dict.append(data) 
            
            return details_list
            
    else:
        print("Failed to fetch content from the URL")
        
query = input("Enter a search term")
print(exporters_products(query))
