from bs4 import BeautifulSoup

html_content = '''
<div id="content-slot">      
    <div class=" row">
        <div class="page-content col-md-12 col-sm-12">
            <div class="relevant-categories">
                <h3 class="category-search-title">Category Results for: "shampoo"</h3>
                <div class="header">
                    <h1>Keywords searched by you appear in following categories, please click on the category name to look at relevant products:</h1>
                    <div class="note-block">
                        <p class="note">Uploading of wrong or misleading product in category not relevant for that product is strictly prohibited and such sellers are liable for strict Administrative action as per GeM GTC clause 3 (A) (xiii). Buyers are also warned not to place contracts against such items listed in wrong or irrelevant categories since all such contract shall be treated as null and void as per GeM GTC. </p>
                    </div>
                </div>
                <ul class="clearfix">
                    <li class="bn-group">
                        <strong>bath and body</strong>
                        <ul class="bn-list">
                            <li class="bn-link "> <a href="/bath-and-body-shampoo-surfactant-based/search#/?q=shampoo">Shampoo, Surfactant Based as per IS 7884<i>(Q4)</i></a></li>
                            <li class="bn-link "> <a href="/bath-and-body-waterless-shampoo-v2-/search#/?q=shampoo">Waterless Shampoo (V2)<i>(Q4)</i></a></li>
                            <li class="bn-link "> <a href="/bath-and-body-shampoo-soap-based/search#/?q=shampoo">Shampoo, Soap Based as per IS 7669<i>(Q4)</i></a></li>
                            <li class="bn-link "> <a href="/bath-and-body-waterless-shampoo/search#/?q=shampoo">Waterless Shampoo as per IS 13498<i>(Q4)</i></a></li>
                        </ul>
                    </li>
                    <li class="bn-group">
                        <strong>Seating</strong>
                        <ul class="bn-list">
                            <li class="bn-link "> <a href="/chairs-shampoo-station/search#/?q=shampoo">Shampoo Station<i>(Q3)</i></a></li>
                        </ul>
                    </li>
                </ul>
            </div>
        </div>
    </div>
</div>
'''

soup = BeautifulSoup(html_content, 'html.parser')

result_dict = {}

categories = soup.find_all('li', class_='bn-group')
for category in categories:
    category_name = category.strong.text.strip()
    links = category.find_all('a')
    category_dict = {link.text.strip(): link['href'] for link in links}
    result_dict[category_name] = category_dict

print(result_dict)
