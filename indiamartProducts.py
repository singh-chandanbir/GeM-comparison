import requests
import pandas as pd
import json
from bs4 import BeautifulSoup

url = "https://dir.indiamart.com/search.mp?ss=kids"

# Fetch the HTML content from the URL
response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    # Find all <script> tags
    script_tags = soup.find_all('script')
    subject = " "
    # Iterate through each script tag to find the desired data
    for script in script_tags:
        if ("window.__INITIAL_DATA__" in script.text):
            subject = script.text
            start_index = subject.find('window.__INITIAL_DATA__ =') + len('window.__INITIAL_DATA__ =')
            end_index = subject.find('var glmodid="DIR"')
            subject = subject[start_index:end_index]
            json_text = subject[start_index:end_index]
            data = json.loads(json_text)
            df = pd.DataFrame([data])
            print(df)
else:
    print("Failed to fetch content from the URL")
