import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "https://www.exportersindia.com/search.php?srch_catg_ty=prod&term=kids&cont=IN&ss_status=N"

# Fetch the HTML content from the URL
details_dict = []
response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    # Find all <script> tags
    script_tags = soup.find_all("div", class_='class_box_sec')
    # Iterate through each script tag to find the desired data
    for i, script in enumerate(script_tags):
        title = script.find('a', class_='prdclk').text if script.find('a', class_='prdclk') else "No Title"
        price = script.find('span', class_='black fw6 large').text if script.find('span', class_='black fw6 large') else "Contact"
        brand = script.find('a', class_='blue fw6 com_nam').text if script.find('a', class_='blue fw6 com_nam') else "No Brand"
        data = {"index": i, "title": title, "price": price, "brand": brand}
        details_dict.append(data)        
else:
    print("Failed to fetch content from the URL")

for data in details_dict:
    print(f"Index: {data['index']}")
    print(f"Title: {data['title']}")
    print(f"Price: {data['price']}")
    print(f"Brand: {data['brand']}")
    print("________________________\n")

