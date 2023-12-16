import requests
from bs4 import BeautifulSoup as BS
from api.gemPages import getPages

def fetch_page_content(url):
    response = requests.get(url)
    return response.text if response.status_code == 200 else None

def get_product_details(product):
    details_dict = {}
    details_dict['product_title'] = product.find('span', class_='variant-title').text if product.find('span', class_='variant-title') else ''
    details_dict['product_brand'] = product.find('div', class_='variant-brand').text.replace('Brand:', '') if product.find('div', class_='variant-brand') else ''
    details_dict['product_min_qty'] = product.find('div', class_='variant-moq').text.replace('Min. Qty. Per Consignee:', '') if product.find('div', class_='variant-moq') else ''
    details_dict['product_final_price'] = product.find('span', class_='variant-list-price').text if product.find('span', class_='variant-list-price') else ''
    details_dict['product_list_price'] = product.find('span', class_='variant-final-price').text if product.find('span', class_='variant-final-price') else ''
    return details_dict

def get_products(query):
    product_detail_list = []
    product_pages = getPages(query)
    
    for link in product_pages:
        base_url = f"https://mkp.gem.gov.in{link}&page="
        page_number = 1
        highest_page_number = 1
        initial_url = f"https://mkp.gem.gov.in{link}"
        initial_content = fetch_page_content(initial_url)
        
        initial_soup = BS(initial_content, 'html.parser')
        pagination_div = initial_soup.find('div', class_='pagination')
        if pagination_div:
            page_links = pagination_div.find_all('a')
            page_numbers = [int(link['href'].split('=')[-1]) for link in page_links]
            highest_page_number = max(page_numbers)
                
        while (page_number <= highest_page_number):
            url = f"https://mkp.gem.gov.in{link}&page={page_number}"
            content = fetch_page_content(url)
            html_soup = BS(content, 'html.parser') if content else None
            if html_soup.find('div', id='no-results-found'):
                break
            
            product_list = html_soup.find_all('li', class_="clearfix")
            for product in product_list:
                details_dict = get_product_details(product)
                product_detail_list.append(details_dict)
            
            page_number += 1
    
    return product_detail_list
