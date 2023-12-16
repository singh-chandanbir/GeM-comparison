import requests
from bs4 import BeautifulSoup

url = "https://dir.indiamart.com/search.mp?ss=kids&res=RC5&stype=attr=1|attrS&Mspl=0&qry_typ=P"

# Fetch the HTML content from the URL
response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    # Find all <script> tags
    script_tags = soup.find_all('script')
    
    # Iterate through each script tag to find the desired data
    for script in script_tags:
        if ("window.__INITIAL_DATA__" in script.text):
            print(script)
        
else:
    print("Failed to fetch content from the URL")
