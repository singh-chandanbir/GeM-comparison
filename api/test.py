def get_page_url(page_number):
    base_url = "https://mkp.gem.gov.in/bath-and-body-shampoo-surfactant-based/search"
    
    if page_number <= 1:
        return base_url
    
    return f"{base_url}?don_load_facets=true&home=false&page={page_number}"

page_number = 3
page_url = get_page_url(page_number)
print(page_url)