import concurrent.futures
import requests
from bs4 import BeautifulSoup as BS
from api.gemPages import getPages

def fetch_page_content(url):
    response = requests.get(url)
    return response.text if response.status_code == 200 else None

def get_product_details(product):
    details_dict = {}
    title = product.find('span', class_='variant-title')
    
    if title:
        details_dict['product_title'] = title.text
        details_dict['product_brand'] = product.find('div', class_='variant-brand').text.replace('Brand:', '') if product.find('div', class_='variant-brand') else ''
        details_dict['product_min_qty'] = product.find('div', class_='variant-moq').text.replace('Min. Qty. Per Consignee:', '') if product.find('div', class_='variant-moq') else ''
        details_dict['product_final_price'] = product.find('span', class_='variant-list-price').text if product.find('span', class_='variant-list-price') else ''
        details_dict['product_list_price'] = product.find('span', class_='variant-final-price').text if product.find('span', class_='variant-final-price') else ''
        image_link = product.find('span', class_='responsive').find('img')['src']
        details_dict['product_image_link'] = image_link
        product_link = product.find('a', href=True)['href']
        details_dict['product_link'] = f"https://mkp.gem.gov.in{product_link}"
        return details_dict
    
    return None

def process_page(link, page_number):
    url = f"https://mkp.gem.gov.in{link}&page={page_number}"
    content = fetch_page_content(url)
    html_soup = BS(content, 'html.parser') if content else None
    if html_soup.find('div', id='no-results-found'):
        return []
    
    product_detail_list = []
    product_list = html_soup.find_all('li', class_="clearfix")
    for product in product_list:
        details_dict = get_product_details(product)
        if details_dict is not None:
            product_detail_list.append(details_dict)
    return product_detail_list

def gem_products(query):
    product_detail_list = []
    product_pages = getPages(query)
    
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = []
        for link in product_pages:
            initial_url = f"https://mkp.gem.gov.in{link}"
            initial_content = fetch_page_content(initial_url)
            initial_soup = BS(initial_content, 'html.parser')
            pagination_div = initial_soup.find('div', class_='pagination')
            if pagination_div:
                page_links = pagination_div.find_all('a')
                page_numbers = [int(link['href'].split('=')[-1]) for link in page_links]
                highest_page_number = max(page_numbers)

                for page_number in range(1, highest_page_number + 1):
                    futures.append(executor.submit(process_page, link, page_number))

        for future in concurrent.futures.as_completed(futures):
            product_detail_list.extend(future.result())

    return product_detail_list
